# 🎬 OTT Churn Prediction System

A full-stack Machine Learning project that predicts customer churn for OTT platforms using behavioral data. This system helps identify users likely to leave, enabling businesses to take proactive retention actions.

---

## 🚀 Features
- 📂 Upload CSV file for prediction  
- 🤖 ML-based churn prediction (XGBoost, Random Forest)  
- 📊 Churn vs Non-Churn percentage output  
- 📈 Interactive dashboard (pie chart visualization)  
- ⚡ Fast and real-time predictions  

---

## 🧠 What is Churn?
Churn refers to customers who stop using a service (e.g., canceling a subscription).  
This project predicts such users based on their activity and engagement patterns.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** Pandas, NumPy, Matplotlib  

---

## 📊 ML Workflow
1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering & Encoding  
4. Model Training (Decision Tree, Random Forest, XGBoost)  
5. Cross-validation & Model Evaluation  
6. Deployment using Flask  

---

## 📁 Project Structure
OTT_CHURN_PREDICTION/
│
├── static/
│ └── css/
│ └── style.css
│
├── templates/
│ └── home.html
│
├── model/
│ ├── ott_churn_prediction.pkl
│ └── encoders.pkl
│
├── app.py
├── sample_churn_data.csv
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ott-churn-prediction.git
cd ott-churn-prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Flask app
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000/

📌 Input Format
Upload a CSV file with the same structure as training data
Required columns include:
age, gender, subscription_type, watch_hours
last_login_days, region, device
payment_method, etc.

📈 Sample Output
Churn: 6%
Non-Churn: 94%

🔮 Future Enhancements
Support Excel/PDF input with auto parsing
User authentication (login/register)
Model improvement with deep learning
Deployment on cloud (AWS/Render)

👩‍💻 Author

Krushnali
Engineering Student | Aspiring Data Scientist

⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
