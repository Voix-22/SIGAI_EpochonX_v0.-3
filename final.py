import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime
import google.generativeai as genai
from prediction import predict_task_completion_time


st.title("Study Sync")

st.write("This is a simple app to plan your study schedule. It also predicts the time to finish your tasks so you are always on track.")


if 'tasks' not in st.session_state:
    st.session_state.tasks = []


def add_task(task_type, work_description, urgency, difficulty, deadline, schedule_date):
    task = {
        "Task Type": task_type,
        "Work Description": work_description,
        "Urgency": urgency,
        "Difficulty": difficulty,
        "Deadline": deadline,
        "Scheduled Date": schedule_date,
    }
    st.session_state.tasks.append(task)


task_type = st.selectbox("Select Task Type:", ["Homework", "Project", "Revision", "Exam Preparation", "Club"])
work_description = st.text_input("Enter Work Description:")
urgency = st.slider("Urgency Level (1 to 10):", 1, 10)
difficulty = st.radio("Difficulty Level:", ["Easy", "Medium", "Hard"])
deadline = st.date_input("Select Deadline:", value=pd.to_datetime('today'))
schedule_date = st.date_input("Select Scheduled Date:", value=pd.to_datetime('today'))
hours_available_today = st.number_input("Hours Available Today:", min_value=1, max_value=24)  


if st.button("Add Task"):
    if work_description:  
        add_task(task_type, work_description, urgency, difficulty, deadline, schedule_date)
        st.success("Your task has been added!")
    else:
        st.error("Please enter a work description!")


def urgency_color(urgency):
    if urgency <= 3:
        return 'background-color: #c6efce; color: black;'  # Light green for low urgency
    elif urgency <= 6:
        return 'background-color: #ffeb9c; color: black;'  # Light yellow for medium urgency
    else:
        return 'background-color: #f8d7da; color: black;'  # Light red for high urgency


st.header("Scheduled Tasks")


if st.session_state.tasks:
    
    tasks_df = pd.DataFrame(st.session_state.tasks)
    
    
    def highlight_rows(row):
        return [urgency_color(row['Urgency'])] * len(row)
    
    styled_df = tasks_df.style.apply(highlight_rows, axis=1)

    
    st.write(styled_df)
else:
    st.write("No tasks added yet. Use the fields above to add tasks!")


st.header("Predict Task Completion Time")


if st.button("Predict Completion Time"):
    predicted_time_message = predict_task_completion_time(task_type, difficulty, urgency, hours_available_today, deadline)
    st.write(predicted_time_message)

# Configure the Google API
genai.configure(api_key="YOUR_API_KEY")


generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])


def chat_with_bot(user_input):
    response = chat_session.send_message(user_input)
    return response.text


st.header("Chat with Study Sync")
st.write("Ask Your Doubts To Our Smart Study Sync")


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


user_input = st.text_input("Ask the bot a question")

clear_button = st.button("Clear Chat")


if user_input:
    bot_response = chat_with_bot(user_input)
    st.session_state.chat_history.insert(0, {"user": user_input, "bot": bot_response}) 
    user_input = ""  


if clear_button:
    st.session_state.chat_history = []  

if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        st.write(f"*You:* {chat['user']}")
        st.write(f"*Bot:* {chat['bot']}")
