import unittest
from PycharmProjects.mypython.myset import MySet

class TestMySet(unittest.TestCase):

    def setUp(self):
        self.my_set = MySet()

    def test_add_item(self):
        self.my_set.add_item(1)
        self.assertIn(1, self.my_set.get_items())

    def test_remove_item(self):
        self.my_set.add_item(2)
        self.my_set.remove_item(2)
        self.assertNotIn(2, self.my_set.get_items())

    def test_item_count(self):
        self.my_set.add_item(3)
        self.my_set.add_item(4)
        self.assertEqual(self.my_set.item_count(), 2)

    def test_no_duplicates(self):
        self.my_set.add_item(5)
        self.my_set.add_item(5)
        self.assertEqual(self.my_set.item_count(), 1)


