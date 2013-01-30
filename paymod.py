"""
Month | Current Total | Interest Amount | Principal | Payment | Balance Remaining 

Item:
	Base Price:		(Input)
	Down Payment:	Base Price * account.downPayRate
	Starting Price:	Base Price - Down Payment

Account:
	Rates: (Static)
		Down Payment Rate:		.10
		Monthly Interest Rate:  .01
		Monthly Payment Rate:  	.05
	Info: (Dynamic)



Down Payment = Price * .10
Starting Price = Price - Down Payment
Current Total = Starting price - Payment
Interest Amount = Starting price * .01
Payment = Principal + Interest Amount
Balance Remaining = Current total - Payment
Principal = Starting price * .05

"""
class Item(object):
	"""Item information"""
	
	def __init__(self):
		self._basePrice = None
		self._downPayment = None
		self._interestRate = None

	def __str__(self):
		return 'The price is: ' + str(self._price)

	def setPrice(self, price, downPay, ):
		self._basePrice = price
		self._downPayment = price * .10

class Account(object):
	"""Account information"""

	def __init__(self):
		self._totalBalance = None

class Rates(object):
	"""Price rate information"""

	def __init__(self):
		self._downPay = .10
		self._monthlyIntRate = .01 # Annual rate per month
		self._