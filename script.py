import random

class Trader:
	def __init__(self, name, funds):
		self.name = name
		self.funds = funds
		trader_list.append(self.name)

	def check_money(self):
		print(f"{self.name} has {self.funds} muney left")
	
	def gain(self, amount):
		#print(f"{self.name} earned {amount}")
		self.funds += amount	
		print(f"{self.name} funds are now {self.funds}")

	def lose(self, amount):
		#print(f"{self.name} lost {amount}")
		self.funds -= amount
		#print(f"{self.name}'s funds decreased to {self.funds}")



piet = Trader("Piet", 1000)
klaas = Trader("Klaas", 2000)
joris = Trader("Joris", 3000)
henri = Trader("Henri", 4000)
deja = Trader("Deja", 5000)


object_list = [piet, klaas, joris, henri, deja]


def make_trade(trader1, trader2):
	print(f"{trader1.name}'s current funds are {trader1.funds}. {trader2.name}'s funds are {trader2.funds}.")
	amount = random.randint(100, 1000)
	print(f"amount to be traded is {amount}.")
	trader1.lose(amount/2)
	print(f"{trader1.name} and {trader2.name} both invested {amount/2}")
	trader2.lose(amount/2)
	trader1_luck = random.randint(0,100)/100
	trader1_result = round(amount * trader1_luck)
	print(f"{trader1.name}'s return is {trader1_result}. {trader2.name}'s return is {amount - trader1_result}.")
	trader1.gain(trader1_result)
	trader2.gain(round(amount - trader1_result))



def random_trade(list):
	trader1_num = random.randint(0, len(list)-1)
	trader1 = list[trader1_num]
	print(trader1.name)
	
	trader2_num = trader1_num
	while trader2_num == trader1_num:
		trader2_num = random.randint(0,len(list)-1)
	trader2 = list[trader2_num]
	print(trader2.name)
	
	make_trade(trader1, trader2)	


def remove_trader(trader_name):
	trader_list.remove(trader_name)	

random_trade(object_list)




