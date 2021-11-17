from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks, food):
        
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food = food

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def add_food(self, food):
        self.food.append(food)

    def remove_food(self, food):
        self.food.remove(food)

    def increase_till(self, amount):
        self.till += amount

    def drink_count(self):
        return len(self.drinks)

    def food_count(self):
        return len(self.food)
    

    def serve_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness < 12:
            self.increase_till(drink.price)
            self.remove_drink(drink)
            customer.buy_drink(drink)

        else: 
            return "no sale"

    def serve_food(self, customer, food):
        self.increase_till(food.price)
        self.remove_food(food)
        customer.buy_food(food)
