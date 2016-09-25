import json
import random

rates = {"USDINR":66.71, "USDGBP":0.77, "USDEUR":0.89, "INRUSD":0.015, "GBPUSD":1.30, "EURUSD":1.12, "INREUR":0.013, "EURINR":74.89, "INRGBP":0.012, "GBPINR":86.49, "GBPEUR":1.15, "EURGBP":0.87}
rv = {}

for rate in rates:
	rv["base_value"] = rates[rate]
	rv[rate] = {}
	num_val = 0
	for num in range(1,33):
		num_val = num_val + 0.4
		obj = {}
		obj["strike_price"]  = rates[rate] * num_val + num_val
		obj["calls"] = {}
		obj["puts"]  = {}

		obj["calls"]["bid_quantity"] = random.randint(1, 2000)
		obj["calls"]["bid_price"]    = random.randint( 25, 30000 ) / 10000
		obj["calls"]["ask_quantity"] = random.randint(1, 2000)
		obj["calls"]["ask_price"]    = random.randint( 25, 30000 ) / 10000
		obj["calls"]["LTP"]          = random.randint( 25, 30000 ) / 10000
		obj["calls"]["IV"]           = random.randint(5, 6000) / 100
		obj["calls"]["volume"]       = random.randint(400, 30000)
		obj["calls"]["change_in_OI"] = random.randint(300, 25000) * (-1)**random.randint(1,5)
		obj["calls"]["OI"]           = random.randint(20, 50000)

		obj["puts"]["bid_quantity"] = random.randint(1, 2000)
		obj["puts"]["bid_price"]    = random.randint( 25, 30000 ) / 10000
		obj["puts"]["ask_quantity"] = random.randint(1, 2000)
		obj["puts"]["ask_price"]    = random.randint( 25, 30000 ) / 10000
		obj["puts"]["LTP"]          = random.randint( 25, 30000 ) / 10000
		obj["puts"]["IV"]           = random.randint(5, 6000) / 100
		obj["puts"]["volume"]       = random.randint(400, 30000)
		obj["puts"]["change_in_OI"] = random.randint(300, 25000) * (-1)**random.randint(1,5)
		obj["puts"]["OI"]           = random.randint(20, 50000)
		name = "strike_price_%d"%num
		rv[rate][name] = obj

f = open("options.json", "w")
f.write("%s"%json.dumps(rv))
	