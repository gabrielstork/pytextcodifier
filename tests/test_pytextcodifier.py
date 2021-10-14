from pytextcodifier import Encoder, Decoder
import unittest


class TestEncoder(unittest.TestCase):
    def test_as_str(self) -> None:
        text = Encoder('This is an example!', is_file=False)
        self.assertRaises(ValueError, text.encode, (5, 5))

        text.encode((100, 100))
        self.assertEqual(text.image.shape, (100, 100))

    def test_as_file(self) -> None:
        text = Encoder('example.txt', is_file=True)
        self.assertRaises(ValueError, text.encode, (5, 5))

        text.encode((100, 100))
        self.assertEqual(text.image.shape, (100, 100))


class TestDecoder(unittest.TestCase):
    def setUp(self) -> None:
        self.text = Encoder('example.txt', is_file=True)

    def test_public_image(self) -> None:
        self.text.encode(size=(250, 250), private=False)
        self.text.save('images/public_example.png')

        image = Decoder('images/public_example.png')
        image.decode()

        self.assertCountEqual(image.text, 'This is an example!')

    def test_private_image(self) -> None:
        self.text.encode(size=(250, 250), private=True)
        self.text.save('images/private_example.png')

        image = Decoder('images/private_example.png')
        image.decode(key='images/key_private_example.png')

        self.assertCountEqual(image.text, 'This is an example!')


if __name__ == '__main__':
    unittest.main()
