__author__ = { 'name': 'David Serrano', 'code': 'T00061734', 'email': 'fserrano@utb.edu.co' }

from flask import Flask, render_template, request, redirect, flash
import json
from classes import person

app = Flask(__name__)

app.secret_key = 'mysecretkey'

data = { 'contacts': [] }

@app.route('/')
def index():
	return render_template('index.html', data=data['contacts'])

@app.route('/add', methods=['POST'])
def add_contact():
	contact = person.Contact(len(data['contacts']))
	contact._fullname = request.form['fullname']
	contact._phone = request.form['phone']
	contact._email = request.form['email']
	data['contacts'].append(contact)
	json_data = json.dumps(data, indent=4, cls=person.ContactEncoder)
	with open('./static/json/data.json', 'w') as file:
		json.dump(json.loads(json_data), file, indent=4)

	flash('Contact added successfully')
	return redirect('/')

@app.route('/edit/<string:id>')
def edit(id):
	return render_template('edit.html', data=data['contacts'][int(id)])

@app.route('/update/<string:id>', methods=['POST'])
def update(id):
	data[id]._fullname = request.form['fullname']
	data[id]._phone = request.form['phone']
	data[id]._email = request.form['email']
	flash('Contact updated successfully')
	return redirect('/')

@app.route('/delete/<string:id>')
def delete(id):
	# text = ''
	# with open('./static/json/data.json') as file:
	# 	json_data = json.load(file)
		# for contact in json_data:
			# text += ()
	json_data = str(json.load(open('./static/json/data.json')))
	print(json_data)
	for row in range(len(json_data)):
		if json_data[row]['_id'] == id:
			json_data.pop(row)

	# # data['contacts'].pop(int(id))
	# open('./static/json/data.json', 'w').write(json.dumps(json_data, indent=4))
	flash('Contact removed successfully')
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True, port=1000, host='0.0.0.0')