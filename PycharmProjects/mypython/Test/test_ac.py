import unittest
from PycharmProjects.mypython.ac import Ac

class TestAc(unittest.TestCase):

    def test_ac_is_off(self):
        ac = Ac()
        self.assertFalse(ac.ac_is_off())

    def test_that_ac_can_turned_on(self):
        ac = Ac()
        self.assertFalse(ac.ac_is_off())
        self.assertTrue(ac.ac_can_be_turned_on())


    def test_that_ac_is_on(self):
        ac = Ac()
        self.assertFalse(ac.ac_is_off())
        self.assertTrue(ac.ac_can_be_turned_on())
        self.assertTrue(ac.ac_is_on())


    def test_that_ac_temperature_increased(self):
        ac = Ac()
        self.assertTrue(ac.ac_is_on())
        self.assertEqual(ac.check_ac_temperature_increased(1),2)

    def test_that_ac_temperature_decreased(self):
        ac = Ac()
        self.assertTrue(ac.ac_is_on())
        self.assertEqual(ac.check_ac_temperature_decreased(5), 4)


    def test_that_ac_cannot_be_increased_beyond_30(self):
        ac = Ac()
        self.assertTrue(ac.ac_is_on())
        self.assertEqual(ac.ac_temp_cannot_go_beyond_30(35),30)

    def test_that_ac_cannot_be_decreased_below_16(self):
        ac = Ac()
        self.assertTrue(ac.ac_is_on())
        self.assertEqual(ac.ac_temp_cannot_get_below_16(12),16)



        