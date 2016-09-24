import json
import random

bank_name = ["Goliath National Bank", "Gringotts", "Wayne Enterprises", "Tyrell Corp.", "Barclays", "Iron Bank of Braavos"]
total = []
for bank in bank_name:
	obj = {}
	obj["bank_name"] = bank
	obj["accounts"]  = []
	for account in range(0, 10):
		account_obj = {}
		account_obj["account_type"]  = "current account"
		account_obj["id"]            = account + 1
		account_obj["number"]        = random.randint(100000000000, 999999999999)
		account_obj["balance"]       = random.randint(10000, 100000)
		if account <= 4:
			account_obj["base currency"] = "EUR"
		elif account <= 6:
			account_obj["base currency"] = "GBP"
		elif account <= 8:
			account_obj["base currency"] = "INR"
		else:
			account_obj["base currency"] = "USD"

		obj["accounts"].append(account_obj)
	total.append(obj)

file = open("state_data.json", "w")
for item in total:
	file.write("%s\n"%json.dumps(item))