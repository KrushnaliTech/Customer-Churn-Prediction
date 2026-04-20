from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__, template_folder=r"D:\OTT_churn_prediction\templates")


# -----------------------------
# Load your trained model and encoders
# -----------------------------
MODEL_PATH = "D:/OTT_churn_prediction/models/ott_churn_prediction.pkl"
ENCODER_PATH = "D:/OTT_churn_prediction/models/encoders.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

# -----------------------------
# Route: Home page
# -----------------------------
@app.route('/')
def index():
    return render_template('home.html')

# -----------------------------
# Route: Prediction API
# -----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Please upload a valid CSV file"}), 400

    try:
        df = pd.read_csv(file)

        expected_columns = [
            'age', 'gender', 'subscription_type', 'watch_hours', 'last_login_days',
            'region', 'device', 'monthly_fee', 'payment_method', 'number_of_profiles',
            'avg_watch_time_per_day', 'favorite_genre'
        ]

        for col in expected_columns:
            if col not in df.columns:
                return jsonify({"error": f"Missing required column: {col}"}), 400

        for col, encoder in encoders.items():
            if col in df.columns:
                df[col] = encoder.transform(df[col])

        preds = model.predict(df)
        churn_count = int((preds == 1).sum())
        non_churn_count = int((preds == 0).sum())

        return jsonify({"churn": churn_count, "non_churn": non_churn_count})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Run the app
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
