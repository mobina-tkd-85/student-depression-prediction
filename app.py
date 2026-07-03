from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load the models
model = None
preprocessor = None

def load_models():
    global model, preprocessor
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
        print("✅ Models loaded successfully!")
        return True
    except FileNotFoundError as e:
        print(f"❌ Error loading models: {e}")
        print("Please ensure model.pkl and preprocessor.pkl are in the same directory.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

# Load models when app starts
models_loaded = load_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not models_loaded:
        return jsonify({'error': 'Models not loaded properly'}), 500
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Create DataFrame from input
        input_data = pd.DataFrame([{
            'Gender': data.get('Gender'),
            'Age': float(data.get('Age')),
            'City': data.get('City'),
            'Academic Pressure': float(data.get('Academic Pressure')),
            'CGPA': float(data.get('CGPA')),
            'Study Satisfaction': float(data.get('Study Satisfaction')),
            'Sleep Duration': data.get('Sleep Duration'),
            'Dietary Habits': data.get('Dietary Habits'),
            'Degree': data.get('Degree'),
            'Have you ever had suicidal thoughts ?': data.get('Have you ever had suicidal thoughts ?'),
            'Work/Study Hours': float(data.get('Work/Study Hours')),
            'Financial Stress': float(data.get('Financial Stress')),
            'Family History of Mental Illness': data.get('Family History of Mental Illness')
        }])
        
        # Preprocess the input
        try:
            processed_data = preprocessor.transform(input_data)
        except AttributeError:
            # If preprocessor doesn't have transform method, use it directly
            processed_data = preprocessor(input_data) if callable(preprocessor) else input_data
        
        # Make prediction
        prediction = model.predict(processed_data)
        
        # Get prediction probability if available
        try:
            probability = model.predict_proba(processed_data)
            confidence = float(probability[0][1]) if prediction[0] == 1 else float(probability[0][0])
        except:
            confidence = None
        
        # Determine risk level
        risk_level = "Low"
        if prediction[0] == 1:
            if confidence and confidence > 0.7:
                risk_level = "High"
            elif confidence and confidence > 0.5:
                risk_level = "Moderate"
            else:
                risk_level = "Moderate"
        
        # Return result
        return jsonify({
            'prediction': int(prediction[0]),
            'risk': risk_level,
            'confidence': confidence
        })
        
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)