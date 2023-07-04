from flask import Flask, jsonify,render_template,request, redirect, url_for, session
# import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ram@27102003'
app.config['MYSQL_DB'] = 'pharma'


mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(
			'SELECT * FROM patients WHERE email = % s \
			AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['patient_ID']
			session['username'] = account['name']
			msg = 'Logged in successfully !'
			return render_template('home.html', msg=msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'name' in request.form and 'password' in request.form and'email' in request.form and 'street_address' in request.form and 'city' in request.form and'state' in request.form and 'blood_group'in request.form and 'gender' in request.form and 'contact_number' in request.form and 'age' in request.form and  'locality' in request.form and 'marital_status' in request.form:
		name = request.form['name'] #
		contact_number = request.form['contact_number'] #
		street_address = request.form['street_address'] #
		locality = request.form['locality'] #
		city = request.form['city'] # 
		state = request.form['state'] #
		email = request.form['email'] #
		password = request.form['password'] #
		blood_group = request.form['blood_group'] #
		age = request.form['age'] #
		marital_status = request.form['marital_status']
		gender = request.form['gender'] #
		
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO patients (name,password,email,street_address,city,state,blood_group,gender,contact_number,age,locality,marital_status) \
		( % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)',(name, password, email,street_address, city, state,blood_group, gender, contact_number,age,locality,marital_status))
		mysql.connection.commit()
		msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg=msg)

@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("index.html")
	return redirect(url_for('login'))

@app.route("/history")
def history():
	if 'loggedin' in session:
		return render_template("history.html")
	return redirect(url_for('login'))

@app.route("/hdata")
def hdata():
	if 'loggedin' in session:
		cnx=mysql.connection.cursor()
		cnx.execute("SELECT d.name, h.prescription_report, h.disease_detected_date, h.treatment_end_date, hs.name FROM doctors AS d, patient_history AS h, hospitals AS hs WHERE h.patient_ID = %s and d.doctor_ID = h.doctor_ID and h.hospital_ID = hs.hospital_ID;",(session["id"],))
		data=[{'dname':i[0],'pres':i[1],'ddate':i[2],'edate':i[3],'hname':i[4]} for i in cnx.fetchall()]
		cnx.close()
		return jsonify(data)
	return redirect(url_for('login'))


@app.route("/dashboard")
def dashboard():
	if 'loggedin' in session:
		return render_template("dashboard.html")
	return redirect(url_for('login'))

@app.route("/ddata")
def ddata():
	if 'loggedin' in session:
		cnx=mysql.connection.cursor()
		cnx.execute("SELECT name,email,contact_number,address FROM patients WHERE patient_ID = %s",(session["id"],))
		data=[{'name':i[0],'email':i[1],'phone':i[2],'address':i[3]} for i in cnx.fetchall()]
		cnx.close()
		return jsonify(data)
	return redirect(url_for('login'))

# @app.route("/cart")
# def cart():
# 	if 'loggedin' in session:
# 		return render_template("cart.html")
# 	return redirect(url_for('login'))

@app.route("/cartdata1")
def cartdata1():
	if 'loggedin' in session:
		cnx=mysql.connection.cursor()
		cnx.execute("SELECT p.medicine_name, p.quantity,q.price FROM cart AS p, medicines AS q WHERE q.medicine_name = p.medicine_name AND patient_ID = %s",(session["id"],))
		data=[{'name':i[0],'quantity':i[1],'price':i[2]} for i in cnx.fetchall()]
		cnx.close()
		
		return jsonify(data)
	return redirect(url_for('login'))

@app.route("/display")
def display():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s',
					(session['id'], ))
		account = cursor.fetchone()
		return render_template("display.html", account=account)
	return redirect(url_for('login'))

@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template("home.html")


@app.route("/update", methods=['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			organisation = request.form['organisation']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']
			postalcode = request.form['postalcode']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute(
				'SELECT * FROM accounts WHERE username = % s',
					(username, ))
			account = cursor.fetchone()
			if account:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'name must contain only characters and numbers !'
			else:
				cursor.execute('UPDATE accounts SET username =% s,\
				password =% s, email =% s, organisation =% s, \
				address =% s, city =% s, state =% s, \
				country =% s, postalcode =% s WHERE id =% s', (
					username, password, email, organisation,
				address, city, state, country, postalcode,
				(session['id'], ), ))
				mysql.connection.commit()
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg=msg)
	return redirect(url_for('login'))

@app.route("/productdata")
def get_datapr():
    cnx=mysql.connection.cursor()
    cnx.execute("Select medicine_name from medicines")
    data=[{'name':i[0]} for i in cnx.fetchall()]
    cnx.close()
    return jsonify(data)

@app.route("/doctordata")
def get_datadc():
    cnx=mysql.connection.cursor()
    cnx.execute("Select name, medical_field from doctors")
    data=[{'name':i[0],'field':i[1]} for i in cnx.fetchall()]
    cnx.close()
    return jsonify(data)

@app.route("/labtestdata")
def get_datalb():
    cnx=mysql.connection.cursor()
    cnx.execute("Select test_name from medical_tests")
    data=[{'name':i[0]} for i in cnx.fetchall()]
    cnx.close()
    return jsonify(data)

@app.route("/product")
def product():
	return render_template("product.html")

@app.route("/doctor")
def doctor():
	return render_template("doctor.html")

@app.route("/labtest")
def labtest():
	return render_template("labtest.html")

@app.route("/pharmadata/<name>", methods=['GET', 'POST'])
def pharmadata(name):
	return render_template("pharmacylist.html",data=name)

@app.route("/pharmadata1/<name>", methods=['GET', 'POST'])
def pharmadata1(name):
	cnx=mysql.connection.cursor()
	cnx.execute("SELECT p.name ,pm.price FROM  medicines_in_pharmacy AS pm, pharmacies AS p WHERE pm.medicine_name = %s and p.pharmacy_ID = pm.pharmacy_ID",(name,))
	data=[{'name':i[0], 'price':i[1]} for i in cnx.fetchall()]
	cnx.close()
	return jsonify(data)

if __name__ == "__main__":
	app.run(host="localhost", port=int("5000"))
