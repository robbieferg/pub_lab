import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00,[], [])
        self.drink_1 = Drink("Coke", 2.50, 1)
        self.drink_2 = Drink("cider", 3.80, 4)
        self.food_1 = Food("sandwich", 1.75, 2)
        self.food_2 = Food("pie", 2.10, 4)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00,self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual([],self.pub.drinks)

    def test_pub_can_serve_drink__old_enough(self):
        customer_1 = Customer("Mary", 5.60, 30, 3)
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.serve_drink(customer_1, self.drink_1)
        self.assertEqual(102.50, self.pub.till)
        self.assertNotIn(self.drink_1,self.pub.drinks)

    def test_pub_can_serve_drink__too_young(self):
        customer_2 = Customer("Tammy", 10.50, 15, 0)
        customer_3 = Customer("Frank", 10.50, 35, 20)
        self.assertEqual("no sale", self.pub.serve_drink(customer_2,self.drink_1))
        self.assertEqual("no sale", self.pub.serve_drink(customer_3,self.drink_1))

    def test_pub_can_serve_food(self):
        customer_4 = Customer("Dennis", 199.99, 86, 2)
        self.pub.add_food(self.food_1)
        self.pub.add_food(self.food_2)
        self.pub.serve_food(customer_4, self.food_1)
        self.assertEqual(101.75, self.pub.till)
        self.assertNotIn(self.drink_1, self.pub.food)

    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

    