import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 17.50)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.customer.name)

    def test_customer_wallet_value(self):
        self.assertEqual(17.50,self.customer.wallet)
    
    def test_customer_can_buy_drink(self):
        drink_1 = Drink("water", 1.50)
#       pub = Pub("Clansman", 300.50, [drink_1])
        self.customer.buy_drink(drink_1)
        self.assertEqual(16.00, self.customer.wallet)
#       self.assertEqual(302.00, self.pub.till)
#       self.assertNotIn(drink_1,self.pub.drinks)
