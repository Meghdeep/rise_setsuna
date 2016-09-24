def customers():
	return """[
    {
        "id": "8384692676375759",
        "title": "Mrs",
        "firstName": "Helen",
        "lastName": "Jones",
        "middleNames": "",
        "mobileNo": "07599458556",
        "nationalityCode": "UK",
        "dateOfBirth": "01-01-1983 00:00:00 UTC",
        "address": {
            "number": "3",
            "buildingName": "",
            "street": "Kings Road",
            "town": "Knutsford",
            "postalCode": "WA166AD",
            "country": "UK"
        },
        "isNewToBank": false,
        "accountList": [
            {
                "id": "4051694345404902",
                "description": "Regular Savings Account",
                "nickName": "Helen's holiday savings",
                "customerId": "8384692676375758",
                "accountType": "SAVINGS_ACCOUNT",
                "sortCode": 402578,
                "accountNo": "****8122",
                "currentBalance": 4500
            },
            {
                "id": "8253594415636011",
                "description": "Premier Current Account",
                "nickName": "Helen's salary account",
                "customerId": "8384692676375759",
                "accountType": "CURRENT_ACCOUNT",
                "sortCode": 112233,
                "accountNo": "****1258",
                "card": {
                    "cardNumber": "************4567",
                    "displayName": "Helen Smith",
                    "maxSpend": 3000,
                    "currentBalance": 500,
                    "type": "DEBIT",
                    "customerId": "8384692676375759",
                    "expiryDate": "01-01-2018 00:00:00 UTC"
                },
                "currentBalance": 2500,
                "overdraftLimit": 1500
            },
            {
                "id": "1945340430755308",
                "description": "Barclaycard Platinum Credit Card Account",
                "nickName": "Helen's credit card",
                "customerId": "8384692676375759",
                "accountType": "CREDIT_CARD_ACCOUNT",
                "card": {
                    "cardNumber": "************9999",
                    "displayName": "Helen Smith",
                    "maxSpend": 7000,
                    "currentBalance": 1500,
                    "type": "CREDIT",
                    "customerId": "8384692676375759",
                    "expiryDate": "01-01-2019 00:00:00 UTC"
                }
            },
            {
                "id": "1945340430755315",
                "description": "Barclaycard Platinum Corporate Account",
                "nickName": "Business credit card",
                "customerId": "8384692676375759",
                "accountType": "CREDIT_CARD_ACCOUNT",
                "card": {
                    "cardNumber": "************8888",
                    "displayName": "Helen Smith",
                    "maxSpend": 17000,
                    "currentBalance": 2501,
                    "type": "CREDIT",
                    "customerId": "8384692676375759",
                    "expiryDate": "01-05-2017 00:00:00 UTC"
                }
            },
            {
                "id": "4051694345404912",
                "description": "Mortgage Fixed Rate 1.3% (September 2019)",
                "currentSVR": "1.8",
                "termMonths": 300,
                "nickName": "Mortgage",
                "customerId": "8384692676375759",
                "accountType": "MORTGAGE_FIXED",
                "sortCode": 402570,
                "accountNo": "****5678",
                "product details": {
                  "discountRate": "1.3",
                  "outstandingBalance": 75000,
                  "monthlyRepayments": 711,
                  "monthlyRateAfterDiscount": 728,
                  "remainingTermMonths": 150,
                  "remainingPaymentHolidaysMonths": 6,
                  "discountEndDate": "01-09-2019 00:00:00 UTC"
                }
            }
        ]
    }
]"""

def transactions():
	return """[
  {
      "id": "8573315966758950",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "28.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1500.00"
      },
      "created": "06-09-2015 08:00:00 UTC",
      "description": "Texaco petrol station",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Texaco"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": null,
              "value": null
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CARD"
  },
  {
      "id": "8573315966758949",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "30.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1528.00"
      },
      "created": "05-19-2016 21:00:00 UTC",
      "description": "Raspberry Pi 5 starter kit",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Amazon"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": "RECEIPT",
              "value": "https://amazon.com/invoices"
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CARD"
  },
  {
      "id": "8573315966758940",
      "amount": {
          "moneyIn": "50.00",
          "moneyOut": "00.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1558.00"
      },
      "created": "05-09-2016 12:30:00 UTC",
      "description": "Cheque 00012345",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Barclays"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": "RECEIPT",
              "value": "https://www.barclays.com/cloudit"
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CHEQUE"
  },
  {
      "id": "8421552562162948",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "22.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1508.00"
      },
      "created": "05-09-2016 08:20:00 UTC",
      "description": null,
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "British Rail"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CARD"
  },
  {
      "id": "8573315966758947",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "11.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1530.00"
      },
      "created": "04-09-2016 14:00:00 UTC",
      "description": "Fender Acoustic Guitar",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Starbucks"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": "RECEIPT",
              "value": "https://upload.wikimedia.org/wikipedia/common"
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CARD"
  },
  {
      "id": "8573315966758940",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "200.00"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1541.00"
      },
      "created": "01-10-2015 14:00:00 UTC",
      "description": "Internal Tranfer Acc ****8122",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Eagle Bank"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": "RECEIPT",
              "value": "https://upload.wikimedia.org/wikipedia/common"
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "TRANSFER"
  },
  {
      "id": "8573315966758940",
      "amount": {
          "moneyIn": "0.00",
          "moneyOut": "10.57"
      },
      "accountBalanceAfterTransaction": {
          "position": "CR",
          "amount": "1741.00"
      },
      "created": "02-09-2016 00:01:00 UTC",
      "description": "Account charges",
      "paymentDescriptor": {
          "id": "9701229312305196",
          "address": {
              "addressId": 1,
              "number": "5",
              "buildingName": "Altrincham Retail Park",
              "street": "George Richards Way",
              "town": "Altrincham",
              "postalCode": "WA14 5GR",
              "country": "UK"
          },
          "groupId": "4722",
          "logo": "",
          "name": "Eagle Bank"
      },
      "payee": null,
      "pingIt": null,
      "metadata": [
          {
              "key": "RECEIPT",
              "value": "https://upload.wikimedia.org/wikipedia/common"
          }
      ],
      "notes": null,
      "customerId": "8384692676375758",
      "paymentMethod": "CHARGES"
  }
  ]
"""