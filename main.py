__author__ = { 'name': 'David Serrano' }

from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactos'
db = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
	cursor = db.connection.cursor()
	cursor.execute('SELECT * FROM contacts')
	data = cursor.fetchall()
	return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cursor = db.connection.cursor()
		cursor.execute(
			'INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email)
		)
		db.connection.commit()
		flash('Contact added successfully')
		return redirect('/')

@app.route('/edit/<string:id>')
def edit(id):
	cursor = db.connection.cursor()
	cursor.execute('SELECT * FROM contacts WHERE id = %s' % id)
	data = cursor.fetchall()
	return render_template('edit.html', data=data[0])

@app.route('/update/<string:id>', methods=['POST'])
def update(id):
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cursor = db.connection.cursor()
		cursor.execute(
			'UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s', (fullname, phone, email, id)
		)
		db.connection.commit()
		flash('Contact updated successfully')
		return redirect('/')

@app.route('/delete/<string:id>')
def delete(id):
	cursor = db.connection.cursor()
	cursor.execute('DELETE FROM contacts WHERE id = %s' % id)
	db.connection.commit()
	flash('Contact removed successfully')
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True, port=1000)
