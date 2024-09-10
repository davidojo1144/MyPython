import unittest
import swap
class SwappingTest(unittest.TestCase):


    def test_that_swapping_exist(self):
        swap.swapping_two_strings("abc","xyz")

    def test_that_swapping_worked_succesfully(self):
        answer = swap.swapping_two_strings("abc","xyz")
        self.assertEqual(answer, "xycabz")


    def test_that_upper_and_lower_case_is_in_existence(self):
        swap.upper_before_lower("ChAracTERISticS")


    def test_that_upper_case_comes_before_lower_case(self):
        answer = swap.upper_before_lower("ChAracTERISticS")
        self.assertEqual(answer, "CATERIShractic")


    def test_that_adding_ce_is_in_existence(self):
        swap.adding_ce("helloo")


