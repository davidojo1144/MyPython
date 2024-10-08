import unittest
from PycharmProjects.mypython import television
from PycharmProjects.mypython.television import Television


class TestTelevision(unittest.TestCase):

    def test_that_tv_is_on(self):
        tele = Television()
        tele.television_is_on()

    def test_that_tv_can_be_switch_on(self):
        tele = Television()
        tele.television_is_on()
        tele = Television()
        tele.television_that_tv_can_be_on()



    def test_that_tv_is_on_now(self):
        tele = Television()
        tele.television_is_on()
        tele = Television()
        tele.television_that_tv_can_be_on()
        tele.television_is_on_now()



    def test_that_theres_a_channel_when_tv_is_on(self):
        tele = Television()
        tele.television_is_on()
        tele = Television()
        tele.television_that_tv_can_be_on()
        tele.television_is_on_now()
        tele.get_channel()

    def test_that_tv_channel_cannot_be_less_than_one(self):
        tele = Television()
        tele.television_is_on()
        tele = Television()
        tele.television_that_tv_can_be_on()
        tele.television_is_on_now()
        tele.get_channel()
        result = tele.check_channel_is_one_channel_one(1)
        self.assertFalse(result)

    def test_that_channel_can_go_up(self):
        tele = Television()
        tele.television_is_on()
        tele = Television()
        tele.television_that_tv_can_be_on()
        tele.television_is_on_now()
        tele.get_channel()
        result = tele.check_channel_is_one_channel_one(1)
        self.assertFalse(result)
        tele.channel_can_increase()


