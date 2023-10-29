from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('anaemia_detection.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    gender = float(request.form['gender'])
    hemoglobin = float(request.form['hemoglobin'])
    mch = float(request.form['mch'])
    mchc = float(request.form['mchc'])
    mcv = float(request.form['mcv'])

    result = model.predict([[gender,hemoglobin,mch,mchc,mcv]])[0]
    if result==1:
        result = "Anaemia Detection Reports show that you are more likely to be having Anaemia!"
    else:
        result = "Anaemia Detection Reports show that you are not likely to be having Anaemia!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)