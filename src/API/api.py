from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import joblib
import os
import pandas as pd

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

def load_model(model):
    path = f"./{model}.sav"
    model = None
    with open(path, 'rb') as file:
        model = joblib.load(file)
    if model is None:
        raise Exception(f"Model {model} not found")
    return model

model = load_model('model')

fields = [
    'age',
    'academic_pressure',
    'study_satisfaction',
    'dietary_habits',
    'degree',
    'suicidal_thoughts',
    'workstudy_hours',
    'financial_stress'
    ]

@app.route("/")
def index():

    message = "online"
    return Response(message, mimetype='text/plain', content_type='text/plain')

@app.route('/', methods=['POST'])
def api():

    input = request.get_json()
    
    # Valida campos
    for key in fields:
        if key not in input:
            return {'error': f"Field {key} not found"}, 400
        if not isinstance(input[key], (int, float)):
            return {'error': f"Field {key} must be a number"}, 400
        if key == 'workstudy_hours' and input[key] > 24:
            return {'error': f"Field {key} exceeded 24 hours"}, 400
        if key == 'suicidal_thoughts' and input[key] not in [0, 1]:
            return {'error': f"Field {key} must be 0 or 1"}, 400
        
    # Create a dataset to be processed.
    df_input = pd.DataFrame([[input[key] for key in fields]], columns=fields)

    # Predict
    pred = model.predict(df_input)

    result = bool(pred[0])

    return jsonify({
        "success": True,
        "depression": result
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
