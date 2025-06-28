from flask import Flask, render_template, request
import pickle
import numpy as np

with open('xgboost_model.pkl', 'rb') as file:
    xgboost_model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    hemoglobin = float(request.form['hemoglobin'])
    mchc = float(request.form['mchc'])
    mcv = float(request.form['mcv'])
    mch = float(request.form['mch'])

    input_data = np.array([[hemoglobin, mchc, mcv, mch]])
    prediction = xgboost_model.predict(input_data)

    result = "Anemia Found" if prediction == 1 else "Anemia not found"
    return result

if __name__ == '__main__':
    app.run(debug=True)
