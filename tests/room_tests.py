import unittest
from classes.room import Room
from classes.song import Song
from classes.karaoke_bar import KaraokeBar


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.karaoke = KaraokeBar("Super Cube", 200)
        self.room1 = Room("Room1", 3)
        self.room2 = Room("Room2", 5)
        self.song1 = Song("Hello", "Adele")
        self.song2 = Song("Help", "The Beatles")


    def test_room_has_name(self):
        self.assertEqual("Room1", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room1.capacity)

    def test_capacity_3_result_3(self):
        self.assertEqual(3, self.room1.check_capacity())

    def test_guests_in_room(self):
        self.assertEqual(0, self.room1.check_guests_in_room())

    def test_add_song_to_playlist(self):
        self.karaoke.add_to_song_book(self.song1)
        self.room1.add_to_playlist(self.karaoke.song_book, self.song1)
        self.assertEqual(1, len(self.room1.playlist))
    
    def test_add_song_to_playlist_not_in_songbook(self):
        self.karaoke.add_to_song_book(self.song1)
        result = self.room1.add_to_playlist(self.karaoke.song_book, self.song2)
        self.assertEqual("song not available", result)

    def test_sing_song(self):
        self.karaoke.add_to_song_book(self.song1)
        self.room1.add_to_playlist(self.karaoke.song_book, self.song1)
        self.room1.sing_song(self.song1)
        self.assertEqual(0, len(self.room1.playlist))
