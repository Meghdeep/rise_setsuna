import tornado.ioloop
import tornado.web
import json
import requests

cache = """{
  "current account example":
    {
        "id": "8253594415636011",
        "description": "Premier Current Account",
        "nickName": "John salary account",
        "customerId": "8384692676375758",
        "accountType": "CURRENT_ACCOUNT",
        "sortCode": 112233,
        "accountNo": "****1258",
        "card": {
            "cardNumber": "************4567",
            "displayName": "John Smith",
            "maxSpend": 3000,
            "currentBalance": 500,
            "type": "DEBIT",
            "customerId": "8384692676375758",
            "expiryDate": "01-01-2018 00:00:00 UTC"
        },
        "currentBalance": 1500,
        "overdraftLimit": 1500
    },
  "savings account example":
    {
        "id": "4051694345404902",
        "description": "Regular Savings Account",
        "nickName": "John holiday savings",
        "customerId": "8384692676375758",
        "accountType": "SAVINGS_ACCOUNT",
        "sortCode": 402578,
        "accountNo": "****8122",
        "currentBalance": 5000
    },
  "credit card account":
    {
        "id": "1945340430755308",
        "description": "Barclaycard Platinum Credit Card Account",
        "nickName": "John credit card",
        "customerId": "8384692676375758",
        "accountType": "CREDIT_CARD_ACCOUNT",
        "card": {
            "cardNumber": "************9999",
            "displayName": "John Smith",
            "maxSpend": 7000,
            "currentBalance": 1500,
            "type": "CREDIT",
            "customerId": "8384692676375758",
            "expiryDate": "01-01-2019 00:00:00 UTC"
        }
    }
}"""
cache_obj = json.loads(cache)

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers','Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')
        #self.write( requests.get( "https://api108567live.gateway.akana.com:443/accounts/" + str( self.get_argument("account_number") ) ).content )
        self.write( cache_obj )

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
