import unittest
from PycharmProjects.mypython.ac import Ac

class TestAc(unittest.TestCase):

    def test_ac_is_off(self):
        ac = Ac()
        ac.check_ac_is_on()

    def test_ac_can_be_switch_on(self):
        ac = Ac()
        ac.check_ac_is_on()
        ac = Ac()
        ac.check_ac_has_been_switched_on()


    def test_ac_is_on(self):
        ac = Ac()
        ac.check_ac_is_on()
        ac = Ac()
        ac.check_ac_has_been_switched_on()
        ac = Ac()
        ac.check_ac_is_off()


        