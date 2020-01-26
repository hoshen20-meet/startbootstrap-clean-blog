from flask import Flask, render_template, request, redirect, url_for
from model import *
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

 
@app.route('/')
def index():
    return render_template('index.html',Article=session.query(article).all())

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

@app.route('/specific_article/<int:article_id>', methods=(['GET','POST']))
def spesific(article_id):
    return render_template('specific-book.html', article=query_article_by_id(article_id))

@app.route('/log_in',methods=['POST','GET'])
def log_in():
    if request.method == "GET":
        return render_template ("log_in.html" )
    else:
        name = request.form['uname']
        password = request.form['psw']
        if name == 'admin' and password== 'esports123':
            login_session["admin"]=True
            return redirect(url_for('add_books'))
        else:add_book
        return render_template ("log_in.html",wrong=True )

    return render_template ("log_in.html" )



@app.route('/add_book',methods=['POST','GET'])
def add_books():
    if request.method == "GET":
        return render_template ("add_book.html" )
    else:
        title=request.form['title']
        author=request.form['author']
        date=request.form['date']
        paragraph=request.form['paragraph']
        add_article(title,author, paragraph, date)
        Article = query_all_article()
        return render_template("index.html",Article=Article)

    
app.run(debug = True)
