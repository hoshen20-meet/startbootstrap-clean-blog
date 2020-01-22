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

@app.route('/spesific-book/<int:Book_id>', methods=(['GET','POST']))
def spesific(Book_id):
    return render_template('spesific-book.html', Books=query_book_by_id(Book_id))

@app.route('/log_in',methods=['POST','GET'])
def log_in():
    if request.method == "GET":
        return render_template ("log_in.html" )
    else:
        name = request.form['uname']
        password = request.form['psw']
        if name == 'admin' and password== 'esports123':
            login_session["admin"]=True
            return redirect(url_for('store'))
        else:
            return render_template ("log_in.html",wrong=True )

    return render_template ("log_in.html" )



@app.route('/add_book',methods=['POST','GET'])
def add_books():
    if request.method == "GET":
        return render_template ("add_book.html" )
    else:
        bookname=request.form['bookname']
        authorname=request.form['authorname']
        price=request.form['price']
        print(request.files)
        f = request.files['bookpic']
        f.save("static/img/"+f.filename)
        add_book(bookname,authorname, price, f.filename)
        Books = query_all_books()
        return render_template("store.html",Books=Books)

    
app.run(debug = True)
