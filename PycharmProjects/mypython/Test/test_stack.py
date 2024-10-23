import unittest

from PycharmProjects.mypython.stack import MyStack

class StackTest(unittest.TestCase):
        def setUp(self):
            self.stack = MyStack(5)

        def test_that_stack_have_a_size(self):
            self.assertEqual(5, self.stack.get_stack_size())

        def test_that_stack_have_a_empty_stack(self):
            self.assertTrue(self.stack.is_empty())

        def test_that_stack_can_accept_element(self):
            self.stack.push(16)
            self.assertFalse(self.stack.is_empty())

        def test_that_stack_can_accept_two_or_more_elements(self):
            self.stack.push(16)
            self.stack.push(35)
            self.stack.push(2)
            self.assertFalse(self.stack.is_empty())

        def test_that_stack_can_not_contain_element_more_than_the_size(self):
            self.stack.push(16)
            self.stack.push(35)
            self.stack.push(87)
            self.stack.push(31)
            self.stack.push(60)
            self.assertRaises(IndexError, self.stack.push, 42)

        def test_that_stack_can_pop_element_store_inside(self):
            self.stack.push(16)
            self.stack.push(35)
            self.stack.push(2)
            self.stack.push(87)
            self.stack.push(31)
            self.stack.pop()
            self.assertEqual(self.stack.get_element_number(), 4)

        def test_that_stack_can_pop_the_last_element_store_inside(self):
            self.stack.push(16)
            self.stack.push(35)
            self.stack.push(2)
            self.stack.push(87)
            self.stack.push(31)
            self.assertEqual(self.stack.pop(), 31)

