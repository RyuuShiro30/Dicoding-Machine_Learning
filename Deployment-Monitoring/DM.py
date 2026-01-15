from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("lars_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    content = request.get_json()
    
    # Ambil data
    data = np.array(content["data"])
    
    # Prediksi
    prediction = model.predict(data)

    return jsonify({
        "prediction": prediction.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
