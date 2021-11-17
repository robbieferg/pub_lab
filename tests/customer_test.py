import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack", 17.50)

    def test_customer_has_name(self):
        self.assertEqual("Jack", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00,self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(["beer", "wine", "vodka"],self.pub.drinks)