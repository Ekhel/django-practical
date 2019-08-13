from django.test import TestCase
from practical.calc import add

class CalcTest(TestCase):

    def tesd_add_numbers(self):
        self.assertEqual(add(3, 8), 11)
