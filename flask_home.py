#! /usr/bin/python

from subprocess import call
from flask import Flask
from flask import render_template
from scan_folder import make_tree

app = Flask(__name__, static_url_path = "", static_folder = "static")

liste = make_tree("/home/pi/Documents/python/flask_alarm/static/photos")

@app.route('/')
def index():
	#return "Hello Flassk !"
	state="home"
	return render_template("home.html", state=state, liste=liste)

@app.route('/alarm_start')
def alarm_start():
	# nohup python script.py &
	call(["python", "/home/pi/Documents/python/flask_alarm/daemon_alarm_light.py","start", "&"])
	
	photos="Aucune photos"
	state="ON"
	return render_template("home.html", state=state, liste=photos)


@app.route('/alarm_stop')
def alarm_stop():
	call(["/home/pi/Documents/python/flask_alarm/daemon_alarm_light.py","stop"])
	
	photos="Aucune photos"
	state="OFF"
	return render_template("home.html", state=state, liste=photos)


@app.route('/photos')
def maj_photos():
	state="Liste"
	#t2 = make_tree("/home/pi/Documents/PIRemail/photos")
	liste_maj = make_tree("/home/pi/Documents/flask_alarm/static/photos")
	return render_template("liste_folder.html", state=state, liste=liste_maj)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)
