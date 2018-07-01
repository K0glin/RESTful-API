"""
RESTful API via Flask 
for Machine Learning model <-> wrapper interaction
"""

from pathlib import Path
from sklearn.externals import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# HTTP Constants
HTTP_BAD_REQUEST = 400

# Load the model
MODEL_DIR = Path(__file__).resolve().parents[0]
MODEL_FILE = MODEL_DIR / 'model.pkl'
MODEL = joblib.load(MODEL_FILE)

@app.route('/')
@app.route('/predict')
def predict():
    try:
        result = MODEL.predict(request.args) # use request
    except MODEL.ModelError as err:
        response = jsonify(status='error',
                           error_message=str(err))
        # Sets the status code to 400
        response.status_code = HTTP_BAD_REQUEST
        return response

    return jsonify(status='complete', **result)

if __name__ == '__main__':
    app.run(debug=True)
