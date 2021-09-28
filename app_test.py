import app
import unittest
from unittest.mock import patch


class TestApp(unittest.TestCase):
    def setUp(self):
        print('Start Testing')

    def test_check_document_existance(self):
        self.assertEqual(app.check_document_existance('11-2'), True)
        self.assertEqual(app.check_document_existance('100'), False)

    @patch('app.input')
    def test_get_owner_name(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(app.get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf('11-2')
        self.assertEqual(app.directories['1'], ['2207 876234', '5455 028765'])

    @patch('app.input')
    def test_move_doc_to_shelf(self, user_input):
        user_input.side_effect = ['10006', '2']
        app.move_doc_to_shelf()
        self.assertEqual(app.directories['2'], ['10006'])

    @patch('app.input')
    def test_get_doc_shelf(self, user_input):
        user_input.side_effect = ['2207 876234']
        shelf = app.get_doc_shelf()
        self.assertEqual(shelf, '1')

    @patch('app.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(app.delete_doc(), ('11-2', True))

    def tearDown(self):
        print('Testing over')


if __name__ == '__main__':
    unittest.main()