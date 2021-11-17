import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00,["beer", "wine", "vodka"])

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_till_value(self):
        self.assertEqual(100.00,self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(["beer", "wine", "vodka"],self.pub.drinks)


    #@unittest.skip
    def test_increase_till(self):
        # Arrange - set up everything - we need a pub, (with name and value in our case)
        # Act - if anything need to be done (like increase till)
        self.pub.increase_till(2.50)
        # Assert
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

    