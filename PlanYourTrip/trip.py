from flask import Flask, render_template, request,redirect,url_for
import pymysql as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tour/')
def tours():
    return render_template('tour.html')

@app.route('/signup/')
def sign():
    return render_template('signup.html')

@app.route('/signup1/', methods = ['GET', 'POST'])
def signup_details():
    name = request.form.get('name')
    email = request.form.get('mail')
    try:
        db = sql.connect(host = 'localhost', port = 3306, user = 'root', password = 'rootsql', database = 'trips')
    except Exception as e:
        return f"{e}"
    else:
        c = db.cursor()
        c.execute(f"select * from newsletter where name='{name}'")
        data = c.fetchone()
        if data:
            error = 'User already registered!!'
            return render_template('signup.html', error = error)
        else:
            c.execute(f"insert into newsletter values('{name}', '{email}')") 
            db.commit()
            return redirect(url_for('home'))
            #return render_template('index.html')  

@app.route('/country/<country_name>/')
def countries(country_name):
    try:
        db = sql.connect(host = 'localhost', port = 3306, user = 'root', password = 'rootsql',database='trips')
    except Exception as e:
        return f"{e}"
    else:
        c = db.cursor()
        c.execute(f"select description from country_desc where country_name = '{country_name}'")
        data = c.fetchone()
        return render_template('country.html', c=country_name,d=data[0])

app.run(host="localhost",port=5000,debug=True)