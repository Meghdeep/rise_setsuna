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
	response = jsonify( json.dumps("[" + ",".join(f.readlines()) + "]") )
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response
	return "[" + ",".join(f.readlines()) + "]"

@app.route('/accounts')
def accounts():
	f = open("state_data.json","r")
	return "[" + ",".join(f.readlines()) + "]" 


def interest_rate_parity_calculation(currency_pair, n):
	rfr = {"USD":0.425, "INR":6.5219, "GBP":0.20, "EUR":0.05}
	rates = {"USDINR":66.71, "USDGBP":0.77, "USDEUR":0.89, "INRUSD":0.015, "GBPUSD":1.30, "EURUSD":1.12, "INREUR":0.013, "EURINR":74.89, "INRGBP":0.012, "GBPINR":86.49, "GBPEUR":1.15, "EURGBP":0.87}
	base = currency_pair[:3]
	quotation = currency_pair[3:]
	r_value = rates[currency_pair] * ( 1 + rfr[quotation] ) / ( 1 + rfr[base] ) * int(n) / 365
	return json.dumps({"value":r_value})


@app.route('/default_interest_rate_parity')
def default_interest_rate_parity():

	currency_pair = request.form['currency_pair']
	quotation_rate = request.form['quotation_rate']
	n = request.form['n']
	obj = {
	"1 week":   interest_rate_parity_calculation(currency_pair, 7),
	"2 weeks":  interest_rate_parity_calculation(currency_pair, 14),
	"1 month":  interest_rate_parity_calculation(currency_pair, 30),
	"2 months": interest_rate_parity_calculation(currency_pair, 60),
	"3 months": interest_rate_parity_calculation(currency_pair, 90),
	"6 months": interest_rate_parity_calculation(currency_pair, 180),
	"1 year":   interest_rate_parity_calculation(currency_pair, 365)
	}
	return json.dumps(obj)

@app.route('/custom_interest_rate_parity')
def custom_interest_rate_parity():
	currency_pair = request.form['currency_pair']
	quotation_rate = request.form['quotation_rate']
	n = request.form['n']
	interest_rate_parity_calculation(currency_pair, n)

@app.route('/rates')
def rates():
	return """{\"base\":\"GBP\",\"date\":\"2016-09-24\",\"rates\":{\"INR\":86.436,\"USD\":1.2974,\"EUR\":1.1569}}"""

@app.route('/futures_price_from_interest_rate_parity')
def futures_price_from_interest_rate_parity():
	return open("futures_quotations.json", "r").readlines().strip("\n")

