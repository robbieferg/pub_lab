import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("beer", 3.75)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.75, self.drink.price)

