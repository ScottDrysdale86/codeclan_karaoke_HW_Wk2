import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.karaoke_bar import KaraokeBar


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Scott", 50, "Hello")
        self.guest2 = Guest("Becca", 20, "Help")
        self.guest3 = Guest("Jacob", 10, "Baby Shark")
        self.room1 = Room("Room1", 3)
        self.song1 = Song("Hello", "Adele")
        self.karaoke = KaraokeBar("Super Cube", 200)

    def test_guest_has_name(self):
        self.assertEqual("Scott", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Hello", self.guest1.fav_song)

    def test_favourite_song(self):
        songbook = self.karaoke.add_to_song_book(self.song1)
        add = self.room1.add_to_playlist(self.karaoke.song_book, self.song1)
        result = self.room1.check_favourite_song_in_playlist(self.guest1)
        self.assertEqual("Woo Hoo, I love this song", result)
