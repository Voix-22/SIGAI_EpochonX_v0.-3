import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
# Check if dataset already exists
try:
    df = pd.read_csv('task_dataset.csv')
except FileNotFoundError:
    # Generate the dataset and save it if it doesn't exist
    num_tasks = 1000
    task_types = np.random.choice(['Homework', 'Club', 'Project', 'Revision', 'Exam Preparation'], size=num_tasks)
    difficulty_levels = np.random.choice(['Easy', 'Medium', 'Hard'], size=num_tasks)
    urgency = np.random.randint(1, 11, size=num_tasks)
    time_to_complete = np.random.randint(30, 180, size=num_tasks)
    current_date = datetime.now()
    deadlines = [current_date + timedelta(days=np.random.randint(1, 15)) for _ in range(num_tasks)]
    hours_available_today = np.random.randint(1, 9, size=num_tasks)

    # Create the dataset
    df = pd.DataFrame({
        'Task_Type': task_types,
        'Difficulty': difficulty_levels,
        'Urgency': urgency,
        'Time_To_Complete': time_to_complete,
        'Deadline': deadlines,
        'Hours_Available_Today': hours_available_today
    })

    # Save the dataset to CSV for future use
    df.to_csv('task_dataset.csv', index=False)
