# Anemia-prediction
# 🩺 Anemia Prediction Based On Eye Condition Data

This project aims to predict the presence of anemia using clinical data related to eye condition features such as hemoglobin, MCHC, MCV, and MCH. Machine learning models including **Decision Tree**, **Random Forest**, and **XGBoost** were implemented to classify whether anemia is present.

## 🔍 Project Overview

Anemia is a condition in which the blood lacks enough healthy red blood cells or hemoglobin. Early prediction can help prevent complications. This machine learning application takes key hematological parameters as input and predicts anemia presence.

## 📁 Files in This Repository

| File Name              | Description |
|------------------------|-------------|
| `anemia.csv`           | The dataset used for training and testing the models. |
| `ML.ipynb`             | Jupyter notebook containing data preprocessing, model training, evaluation, and visualization. |
| `xgboost_model.pkl`    | Saved XGBoost model used for deployment. |
| `app.py`               | Flask web application to take input from users and make predictions. |
| `templates/index.html` | HTML page for user input (you should add this to your GitHub if not yet). |

## 🧪 Algorithms Used

- ✅ Decision Tree
- ✅ Random Forest
- ✅ XGBoost

XGBoost performed best and is used in the deployed model.

## ⚙️ How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/anemia-prediction.git
   cd anemia-prediction
   ```

2. **Install dependencies**
   Make sure you have Python 3.8+ installed.

   ```bash
   pip install flask numpy scikit-learn xgboost
   ```

3. **Run the Flask App**
   ```bash
   python app.py
   ```

4. **Visit in Browser**
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to access the prediction UI.

## 💻 Input Fields in UI

- Hemoglobin
- MCHC
- MCV
- MCH

These values are taken as input and the model predicts:
- `Anemia Found`
- `Anemia not found`

## 📊 Model Evaluation (from `ML.ipynb`)

Each model was evaluated on accuracy, precision, recall, and F1-score. The XGBoost model outperformed others and was selected for deployment.

## 📌 Future Improvements

- Add more features (e.g., age, sex, symptoms).
- Improve UI using Streamlit or React frontend.
- Connect to a real-time clinical database for live predictions.

## 🤝 Acknowledgements

- Dataset manually created for academic purposes.
- Models implemented using `scikit-learn` and `xgboost`.

## 📜 License

This project is for educational purposes only.
