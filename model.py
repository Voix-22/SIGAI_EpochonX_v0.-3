import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from datetime import datetime, timedelta

# Generate dataset (or load from file)
num_tasks = 1000
task_types = np.random.choice(['Homework', 'Club', 'Project', 'Revision', 'Exam Preparation'], size=num_tasks)
difficulty_levels = np.random.choice(['Easy', 'Medium', 'Hard'], size=num_tasks)
urgency = np.random.randint(1, 11, size=num_tasks)
time_to_complete = np.random.randint(30, 180, size=num_tasks)  # Random time between 30 and 180 mins
current_date = datetime.now()
deadlines = [current_date + timedelta(days=np.random.randint(1, 15)) for _ in range(num_tasks)]
hours_available_today = np.random.randint(1, 9, size=num_tasks)

# Label encode the difficulty levels
difficulty_encoder = LabelEncoder()
encoded_difficulty_levels = difficulty_encoder.fit_transform(difficulty_levels)

# Create DataFrame for the model
df = pd.DataFrame({
    'Task_Type': task_types,
    'Difficulty_Encoded': encoded_difficulty_levels,
    'Urgency': urgency,
    'Time_To_Complete': time_to_complete,
    'Deadline': deadlines,
    'Hours_Available_Today': hours_available_today
})

# Prepare input data
X = df.drop(columns=['Task_Type', 'Time_To_Complete', 'Deadline'])
y = df['Time_To_Complete']

# Train and compare models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'SVR': SVR(),
    'K-Nearest Neighbors': KNeighborsRegressor()
}

model_mae = {}

# Train and evaluate each model
for name, model in models.items():
    model.fit(X, y)
    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)
    model_mae[name] = mae

# Select the best model based on MAE
best_model_name = min(model_mae, key=model_mae.get)
best_model = models[best_model_name]

print(f"Best model: {best_model_name} with MAE: {model_mae[best_model_name]}")
