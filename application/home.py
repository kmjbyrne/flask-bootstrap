
from flask import Flask, Blueprint, current_app, render_template, jsonify

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/', methods=['GET'])
def welcome():
	# current_app.logger.info('Resource requested: %s', ('welcome'))
	salutation = 'Thank for using flask-fundamentum!'
	return render_template('content.html', msg=salutation)

@home.route('/print/<input>', methods=['GET'])
def print_url_param(input=None):
	return jsonify(resp=input)


