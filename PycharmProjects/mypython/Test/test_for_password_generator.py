import unittest
import  re
from PycharmProjects.mypython.passwordgenerator import password


class TestPassword(unittest.TestCase):

    def testThatPasswWordExists(self):
        self.assertTrue(password())


    def testThatPasswordWillIncludeDigits(self):
        expected =  password()
        number = r'\d'
        re.findall(number, expected)
        self.assertTrue(re.findall(number, expected))

    def testThatPasswordWillIncludeLowerCaseDigits(self):
        result = password()
        number = r'\d[a-z]+'
        self.assertTrue(re.findall(number, result))

    def testThatPasswordWillIncludeUpperCaseLowerCaseAndDigits(self):
        result = password()
        number = r'\d[a-z]+[A-Z]'
        self.assertTrue(re.findall(number, result))

    def testThatPasswordWillIncludeLowerCaseUpperCaseDigitsAndSymbol(self):
        result = password()
        number = r'\d[a-z]+[A-Z]\W'
        self.assertTrue(re.findall(number, result))

    def testThatPassWordIsNotMoreThan16(self):
        result = password()
        self.assertNotEqual(result, 32)
        self.assertEqual(len(result), 16)


    def testThatPassWordIsNotLessThan16(self):
        result = password()
        self.assertNotEqual(result, 12)
        self.assertEqual(len(result), 16)