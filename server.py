from cgitb import reset
from flask import Flask, redirect, session, render_template #type: ignore
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/home')

@app.route('/home')
def r_home():
    return render_template('form.html')

@app.route('/result')
def r_result():
    return render_template('result.html')

@app.route('/form')
def form():
    return redirect('/home')

if __name__ == ('__main__'):
    app.run(debug=True)