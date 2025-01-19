from flask import Flask,redirect,render_template,request,make_response,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/flask_app'

db  = SQLAlchemy(app)
class FlaskUser(db.Model):

    name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),primary_key = True,nullable = False)
    password = db.Column(db.String(100),nullable = False)

    def __repr__(self):
        return f'name : {self.name}'
    

class Notes(db.Model):
    email = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.String(255), primary_key=True, nullable=False)
    content = db.Column(db.Text, nullable=False)  # Changed from db.String to db.Text

    def __repr__(self):
        return f'title : {self.title}, email : {self.email}, date : {self.datetime}'


with app.app_context():
    db.create_all()


@app.route('/',methods = ['POST','GET'])
def index():
    email = request.cookies.get('email')
   
    if email:
        return redirect('/home')
    return redirect('/login')


@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        isUserExist = FlaskUser.query.filter_by(email=email).first()

        if isUserExist and isUserExist.password == password:
            response = make_response(redirect('/home'))
            response.set_cookie('email',email,max_age=60*60*24)
            return response
        else:
           
            return render_template('login.html')

    return render_template('login.html')

@app.route('/signup',methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        obj = FlaskUser(name = name, email = email,password = password)
        db.session.add(obj)
        db.session.commit()
        response = make_response(redirect('/login'))
        response.set_cookie('email',email,max_age=60*60*24)
        return response
    return render_template('signup.html')


@app.route('/home',methods = ['POST','GET'])
def home():
    email = request.cookies.get('email')
    topics = Notes.query.filter_by(email = email).all()

    return render_template('home.html',topics = topics,title = '',content = '')


@app.route('/topicadd',methods = ['POST','GET'])
def topicadd():
    email = request.cookies.get('email')
    title = request.form.get('title')
    datetime_ = datetime.now()
    content = request.form.get('content')
    
    obj = Notes(email = email,title=title,datetime=datetime_,content=content)
    db.session.add(obj)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/shownotes',methods = ['POST','GET'])
def shownotes():
    email = request.cookies.get('email')
    title = request.form.get('Lefttitle')
    datetime = request.form.get('Leftdatetime')

    obj = Notes.query.filter_by(email = email,datetime = datetime,title = title).first()
   
    content = obj.content
    topics = Notes.query.filter_by(email = email).all()
    return render_template('home.html',topics = topics,title = title,content = content)




@app.route('/logout')
def logout():
        response = make_response(redirect('/login'))
        response.set_cookie('email','',expires=0)
        return response

if __name__ == '__main__':
    app.run(debug=True)






