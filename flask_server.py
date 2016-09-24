import json
import utils
import twilio
import random
import requests
from flask import Flask, request
from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException
from twilio.rest import TwilioRestClient

app = Flask(__name__)
auth = {}

@app.route('/customers')
def customers():
	return utils.customers()

@app.route('/transactions')
def transactions():
	return utils.transactions()

@app.route('/start_auth', methods=['POST'])
def start_auth():
	number = request.form['number']
	password = random.randint(0,99999)
	account_sid = "AC3d92d3e1fd8e9b9337f248a4c7ec3baa"
	auth_token  = "3c01fe6ced4686a02623ee36ef83772f"
	client      = TwilioRestClient(account_sid, auth_token)
	message     = client.messages.create(to=number, from_="+16787016646", body=password)
	#file = open("pass.txt", "a")
	#file.write("%s:%s\n"%(number,str(password)))
	#file.close()
	global auth
	auth[number] = password
	return json.dumps({"password":password})

@app.route('/end_auth', methods=['POST'])
def end_auth():
	number   = request.form['number']
	password = request.form['password']
	#file = open("pass.txt", "r").realines()
	#for line in file:
	#	if line.strip("\n").split(":")[0] == password:
	global auth
	if auth[number] == int(password):
		account_sid = "AC3d92d3e1fd8e9b9337f248a4c7ec3baa"
		auth_token  = "3c01fe6ced4686a02623ee36ef83772f"
		client      = TwilioRestClient(account_sid, auth_token)
		message     = client.messages.create(to=number, from_="+16787016646", body="Succesfully Verified !")
		return json.dumps({"status":True})
	else:
		return json.dumps({"status":False})

@app.route('/futures_data')
def futures_data():
	f = open("futures_data.json","r")
	return "[" + ",".join(f.readlines()) + "]"

@app.route('/accounts')
def accounts():
	f = open("state_data.json","r")
	return "[" + ",".join(f.readlines()) + "]" 

@app.route('/rfr')
def rfr():
	f = open("rfr.json","r")
	return "[" + ",".join(f.readlines()) + "]"