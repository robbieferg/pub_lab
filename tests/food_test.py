import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food_1 = Food("burger", 3.10, 4)

    def test_food_has_name(self):
            self.assertEqual("burger", self.food_1.name)

    def test_food_has_price(self):
            self.assertEqual(3.10, self.food_1.price)

    def test_food_has_rejuvenation_level(self):
            self.assertEqual(4, self.food_1.rejuvenation_level)