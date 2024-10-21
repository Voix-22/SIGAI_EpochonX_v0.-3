import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from datetime import datetime

df = pd.read_csv('task_dataset.csv')

difficulty_encoder = LabelEncoder()
df['Difficulty_Encoded'] = difficulty_encoder.fit_transform(df['Difficulty'])

X = df[['Difficulty_Encoded', 'Urgency', 'Hours_Available_Today']]
y = df['Time_To_Complete']


decision_tree_model = DecisionTreeRegressor()
decision_tree_model.fit(X, y)

def predict_task_completion_time(task_type, difficulty, urgency, hours_today, deadline):
    
    difficulty_encoded = difficulty_encoder.transform([difficulty])[0]
    
    
    task_input = pd.DataFrame({
        'Difficulty_Encoded': [difficulty_encoded],
        'Urgency': [urgency],
        'Hours_Available_Today': [hours_today]
    })
    
    
    task_input_np = task_input.to_numpy()

    
    predicted_time = decision_tree_model.predict(task_input_np)[0]

    
    current_date = datetime.now().date()  
    days_until_deadline = (deadline - current_date).days
    total_hours_available = (days_until_deadline * hours_today) + hours_today
    
    
    if total_hours_available * 60 >= predicted_time:
        return f"Predicted time: {predicted_time:.2f} minutes. Task can be completed before the deadline!"
    else:
        return f"Predicted time: {predicted_time:.2f} minutes. Let's try our best and push to finish the task in time! It's been added to your schedule."
