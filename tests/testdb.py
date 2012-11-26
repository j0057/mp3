import unittest

import jjm.mp3.db

FILENAME = "../silence.mp3"

EXPECTED_OBJ = lambda: {
    "fn":           "../silence.mp3",
    "artist":       u"Silent Artist",
    "album":        u"Silent Album",
    "track":        "42",
    "title":        u"The Sound Of Silence",
    "bitrate":      320000,
    "length":       2.112,
    "year":         2012,
    "image_type":   u"image/jpeg",
    "image_size":   21992,
    "image_hash":   "cdc3b204ae00663fb57fa0f63c9d55fdd327667bcfd82e1921832b61872d39ed",
    "mtime":        1353959660
}

class TestTrack(unittest.TestCase):

    def assert_properties(self, track):
        self.assertIsNotNone(track)

        self.assertEqual(track.fn, "../silence.mp3")

        self.assertEqual(track.artist, "Silent Artist")
        self.assertEqual(track.album, "Silent Album")
        self.assertEqual(track.track, "42")
        self.assertEqual(track.title, "The Sound Of Silence")

        self.assertEqual(track.artist_url, "silent-artist")
        self.assertEqual(track.album_url, "silent-album")
        self.assertEqual(track.title_url, "the-sound-of-silence")

        self.assertEqual(track.bitrate, 320000)
        self.assertEqual(track.length, 2.112)

        self.assertEqual(track.year, 2012)

        self.assertEqual(track.image_type, 'image/jpeg')
        self.assertEqual(track.image_hash, 'cdc3b204ae00663fb57fa0f63c9d55fdd327667bcfd82e1921832b61872d39ed')
        self.assertEqual(track.image_size, 21992)

        self.assertEqual(track.library, 'Foo')
        self.assertEqual(track.library_url, 'foo')
   
    def test_from_file(self):
        track = jjm.mp3.db.Track.from_file(FILENAME, library="Foo", library_url='foo')

        self.assert_properties(track)

    def test_from_obj(self):
        track = jjm.mp3.db.Track.from_obj(EXPECTED_OBJ(), library='Foo', library_url='foo')

        self.assert_properties(track)

    def test_repr(self):
        track = jjm.mp3.db.Track.from_file(FILENAME)

        self.assertEqual(repr(track), "silent-artist/silent-album/42-the-sound-of-silence.mp3")

    def test_obj(self):
        track = jjm.mp3.db.Track.from_file(FILENAME)

        obj = track.obj()

        self.assertEqual(obj, EXPECTED_OBJ())

    
if __name__ == '__main__':
    unittest.main()

