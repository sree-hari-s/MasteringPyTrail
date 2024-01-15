from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return f"Form Submitted Successfully\nEmail:{email} Password:{password}"

if __name__ == '__main__':
    app.run(debug=True)