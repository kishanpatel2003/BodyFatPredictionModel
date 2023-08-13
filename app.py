from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('optimized_random_forest_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['Age'], data['Weight'], data['Height'], data['Neck'],
        data['Chest'], data['Abdomen'], data['Hip'], data['Thigh'],
        data['Knee'], data['Ankle'], data['Biceps'], data['Forearm'],
        data['Wrist']
    ]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')
