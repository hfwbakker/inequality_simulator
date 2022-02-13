class Trader:
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        #trader_list.append(name)

trader_list = []

piet = Trader("Piet", 1000)
klaas = Trader("Klaas", 2000)
joris = Trader("Joris", 3000)
henri = Trader("Henri", 4000)
deja = Trader("Deja", 5000)

trader_list.append(piet)
trader_list.append(klaas)
trader_list.append(joris)
trader_list.append(henri)
trader_list.append(deja)

print(trader_list[1].name)

def make_trade(trader1, trader2):
	print(f"{trader1.name} trades with {trader2.name}")
