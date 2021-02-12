class MoneyTracker:
	CURRENCY = "$"  # label for formatting currency

	COIN_VALUES = {
		"quarters": 0.25,
		"dimes": 0.10,
		"nickles": 0.05,
		"pennies": 0.01
	}

	def __init__(self):
		self.profit = 0
		self.money_received = 0

	def report(self):
		"""Prints the current profit.  I added the :.2f formatting"""
		print(f"Money: {self.CURRENCY}{self.profit:.2f}")

	def process_coins(self):
		"""Returns the total calculated from coins inserted."""
		print("Please insert coins.")
		for coin in self.COIN_VALUES:
			try:
				number_of_coins = int(input(f"How many {coin}?: "))
			except ValueError:
				number_of_coins = 0
			self.money_received += number_of_coins * self.COIN_VALUES[coin]
		return self.money_received

	def make_payment(self, cost):
		"""Returns True when payment is accepted, or False if insufficient."""
		self.process_coins()
		if self.money_received >= cost:
			change = round(self.money_received - cost, 2)
			print(f"Here is {self.CURRENCY}{change:.2f} in change.")
			self.profit += cost
			self.money_received = 0
			return True
		else:
			print("Sorry that's not enough money. Money refunded.")
			self.money_received = 0
			return False
