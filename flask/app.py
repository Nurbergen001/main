from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def mainPage():
    return render_template('index.html')
@app.route('/about')
def about():
    return 'About'
