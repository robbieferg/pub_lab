from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks):
        
        self.name = name
        self.till = till
        self.drinks = drinks


    def increase_till(self, amount):
        self.till += amount

    def serve(self, customer, drink):
        self.till += drink.price 
        self.drinks.remove(drink)
        customer.buy_drink(drink)