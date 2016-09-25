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
	return json.dumps([{"interest_rate_parity_values": {"2_weeks": "{\"value\": 1.178301, \"quotation\": \"EURUSD\"}", "6_months": "{\"value\": 1.869589, \"quotation\": \"EURUSD\"}", "2_months": "{\"value\": 1.369863, \"quotation\": \"EURUSD\"}", "1_year": "{\"value\": 2.64, \"quotation\": \"EURUSD\"}", "1_week": "{\"value\": 1.149151, \"quotation\": \"EURUSD\"}", "3_months": "{\"value\": 1.494795, \"quotation\": \"EURUSD\"}", "1_month": "{\"value\": 1.244932, \"quotation\": \"EURUSD\"}"}, "quotation": "EURUSD", "quotation_value": 1.12}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.012073, \"quotation\": \"INRGBP\"}", "6_months": "{\"value\": 0.012944, \"quotation\": \"INRGBP\"}", "2_months": "{\"value\": 0.012315, \"quotation\": \"INRGBP\"}", "1_year": "{\"value\": 0.013914, \"quotation\": \"INRGBP\"}", "1_week": "{\"value\": 0.012037, \"quotation\": \"INRGBP\"}", "3_months": "{\"value\": 0.012472, \"quotation\": \"INRGBP\"}", "1_month": "{\"value\": 0.012157, \"quotation\": \"INRGBP\"}"}, "quotation": "INRGBP", "quotation_value": 0.012}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 95.46772, \"quotation\": \"EURINR\"}", "6_months": "{\"value\": 339.460689, \"quotation\": \"EURINR\"}", "2_months": "{\"value\": 163.08023, \"quotation\": \"EURINR\"}", "1_year": "{\"value\": 611.380563, \"quotation\": \"EURINR\"}", "1_week": "{\"value\": 85.17886, \"quotation\": \"EURINR\"}", "3_months": "{\"value\": 207.175344, \"quotation\": \"EURINR\"}", "1_month": "{\"value\": 118.985115, \"quotation\": \"EURINR\"}"}, "quotation": "EURINR", "quotation_value": 74.89}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 1.359212, \"quotation\": \"GBPUSD\"}", "6_months": "{\"value\": 2.061301, \"quotation\": \"GBPUSD\"}", "2_months": "{\"value\": 1.553767, \"quotation\": \"GBPUSD\"}", "1_year": "{\"value\": 2.84375, \"quotation\": \"GBPUSD\"}", "1_week": "{\"value\": 1.329606, \"quotation\": \"GBPUSD\"}", "3_months": "{\"value\": 1.680651, \"quotation\": \"GBPUSD\"}", "1_month": "{\"value\": 1.426884, \"quotation\": \"GBPUSD\"}"}, "quotation": "GBPUSD", "quotation_value": 1.3}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.794871, \"quotation\": \"USDGBP\"}", "6_months": "{\"value\": 1.089769, \"quotation\": \"USDGBP\"}", "2_months": "{\"value\": 0.87659, \"quotation\": \"USDGBP\"}", "1_year": "{\"value\": 1.418421, \"quotation\": \"USDGBP\"}", "1_week": "{\"value\": 0.782435, \"quotation\": \"USDGBP\"}", "3_months": "{\"value\": 0.929885, \"quotation\": \"USDGBP\"}", "1_month": "{\"value\": 0.823295, \"quotation\": \"USDGBP\"}"}, "quotation": "USDGBP", "quotation_value": 0.77}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.01307, \"quotation\": \"INREUR\"}", "6_months": "{\"value\": 0.013895, \"quotation\": \"INREUR\"}", "2_months": "{\"value\": 0.013298, \"quotation\": \"INREUR\"}", "1_year": "{\"value\": 0.014815, \"quotation\": \"INREUR\"}", "1_week": "{\"value\": 0.013035, \"quotation\": \"INREUR\"}", "3_months": "{\"value\": 0.013447, \"quotation\": \"INREUR\"}", "1_month": "{\"value\": 0.013149, \"quotation\": \"INREUR\"}"}, "quotation": "INREUR", "quotation_value": 0.013}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 1.188596, \"quotation\": \"GBPEUR\"}", "6_months": "{\"value\": 1.646233, \"quotation\": \"GBPEUR\"}", "2_months": "{\"value\": 1.315411, \"quotation\": \"GBPEUR\"}", "1_year": "{\"value\": 2.15625, \"quotation\": \"GBPEUR\"}", "1_week": "{\"value\": 1.169298, \"quotation\": \"GBPEUR\"}", "3_months": "{\"value\": 1.398116, \"quotation\": \"GBPEUR\"}", "1_month": "{\"value\": 1.232705, \"quotation\": \"GBPEUR\"}"}, "quotation": "GBPEUR", "quotation_value": 1.15}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 107.284447, \"quotation\": \"GBPINR\"}", "6_months": "{\"value\": 353.847177, \"quotation\": \"GBPINR\"}", "2_months": "{\"value\": 175.609059, \"quotation\": \"GBPINR\"}", "1_year": "{\"value\": 628.630943, \"quotation\": \"GBPINR\"}", "1_week": "{\"value\": 96.887224, \"quotation\": \"GBPINR\"}", "3_months": "{\"value\": 220.168589, \"quotation\": \"GBPINR\"}", "1_month": "{\"value\": 131.04953, \"quotation\": \"GBPINR\"}"}, "quotation": "GBPINR", "quotation_value": 86.49}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.015109, \"quotation\": \"INRUSD\"}", "6_months": "{\"value\": 0.016401, \"quotation\": \"INRUSD\"}", "2_months": "{\"value\": 0.015467, \"quotation\": \"INRUSD\"}", "1_year": "{\"value\": 0.017842, \"quotation\": \"INRUSD\"}", "1_week": "{\"value\": 0.015054, \"quotation\": \"INRUSD\"}", "3_months": "{\"value\": 0.015701, \"quotation\": \"INRUSD\"}", "1_month": "{\"value\": 0.015234, \"quotation\": \"INRUSD\"}"}, "quotation": "INRUSD", "quotation_value": 0.015}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 80.216375, \"quotation\": \"USDINR\"}", "6_months": "{\"value\": 240.363393, \"quotation\": \"USDINR\"}", "2_months": "{\"value\": 124.594464, \"quotation\": \"USDINR\"}", "1_year": "{\"value\": 418.840491, \"quotation\": \"USDINR\"}", "1_week": "{\"value\": 73.463187, \"quotation\": \"USDINR\"}", "3_months": "{\"value\": 153.536696, \"quotation\": \"USDINR\"}", "1_month": "{\"value\": 95.652232, \"quotation\": \"USDINR\"}"}, "quotation": "USDINR", "quotation_value": 66.71}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.908137, \"quotation\": \"EURGBP\"}", "6_months": "{\"value\": 1.360333, \"quotation\": \"EURGBP\"}", "2_months": "{\"value\": 1.033444, \"quotation\": \"EURGBP\"}", "1_year": "{\"value\": 1.864286, \"quotation\": \"EURGBP\"}", "1_week": "{\"value\": 0.889068, \"quotation\": \"EURGBP\"}", "3_months": "{\"value\": 1.115166, \"quotation\": \"EURGBP\"}", "1_month": "{\"value\": 0.951722, \"quotation\": \"EURGBP\"}"}, "quotation": "EURGBP", "quotation_value": 0.87}, {"interest_rate_parity_values": {"2_weeks": "{\"value\": 0.915154, \"quotation\": \"USDEUR\"}", "6_months": "{\"value\": 1.213403, \"quotation\": \"USDEUR\"}", "2_months": "{\"value\": 0.997801, \"quotation\": \"USDEUR\"}", "1_year": "{\"value\": 1.545789, \"quotation\": \"USDEUR\"}", "1_week": "{\"value\": 0.902577, \"quotation\": \"USDEUR\"}", "3_months": "{\"value\": 1.051702, \"quotation\": \"USDEUR\"}", "1_month": "{\"value\": 0.943901, \"quotation\": \"USDEUR\"}"}, "quotation": "USDEUR", "quotation_value": 0.89}])

