import requests
import json
import random

rates = {"USDINR":66.71, "USDGBP":0.77, "USDEUR":0.89, "INRUSD":0.015, "GBPUSD":1.30, "EURUSD":1.12, "INREUR":0.013, "EURINR":74.89, "INRGBP":0.012, "GBPINR":86.49, "GBPEUR":1.15, "EURGBP":0.87}

obj = {}

for rate in rates:
	obj[rate] = {}
	obj[rate]["currency_pair"]                                = rate
	obj[rate]["currency_pair_value"]                          = rates[rate]
	curr = rates[rate]
	base1 = rate[:3]
	base2 = rate[3:]

	obj[rate]["1_week"]    = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["2_weeks"]   = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["1_month"]   = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["2_months"]  = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["3_months"]  = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["6_months"]  = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000
	obj[rate]["1_year"]    = random.randint( curr * 1000 - 2000, curr * 1000 + 2000 ) / 1000

f = open("forex.json", "w")
f.write("%s"%json.dumps(obj))

