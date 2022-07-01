import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Scott", 50, "Hello")
        self.guest2 = Guest("Becca", 20, "Help")
        self.guest3 = Guest("Jacob", 10, "Baby Shark")

    def test_guest_has_name(self):
        self.assertEqual("Scott", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Hello", self.guest1.fav_song)

    
