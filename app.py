from flask import Flask, render_template, url_for, request

import pickle


# returns array of potential conditions
def predict_conditions(age, gender, told_to_exercise, bmi, water, weight_kg, country):
    conditions = {
        'DLQ010': 'Serious difficulty hearing',
        'DLQ020': 'Serious difficulty seeing',
        'DLQ040': 'Serious difficulty concentrating, remembering or making decisions',
        'DLQ050': 'Serious difficulty walking or climbing',
        'DLQ060': 'Difficulty dressing or bathing',

        'CDQ001': 'Pain or discomfort in chest',
        'CDQ008': 'Severe pain across chest',
        'CDQ010': 'Shortness of breath',

        'BPQ020': 'Hypertension/high blood pressure',
        'BPQ080': 'High blood cholesterol level',

        'AGQ030': 'Hay fever',
        'MCQ010': 'Asthma',
        'MCQ053': 'Anemia/tired blood/low blood',
        'MCQ070': 'Psoriasis',
        'MCQ080': 'Obesity',
        'MCQ082': 'Celiac Disease',
        'MCQ160A': 'Arthritis',
        'MCQ160B': 'Congestive heart failure',
        'MCQ160C': 'Coronary heart disease',
        'MCQ160D': 'Angina',
        'MCQ160E': 'Heart Attack',
        'MCQ160F': 'Stroke',
        'MCQ160G': 'Emphysema',
        'MCQ160K': 'Chronic Bronchitis',

    }

    in_us = 0
    t_o_e = 0
    gen = 0  # female
    if country == 'United States':
        in_us = 1
    if told_to_exercise == 'Yes':
        t_o_e = 1
    if gender == 'Male':
        gen = 1

    retArr = []
    for k in conditions:
        model = pickle.load(open(f"{k}.pickle", "rb"))
        s = model.predict([[age, gen, t_o_e, bmi, water, weight_kg, in_us]])[0]

        if s == 1.:
            retArr.append(conditions.get(k))
    return retArr


app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        country = request.form["country"]
        age = request.form["age"]
        exercise = request.form["exercise"]
        weight = request.form["weight"]
        BMI = request.form["BMI"]
        gender = request.form["gender"]
        water = request.form["water"]

        arr = predict_conditions(age, gender, exercise, BMI, water, weight, country)
        res = ""
        for i in range(len(arr) - 1):
            res += arr[i] + ', '
        if len(arr) > 0:
            res += arr[-1]
        else:
            res = "You look healthy!"
    return render_template('result.html', results= res)


if __name__ == '__main__':
    app.run(debug=True)
