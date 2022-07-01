import unittest
from classes.karaoke_bar import KaraokeBar
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke = KaraokeBar("Super Cube", 200)
        self.room1 = Room("Room1", 3)
        self.guest1 = Guest("Scott", 50, "Hello")
        self.guest2 = Guest("Becca", 20, "Help")
        self.guest3 = Guest("Jacob", 0, "Baby Shark")
        self.guest4 = Guest("Donna", 100, "Sunshine on Leith")
        self.song1 = Song("Hello", "Adele")
        self.song2 = Song("Help", "The Beatles")

    def test_karaoke_has_name(self):
        self.assertEqual("Super Cube", self.karaoke.name)

    def test_add_room_to_karaoke(self):
        self.karaoke.add_room_to_karaoke(self.room1)
        self.assertEqual(1, len(self.karaoke.rooms))

    def test_add_guest_to_room(self):
        self.karaoke.add_room_to_karaoke(self.room1)
        self.karaoke.add_guest_to_room(self.room1, self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_remove_guest_from_room(self):
        self.karaoke.add_room_to_karaoke(self.room1)
        self.karaoke.add_guest_to_room(self.room1, self.guest1)
        self.karaoke.remove_from_room(self.room1, self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_add_song_to_songbook(self):
        self.karaoke.add_to_song_book(self.song1)
        self.assertEqual(1, len(self.karaoke.song_book))

    def test_remove_from_songbook(self):
        self.karaoke.add_to_song_book(self.song1)
        self.karaoke.remove_from_song_book(self.song1)
        self.assertEqual(0, len(self.room1.playlist))

    def test_remove_from_songbook_song_doesnt_exist(self):
        self.karaoke.add_to_song_book(self.song1)
        result = self.karaoke.remove_from_song_book(self.song2)
        self.assertEqual("Song is not in songbook", result)

    def test_add_guest_to_room_no_space(self):
        self.karaoke.add_room_to_karaoke(self.room1)
        self.karaoke.add_guest_to_room(self.room1, self.guest1)
        self.karaoke.add_guest_to_room(self.room1, self.guest2)
        self.karaoke.add_guest_to_room(self.room1, self.guest3)
        result = self.karaoke.add_guest_to_room(self.room1, self.guest4)
        self.assertEqual("Room Full", result)

    def test_charge_entry_fee(self):
        self.karaoke.charge_entry_fee(self.guest1)
        self.assertEqual(205, self.karaoke.till)
        self.assertEqual(45, self.guest1.wallet)

    def test_charge_entry_fee_insufficient_funds(self):
        result = self.karaoke.charge_entry_fee(self.guest3)
        self.assertEqual(200, self.karaoke.till)
        self.assertEqual(0, self.guest3.wallet)
        self.assertEqual("You do not have enough money to enter", result)
