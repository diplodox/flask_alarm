#! /usr/bin/python

from subprocess import call
from flask import Flask, render_template, session, redirect
from scan_folder import make_tree
from db_manager import *
from check_parc import *

app = Flask(__name__, static_url_path = "", static_folder = "static")

liste = make_tree("/home/pi/Documents/python/flask_alarm/static/photos")

for item in query_db('select * from todo_items'):
    print item[1], ' : ', item[0], ' / ', item[2]

parc_machine = return_parc()

# HOME
@app.route('/')
def index():
	state="undefined"

	if 'alarm_status' in session:
    	alarm_status = session['alarm_status']
    	state = session['alarm_status']
	
	return render_template("home.html", state=state, liste=liste)

# ROUTES ALARM
@app.route('/alarm_start')
def alarm_start():
	# nohup python script.py &
	call(["python", "/home/pi/Documents/python/flask_alarm/daemon_alarm_light.py","start", "&"])
	session['alarm_status'] = 'ON'

	photos="Aucune photos"
	return render_template("home.html", state=session['alarm_status'], liste=photos)


@app.route('/alarm_stop')
def alarm_stop():
	call(["/home/pi/Documents/python/flask_alarm/daemon_alarm_light.py","stop"])
	session['alarm_status'] = 'OFF'

	photos="Aucune photos"
	return render_template("home.html", state=session['alarm_status'], liste=photos)


# ROUTE PHOTOS
@app.route('/photos')
def maj_photos():
	
	#t2 = make_tree("/home/pi/Documents/PIRemail/photos")
	liste_maj = make_tree("/home/pi/Documents/flask_alarm/static/photos")
	return render_template("liste_photos.html", liste_photos=liste_maj)


# ROUTES TODO LISTE

@app.route('/todo')
def todo_liste():
	state="Liste"
	liste_todo = listeTodo()
	
	return render_template("todo.html", state=state, liste_items=liste_todo)


@app.route('/add_item', methods=['POST'])
	def add_item():
		it_state='do'
		it_name = request.form["name"]

		# requete add item
		connection=sqlite3.connect('todo.db')
		cursor=connection.cursor()
		it_id = cursor.lastrowid
		cursor.execute('INSERT INTO todo_items (id,name,state) VALUES (?,?,?)', (it_id, it_name, it_state))
		con.commit()
		connection.close()
		
		# redirect vers la liste
		redirect('/liste_item')

@app.route('/modif_item/<int:it_id>')
	def modify_item(it_id):
		# on recoi en POST : type, name ou state
		typeMaj =  request.form["type"]
		connection=sqlite3.connect('todo.db')
		cursor=connection.cursor()
		
		if typeMaj == 'name':
			it_name =  request.form["name"]
			# requete maj nom
			cursor.execute('UPDATE todo_items SET name = ? WHERE id = ?', (it_name, it_id))
		elif typeMaj == 'state':
			it_state =  request.form["state"]
			# requete maj state
			cursor.execute('UPDATE todo_items SET state = ? WHERE id = ?', (it_state, it_id))
		
		# redirect vers la liste
		redirect('/liste_item')



@app.route('/del_item')
	def del_item(it_id):
		it_id =  request.form["id"]
		# requete delete item
		connection=sqlite3.connect('todo.db')
		cursor=connection.cursor()
		cursor.execute('DELETE FROM todo_items WHERE id=?', (it_id))
		connection.close()
		# redirect vers la liste
		redirect('/liste_item')




# Routes check local network
@app.route('/check_network')
	def check_network():
		return render_template("network.html", liste_network=parc_machine)

'''
@app.route('/add_item', methods=['POST'])
def add_item():
	id = (int)(request.form['it_id'])
	name = str(request.form['it_name'])
	state = "do"
	# request BDD

	# return liste maj
	return render_template("home.html", state=state)


@app.route('/modif_item', methods=['POST'])
def modif_item():
	# if request.form['type'] == 'state'
	# requete maj state item
	#else
	# req maj nom
	
	it_id = (int)(request.form['id'])
	it_name = request.form['name']
	# request BDD

	# return liste maj
	cursor.execute("""UPDATE todo_items SET name = ? WHERE id = ?""", (it_name, it_id))
'''

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
