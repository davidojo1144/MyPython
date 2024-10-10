import unittest
from PycharmProjects.mypython.loan import Loan

class TestLoan(unittest.TestCase):
    def setUp(self):
        loan = Loan()
        self.loan = LoanBorrow("Ojo", "david", 10000.00)

    def test_that_loan_borrower_have_a_name(self):
        expected = "Ojo david"
        self.assertEqual(self.loan.get_name(), expected)

    def test_that_loan_borrower_have_a_loan_amount(self):
        expected = 10_000.00
        self.assertEqual(self.loan.get_loan_amount(), expected)

    def test_that_borrower_can_not_borrow_less_than_2k(self):
        self.assertRaises (ValueError, LoanBorrow, "Ojo", "david", 1000.00)

