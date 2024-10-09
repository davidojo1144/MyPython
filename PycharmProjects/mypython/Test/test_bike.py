import unittest
from PycharmProjects.mypython.bike import Bike


class TestBike(unittest.TestCase):

    def test_bike_is_off(self):
        bike = Bike()
        bike.bike_is_off()

    def test_that_bike_can_turned_on(self):
        bike = Bike()
        bike.bike_is_off()
        bike = Bike()
        bike.bike_can_be_turned_on()

    def test_that_bike_is_on(self):
        bike = Bike()
        bike.bike_is_off()
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        bike.bike_is_on()

    def test_that_bike_can_be_turned_off(self):
        bike = Bike()
        bike.bike_is_off()
        bike = Bike()
        bike.bike_can_be_turned_on()
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        bike.bike_can_be_turned_off()

    def test_that_bike_can_accelerate_on_gear_one(self ):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_accelerate_on_gear_one(15), 16)

    def test_that_bike_can_accelerate_on_gear_two(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_accelerate_on_gear_two(24), 26)

    def test_that_bike_can_accelerate_on_gear_three(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_accelerate_on_gear_three(35), 38)


    def test_that_bike_can_accelerate_on_gear_four(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_accelerate_on_gear_four(44), 48)

    def test_that_bike_can_decelerate_on_gear_one(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_decelerate_on_gear_one(15), 14)


    def test_that_bike_can_decelerate_on_gear_two(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_decelerate_on_gear_two(24), 22)


    def test_that_bike_can_decelerate_on_gear_three(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_decelerate_on_gear_three(35), 32)


    def test_that_bike_can_decelerate_on_gear_four(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_can_decelerate_on_gear_four(44), 40)


    def test_for_gear_changes_while_accelerating(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_gear_changes_automatically_while_accelerating(17),18)
        self.assertEqual(bike.bike_gear_changes_automatically_while_accelerating(26), 28)
        self.assertEqual(bike.bike_gear_changes_automatically_while_accelerating(35), 38)
        self.assertEqual(bike.bike_gear_changes_automatically_while_accelerating(100), 104)



    def test_for_gear_changes_while_decelerating(self):
        bike = Bike()
        bike.bike_is_on()
        bike = Bike()
        self.assertEqual(bike.bike_gear_changes_automatically_while_decelerating(44),40)
        self.assertEqual(bike.bike_gear_changes_automatically_while_decelerating(17), 16)
        self.assertEqual(bike.bike_gear_changes_automatically_while_decelerating(25), 23)
        self.assertEqual(bike.bike_gear_changes_automatically_while_decelerating(34), 31)





        















