from flask import Flask, render_template, request, jsonify
from model import model, le_building, le_day  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  
    try:
        
        building = le_building.transform([data['buildingType']])[0]
        day = le_day.transform([data['day']])[0]
        square = float(data['squareFootage'])
        occupants = float(data['occupants'])
        appliances = float(data['appliances'])
        temperature = float(data['temperature'])

       
        prediction = model.predict([[building, square, occupants, appliances, temperature, day]])
        return jsonify({'prediction': round(float(prediction[0]), 2)})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)