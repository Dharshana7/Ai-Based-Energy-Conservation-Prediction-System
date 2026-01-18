
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "energy_data.csv")

df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.strip().str.lower()

le_building = LabelEncoder()
le_day = LabelEncoder()

df['building type'] = le_building.fit_transform(df['building type'])
df['day of week'] = le_day.fit_transform(df['day of week'])

X = df[['building type', 'square footage', 'number of occupants',
        'appliances used', 'average temperature', 'day of week']]
y = df['energy consumption']

model = LinearRegression()
model.fit(X, y)

def predict_energy(data):
    
    if data['building_type'] in le_building.classes_:
        building = le_building.transform([data['building_type']])[0]
    else:
        
        building = 0

    
    if data['day_of_week'] in le_day.classes_:
        day = le_day.transform([data['day_of_week']])[0]
    else:
        day = 0

    features = [[
        building,
        float(data['square_footage']),
        int(data['occupants']),
        int(data['appliances']),
        float(data['temperature']),
        day
    ]]

    prediction = model.predict(features)
    return round(float(prediction[0]), 2)