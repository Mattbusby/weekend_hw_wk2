import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bill", 10)
        self.guest_2 = Guest("Joe", 5)
        self.guest_3 = Guest("Sam", 0)
        # guests = [self.guest_1, self.guest_2, self.guest_3]

    def test_guest_has_name(self):
        self.assertEqual("Bill", self.guest_1.name)

    