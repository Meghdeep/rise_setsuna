import json

rates = {"USDINR":66.71, "USDGBP":0.77, "USDEUR":0.89, "INRUSD":0.015, "GBPUSD":1.30, "EURUSD":1.12, "INREUR":0.013, "EURINR":74.89, "INRGBP":0.012, "GBPINR":86.49, "GBPEUR":1.15, "EURGBP":0.87}
rfr = {"USD":0.425, "INR":6.5219, "GBP":0.20, "EUR":0.05}

def generate( rate, n ):
	base = rate[:3]
	quotation = rate[3:]
	r_value = rates[rate] * ( 1 + rfr[quotation] ) / ( 1 + rfr[base] ) * int(n) / 365 + rates[rate]
	r_value = round( r_value, 6 )
	return json.dumps({"quotation":rate, "value":r_value})

file = open("futures_quotations.json", "w")
load = []

for rate in rates:
	obj = {}
	obj["quotation"]                                = rate
	obj["quotation_value"]                          = rates[rate]
	obj["interest_rate_parity_values"]              = {}		
	obj["interest_rate_parity_values"]["1_week"]    = generate(rate, 7)
	obj["interest_rate_parity_values"]["2_weeks"]   = generate(rate, 14)
	obj["interest_rate_parity_values"]["1_month"]   = generate(rate, 30)
	obj["interest_rate_parity_values"]["2_months"]  = generate(rate, 60)
	obj["interest_rate_parity_values"]["3_months"]  = generate(rate, 90)
	obj["interest_rate_parity_values"]["6_months"]  = generate(rate, 180)
	obj["interest_rate_parity_values"]["1_year"]    = generate(rate, 365)
	load.append(obj)

file.write( "%s"%json.dumps( load ) )