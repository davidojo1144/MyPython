from PycharmProjects.mypython.mylist import ArrayList
import unittest

class TestArrayList(unittest.TestCase):

    def setUp(self):
        self.arraylist = ArrayList()

    def test_that_list_is_empty(self):
        self.assertTrue(self.arraylist.is_empty())

    def test_to_add_element_and_arraylist_is_not_empty(self):
        self.assertTrue(self.arraylist.add(89) )
        self.assertFalse(self.arraylist.is_empty())

    def test_to_check_number_of_elements_in_the_arraylist(self):
        self.assertTrue(self.arraylist.add(59) )
        self.assertTrue(self.arraylist.add(23) )
        self.assertTrue(self.arraylist.add(5) )
        self.assertEqual(self.arraylist.size(), 3)

    def test_to_add_element_at_a_particular_element(self):
        self.assertTrue(self.arraylist.add(59))
        self.assertTrue(self.arraylist.add(23))
        self.assertTrue(self.arraylist.add(5))
        self.assertTrue(self.arraylist.add( 89))
        self.assertEqual(self.arraylist.size(), 4)