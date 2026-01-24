AI-Based Energy Consumption Prediction System
Overview:

This project is a web-based application that uses artificial intelligence and machine learning to predict energy consumption in buildings. Users can enter building and environmental parameters, and the system provides real-time predictions to support energy optimization and sustainability efforts.

The application integrates a machine learning model with a Flask backend and an interactive frontend built using HTML, CSS, and JavaScript.

Problem Statement:

Accurately estimating building energy consumption is challenging due to varying factors such as occupancy, appliance usage, environmental conditions, and time-based patterns. Traditional approaches rely on static averages and manual calculations, which often lead to inefficient energy usage and increased costs. This project addresses this issue by applying machine learning to generate data-driven predictions.

Solution:

The system uses a Linear Regression machine learning model trained on historical energy usage data. Categorical variables such as building type and day of the week are encoded before training.

Users provide inputs through the web interface, which are sent to the Flask backend for processing. The trained model analyzes the inputs and returns a predicted energy consumption value, which is then displayed on the frontend.

Features:

Real-time energy consumption prediction

AI-powered machine learning model

User-friendly web interface

Flask backend integration

Sustainable energy optimization support

Modular and scalable architecture

Technologies Used:

Python

Flask

Scikit-learn

Pandas

NumPy

HTML

CSS

JavaScript

Dataset:

The dataset (energy_data.csv) contains the following columns:

Building Type

Square Footage

Number of Occupants

Appliances Used

Average Temperature

Day of Week

Energy Consumption

This data is used to train the machine learning model.


Target Users:

Building owners, facility managers, energy managers, small business owners, and residential users interested in monitoring and optimizing energy consumption.

Impact:

The project promotes data-driven decision-making for energy efficiency, cost reduction, and environmental sustainability. It helps users better understand consumption patterns and supports long-term energy conservation practices.

Project Structure:
├── app.py
├── model.py
├── energy_data.csv
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js

Future Enhancements:

Integration of advanced ML models

Real-time IoT sensor data support

Visualization dashboards

Cloud deployment

User authentication

Historical prediction tracking

How to Run the Project:

Install dependencies:

pip install flask pandas scikit-learn numpy


Run the application:

python app.py


Open a browser and go to:

http://127.0.0.1:5000/

Conclusion:

This project demonstrates how artificial intelligence and machine learning can be applied to real-world sustainability challenges. By predicting energy usage through data-driven models, the system supports responsible consumption and environmental awareness.

Demo Video Link:https://1drv.ms/v/c/f74857fe64a549da/IQA5H41vQHICTaPORHYlQQHOAYfKD7HlB_gMSTqa2sKsOvw?e=lnofs6


If you want, I can also add a “System Architecture” section explaining how data flows from the user to the model and back to the UI.

