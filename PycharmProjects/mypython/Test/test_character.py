import unittest
import characters
class TestCharacters(unittest.TestCase):

    def test_that_character_exists(self):
        characters.check_characters("olamide")

    def test_if_character_is_correct(self):
            answer = characters.check_characters("olamide")
            self.assertTrue(answer)

    def test_that_check_character_ignore_case(self):
        answer = characters.check_characters("olAmide")
        self.assertEqual(answer, {'o':1, 'l':1, 'a':1, 'm':1, 'i':1, 'd':1, 'e':1})

