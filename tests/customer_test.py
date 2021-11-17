import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 17.50, 75, 7)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_wallet_value(self):
        self.assertEqual(17.50,self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(75, self.customer.age)

    def test_custumer_drunkeness(self):
        self.assertEqual(7, self.customer.drunkenness)

    
    def test_customer_can_buy_drink(self):
        drink_1 = Drink("vodka", 1.50, 4)
        self.customer.buy_drink(drink_1)
        self.assertEqual(16.00, self.customer.wallet)
        self.assertEqual(11, self.customer.drunkenness)

    def test_customer_can_buy_food(self):
        food_1 = Food("hot dog", 4.00, 3)
        self.customer.buy_food(food_1)
        self.assertEqual(13.50, self.customer.wallet)
        self.assertEqual(4, self.customer.drunkenness)

        

