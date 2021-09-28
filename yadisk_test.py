import unittest
from yadisk_folder import YaFolder


class TestYandexFolder(unittest.TestCase):
    def setUp(self):
        self.yadisk = YaFolder('')

    def test_folder(self):
        self.assertEqual(self.yadisk.create_yadisk_folder('test').status_code, 201)

    def test_passed_create_folder(self):
        self.assertEqual(self.yadisk.create_yadisk_folder('').status_code, 409)

    def tearDown(self):
        del self.yadisk


if __name__ == '__main__':
    unittest.main()
