import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Hello", "Adele")
        self.song2 = Song("Help", "The Beatles")
        self.song3 = Song("Baby Shark", "Pinkfong")

    def test_song_has_a_title(self):
        self.assertEqual("Hello", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Adele", self.song1.artist)
