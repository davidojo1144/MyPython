import unittest

from PycharmProjects.mypython import exercise


class TestCheckEmail(unittest.TestCase):

    def test_if_check_exists(self):
        exercise.check_valid_email("davco1144@gmail.com")


