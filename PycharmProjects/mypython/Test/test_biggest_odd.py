import unittest
import biggestodd

class TestBiggestOdd(unittest.TestCase):
    def test_biggest_odd_is_existing(self):
        biggestodd.biggest_odd("23956")

    def test_biggest_odd(self):
        result = biggestodd.biggest_odd("23956")
        self.assertEqual(result, 9)

    def test_equal_strings_to_check_if_true_or_false(self):
        result = biggestodd.equal_strings("love", "evol")
        self.assertTrue(result)





