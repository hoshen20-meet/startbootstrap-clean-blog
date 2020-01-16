from flask import Flask, render_template, request, redirect, url_for

from flask import session as login_session

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
 
@app.route('/hello')
def hello():
    return 'Hello, World'
 
app.run(debug = True)
