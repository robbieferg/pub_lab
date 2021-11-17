import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00,[])
        self.drink_1 = Drink("Coke", 2.50, 1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00,self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual([],self.pub.drinks)

    def test_pub_can_serve__old_enough(self):
        customer_1 = Customer("Mary", 5.60, 30, 3)
        self.pub.drinks.append(self.drink_1)
        self.pub.serve(customer_1, self.drink_1)
        self.assertEqual(102.50, self.pub.till)
        self.assertNotIn(self.drink_1,self.pub.drinks)

    def test_pub_can_serve__too_young(self):
        customer_2 = Customer("Tammy", 10.50, 15, 0)
        self.assertEqual("no sale", self.pub.serve(customer_2,self.drink_1))

    def test_pub_can_serve__too_young(self):
        customer_3 = Customer("Frank", 10.50, 35, 20)
        self.assertEqual("no sale", self.pub.serve(customer_3,self.drink_1))


    #@unittest.skip
    def test_increase_till(self):
        # Arrange - set up everything - we need a pub, (with name and value in our case)
        # Act - if anything need to be done (like increase till)
        self.pub.increase_till(2.50)
        # Assert
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

    