from flask import Flask, redirect, session, render_template, request #type: ignore
app = Flask(__name__)

#need this app.secret_key every time we use session to enable it to work.
app.secret_key = "asked1245"

@app.route('/')
def home():
    return redirect('/home')

# /home screen renders the form.html
@app.route('/home')
def r_home():
    return render_template('form.html')

# listener route for form data, note the methods (plural s here)
# takes request.form data and links it to sesson data with the same name. 
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    # redirect always on post to a /result route which will render the result.html below
    return redirect('/result')

@app.route('/result')
def r_result():
    return render_template('result.html')


@app.route('/form')
def form():
    return redirect('/home')

if __name__ == ('__main__'):
    app.run(debug=True)