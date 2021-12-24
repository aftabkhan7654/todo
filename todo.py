from flask import Flask, render_template, request, redirect, url_for,session
from flask_mysqldb import MySQL 
import MySQLdb.cursors
import re 

todo = Flask(__name__)

todo.secret_key = 'your secret key'

todo.config['MYSQL_HOST'] = 'localhost'
todo.config['MYSQL_USER'] = 'root'
todo.config['MYSQL_PASSWORD'] = 'aftab'
todo.config['MYSQL_DB'] = 'todo_program'

mysql = MySQL(todo)

@todo.route('/')
@todo.route('/login', methods =['GET','POST'])
def login():
     msg=''
     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(mysql.cursor.dictcursor)
        cursor.execute('select * from persone where username=% s and password=%s',(username,password))
        persone = cursor.fetchone()
        if persone:
            session['loggedin'] = True
            session['persone_id'] = persone['persone_id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return render_template ('mainpage.html', msg=msg)
        else :
            msg = 'Incorrect username and password'
     return render_template('login.html',msg=msg)

@todo.route('/logout')
def logout():
    session.pop('loggedin',none)
    session.pop('Persone_id',none)
    session.pop('username',none)
    return redirect(url_for('login'))

@todo.route('/register', methods = ['GET','POST'])
def register():
     msg = ''
     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'Email' in request.form and 'city' in request.form:
          username = request.form['username']
          password = request.form['password']
          Email = request.form['Email']
          city = request.form['city']
          cursor = mysql.connection.cursor(MySQL.cursors.DictCurso)
          cursor.execute('select * from persone where username = %s', (username,))
          add = cursor.fetchone()
          if persone :
            msg = 'Account already exist !'
          elif not re.match(r' [^@]+@[^@]+\.[^@]+', Email):
             msg = 'invalid Email adress !'
          elif not re.match(r'[A-Za-z0-9]+', username):
             msg = 'name must contain only character and numbers !'
          else :
             cursor.execute('insert into persone value (null, % s,% s,% s,% s)' , (username,password,Email,city,))
             mysql.connection.commit()
             msg = 'successfully redister !'
     elif request.method == 'POST': 
          msg = 'fill out the form !'
     return render_template('register.html',msg=msg)

todo.route("/mainpage")
def mainpage():
  if 'loggedin' in session:
     return render_template("index.html")
  return redirect(url_for('login'))

if __name__ == "__main__":
    todo.run(host="localhost", port = int("5001"))
#changes saved
