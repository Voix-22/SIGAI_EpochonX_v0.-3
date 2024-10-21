# SIGAI_EpochonX_v0.-3.
# Study Sync

## Team Members
- Vani Sugovind
- Poornima
- Reshma Sri

## Problem Statement
Students often struggle to manage their time effectively, leading to stress, lower academic performance, and reduced participation in extracurricular activities like clubs. Traditional methods of planning can be cumbersome and may not adapt to individual needs. 

## Key Features

### 1. Task Management
Users can add tasks related to their study schedules, including:
- **Task Type**: Select from various types like Homework, Project, Revision, Exam Preparation, and Club activities.
- **Work Description**: Input specific descriptions for each task.
- **Urgency Level**: Set an urgency level from 1 to 10 using a slider.
- **Difficulty Level**: Choose a difficulty level (Easy, Medium, Hard).
- **Deadlines**: Set deadlines for tasks.
- **Scheduled Dates**: Specify when to work on each task.

The application tracks all added tasks and displays the schedule.

### 2. Time Prediction
Our AI model predicts the time needed to complete the user-given task, providing realistic expectations for better planning.

### 3. Chatbot Integration
A chatbot interface allows users to interact with an AI powered by Google Generative AI (Gemini). Users can ask questions related to their study plans or seek general assistance.

## Tech Stack
- **Streamlit**: For building the user interface of the AI Study Planner.
- **Decision Tree Regression**: For predicting the time to complete tasks.
- **Gemini API**: Integrated Gemini API for chatbot functionality.

## Challenges Faced
- Difficulty in obtaining a relevant dataset for training the model.
- Limited time for development and testing phases.
- Selection of the optimal model for prediction.

### How We Overcame These Challenges
- Generated a random dataset using Pandas and NumPy.
- Divided the work among the team and committed it to GitHub.
- Tried different regressor models and compared their Mean Absolute Error (MAE). Selected Decision Tree as it provided the optimal output.

## Tech Used
- **Streamlit**: For creating the web application.
- **Gemini API**: Google Generative AI library for chatbot functionality.
- **Pandas & NumPy**: For managing data and tasks.
- **Scikit-learn**: For implementing machine learning algorithms, specifically Decision Trees.
- **Python**: Programming language used for development.

## Setup Instructions


### Clone the Repository
### Install Dependencies
### Add the API Key
### Run the Application


