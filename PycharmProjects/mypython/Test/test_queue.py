import unittest
from PycharmProjects.mypython.queue import Queue


class TestQueue(unittest.TestCase):


    def setUp(self):
        self.queue = Queue()

    def test_that_queue_is_empty(self):
        self.assertFalse(self.queue.is_empty())

    def test_that_queue_add_value(self):
        self.queue.append("James")
        self.assertEqual(self.queue.get_size(), 1)

    def test_that_queue_remove_item(self):
        self.queue.append("James")
        self.queue.append("Jack")
        self.queue.popleft()
        self.assertEqual(self.queue.get_size(), 1)

    def test_that_queue_can_show_items_left(self):
        self.queue.append("James")
        self.queue.append("Jack")
        self.assertEqual(self.queue.dequeue(), "James", )

    def test_that_queue_can_remove_one_item_and_dequeue_item_left(self):
        self.queue.append("Musa")
        self.queue.append("James")
        self.queue.append("Jack")
        self.queue.append("Mimi")
        self.queue.append("Mark")
        self.queue.popleft()
        self.assertEqual(self.queue.dequeue(), "James")
        self.assertEqual(self.queue.dequeue(), "Jack")
        self.assertEqual(self.queue.dequeue(), "Mimi")
        self.assertEqual(self.queue.dequeue(), "Mark")