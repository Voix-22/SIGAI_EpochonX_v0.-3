# SIGAI_EpochonX_v0.-3.
# Study Sync

## Team Members
- Vani Sugovind
- Poornima
- Reshma Sri

## Problem Statement
Students often struggle to manage their time effectively, leading to stress, lower academic performance, and reduced participation in extracurricular activities like clubs. Traditional planning methods can be cumbersome and may not adapt to individual needs. 

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
- **Streamlit**: This is for building the AI Study Planner user interface.
- **Decision Tree Regression**: For predicting the time to complete tasks.
- **Gemini API**: Integrated Gemini API for chatbot functionality.

## Challenges Faced
- Difficulty in obtaining a relevant dataset for training the model.
- Limited time for development and testing phases.
- Selection of the optimal prediction model.

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

## Future Aspects

### Collect Reliable Dataset from Users
As users interact with the app, we aim to collect real-world data on their study habits, time management, and task completion times. This will help improve the accuracy of our time predictions and enhance the overall user experience.

### Use of Reinforcement Learning
Incorporating reinforcement learning can allow the model to adapt and improve its predictions based on feedback. As more users engage with the system and complete tasks, the AI will learn to better estimate completion times and optimize schedules for individual users.

### Personalized Learning Insights
Incorporate machine learning models that adapt over time, providing students with personalized recommendations on task prioritization, study strategies, and more based on their performance and study habits.

### Collaboration Features
Introduce collaboration tools where students can share their tasks, deadlines, and progress with peers, making it easier to work on group projects or share study plans.

### Advanced AI Chatbot Features
Expand the chatbot's capabilities to include study tips, reminders, motivational nudges, and even tutoring in specific subjects using large language models.

### Progress Tracking and Analytics
Add visual analytics to track task completion rates, study hours, and efficiency over time, helping students identify areas for improvement.

### Integration with Calendar Apps
Sync with external calendar applications like Google Calendar or Microsoft Outlook to automatically populate deadlines and scheduled study sessions for better time management.

### Customizable Task Templates
Allow users to create and save custom templates for recurring tasks or projects, streamlining task creation and scheduling for common study activities.

### Gamification Features
Introduce gamification elements like earning badges or points for completing tasks or meeting deadlines, motivating users to stay on track with their study schedules.

## Conclusion
The AI Study Planner aims to enhance students' study efficiency by providing personalized study schedules and real-time assistance through an AI chatbot. We welcome feedback, contributions, and suggestions for future improvements!



