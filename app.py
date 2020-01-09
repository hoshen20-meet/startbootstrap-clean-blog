from flask import Flask, render_template, request, redirect, url_for

from flask import session as login_session

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/hello')
def hello():
    return 'Hello, World'
 
app.run(debug = True)
