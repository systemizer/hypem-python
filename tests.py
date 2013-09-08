import hypem
import unittest

class TestHypemFunctions(unittest.TestCase):

    def test_get_popular(self):
        playlist = hypem.get_popular()
        self.assertIsNotNone(playlist.data)

    def test_get_latest(self):
        playlist = hypem.get_latest()
        self.assertIsNotNone(playlist.data)

    def test_get_artist(self):
        playlist = hypem.get_artist("Siriusmo")
        self.assertIsNotNone(playlist.data)

    def test_get_favorites(self):
        playlist = hypem.get_favorites("systemizer")
        self.assertIsNotNone(playlist.data)

    def test_get_listening_history(self):
        playlist = hypem.get_favorites("systemizer")
        self.assertIsNotNone(playlist.data)

    def test_get_obsessed(self):
        playlist = hypem.get_favorites("systemizer")
        self.assertIsNotNone(playlist.data)

    def test_get_user(self):
        playlist = hypem.get_user("systemizer")
        self.assertIsNotNone(playlist.data)
        

if __name__ == '__main__':
    unittest.main()
