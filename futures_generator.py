import json
import random
pairs = ["USDINR", "USDGBP", "USDEUR", "INRUSD", "GBPUSD", "EURUSD", "INREUR", "EURINR", "INRGBP", "GBPINR", "GBPEUR", "EURGBP"]
rates = {"USDINR":66.71, "USDGBP":0.77, "USDEUR":0.89, "INRUSD":0.015, "GBPUSD":1.30, "EURUSD":1.12, "INREUR":0.013, "EURINR":74.89, "INRGBP":0.012, "GBPINR":86.49, "GBPEUR":1.15, "EURGBP":0.87}
for rate in rates:
	rates[rate] = rates[rate] * 1000
dates = ["280916", "261016", "281116", "281216", "270117", "240217", "240317", "290417", "260517", "280617", "270717", "290817"]
final = []

for pair in pairs:
	for date in dates:
		obj = {}
		obj["ontracts"] = pair + " " + date
		obj["best_bid"] = {}
		obj["best_ask"] = {}
		obj["best_bid"]["quantity"] = random.randint(1, 250)
		obj["best_bid"]["price"]    = random.randint(rates[pair], rates[pair] + 4) / 1000
		obj["best_ask"]["quantity"] = random.randint(1, 250)
		obj["best_ask"]["price"]    = random.randint(rates[pair] + 1, rates[pair] + 4) / 1000
		obj["spread"]               = round( obj["best_ask"]["price"] - obj["best_bid"]["price"], 4 )
		obj["change"]               = -(random.randint(1, 9)) / 100
		obj["change_percent"]       = -(random.randint(4, 18)) / 100
		obj["ltp"]                  = random.randint(obj["best_bid"]["price"] * 1000, obj["best_bid"]["price"] * 1000 + 1000) / 1000
		obj["oi"]                   = random.randint(2000, 50000)
		obj["volume(contracts)"]    = random.randint(30, 2000)
		obj["turnover(crores)"]     = random.randint(1, 2000)
		obj["number of trades"]     = random.randint(1, 2000)
		final.append(obj)

f = open("futures_data.json", "w")
for item in final:
	f.write("%s\n"%json.dumps(item))
f.close()