import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Everything in it's right place")
        self.song_2 = Song("Kid A")
        # songs = [self.song_1, self.song_2]

    def test_song_has_name(self):
        self.assertEqual("Everything in it's right place", self.song_1.song_name)