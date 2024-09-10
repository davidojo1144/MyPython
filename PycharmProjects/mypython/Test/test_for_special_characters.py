import unittest
import specialcharacters
class special_characters(unittest.TestCase):

    def test_that_bad_characters_exist(self):
        specialcharacters.special_characters("he,ll.o")

    def test_that_bad_characters_was_removed_successfully(self):
        answer = specialcharacters.special_characters("he,ll.o")
        answer2 = specialcharacters.special_characters("da;n:i'e;l")
        self.assertEqual(answer, "hello")
        self.assertEqual(answer2, "daniel")
