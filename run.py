#! /usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.debug = True

@app.route("/")
def cafes():
	return render_template('cafes.jade')

@app.route("/order-pickup")
def orderpickup():
	return render_template('options.jade')

@app.route("/menu")
def menu():
	return render_template('menu.jade')

@app.route("/whereto")
def whereto():
	return render_template('whereto.jade')

@app.route("/accepted")
def accepted():
	return render_template('accepted.jade')

@app.route("/deliverto")
def deliverto():
	return render_template('deliverto.jade')

@app.route("/summary")
def summary():
	return render_template('summary.jade')

@app.route("/profile")
def profile():
	return render_template('profile.jade')

@app.route("/thankyou")
def thankyou():
	return render_template('thankyou.jade')
	
if __name__ == '__main__':
	app.run()
