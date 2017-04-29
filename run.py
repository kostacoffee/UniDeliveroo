#! /usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.debug = True

@app.route("/")
def hello():
	return render_template('hello.jade')

@app.route("/cafes")
def cafes():
	return render_template('hello.jade')

@app.route("/order-pickup/<int:cafeid>")
def orderpickup(cafeid):
	return render_template('options.jade')

@app.route("/menu/<int:cafeid>")
def menu(cafeid):
	return render_template('menu.jade')

@app.route("/whereto")
def whereto():
	return render_template('hello.jade')

@app.route("/accepted")
def accepted():
	return render_template('hello.jade')

@app.route("/deliverto")
def deliverto():
	return render_template('hello.jade')

@app.route("/orderlist/<int:cafeid>")
def orderlist(cafeid):
	return render_template('hello.jade')

@app.route("/summary")
def summary():
	return render_template('hello.jade')

if __name__ == '__main__':
	app.run()
