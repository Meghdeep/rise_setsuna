import json
import utils
import twilio
import random
import requests
from flask import Flask, request, jsonify
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
#@crossdomain(origin='*')
def futures_data():
	f = open("futures_data.json","r")
	response = jsonify( json.loads("[" + ",".join(f.readlines()) + "]") )
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response
	return "[" + ",".join(f.readlines()) + "]"

@app.route('/accounts')
def accounts():
	f = open("state_data.json","r")
	return "[" + ",".join(f.readlines()) + "]" 


def interest_rate_parity_calculation(currency_pair, quotation_rate, n):
	rfr = {"USD":0.425, "INR":6.5219, "GBR":0.20, "EUR":0.05}
	base = currency_pair[:3]
	quotation = currency_pair[3:]
	r_value = quotation_rate * ( 1 + rfr[quotation] ) / ( 1 + rfr[base] ) * int(n) / 365
	return json.dumps({"value":r_value})


@app.route('/default_interest_rate_parity')
def default_interest_rate_parity():

	currency_pair = request.form['currency_pair']
	quotation_rate = request.form['quotation_rate']
	n = request.form['n']
	obj = {
	"1 week":   interest_rate_parity_calculation(currency_pair, quotation_rate, 7),
	"2 weeks":  interest_rate_parity_calculation(currency_pair, quotation_rate, 14),
	"1 month":  interest_rate_parity_calculation(currency_pair, quotation_rate, 30),
	"2 months": interest_rate_parity_calculation(currency_pair, quotation_rate, 60),
	"3 months": interest_rate_parity_calculation(currency_pair, quotation_rate, 90),
	"6 months": interest_rate_parity_calculation(currency_pair, quotation_rate, 180),
	"1 year":   interest_rate_parity_calculation(currency_pair, quotation_rate, 365)
	}
	return json.dumps(obj)

@app.route('/custom_interest_rate_parity')
def custom_interest_rate_parity():
	currency_pair = request.form['currency_pair']
	quotation_rate = request.form['quotation_rate']
	n = request.form['n']
	interest_rate_parity_calculation(currency_pair, quotation_rate, n)

@app.route('/rates')
def rates():
	return """{\"base\":\"GBP\",\"date\":\"2016-09-24\",\"rates\":{\"INR\":86.436,\"USD\":1.2974,\"EUR\":1.1569}}"""

