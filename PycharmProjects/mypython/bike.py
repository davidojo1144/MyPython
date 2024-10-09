class Bike:

    def __init__(self):
        self.is_on = False
        self.gear_one = 1
        self.gear_two = 2
        self.gear_three = 3
        self.gear_four = 4
        self.gear_speed1 = 20
        self.gear_speed2 = 30
        self.gear_speed3 = 40
        self.gear_speed4 = 41

    def bike_is_off(self):
        return self.is_on

    def bike_can_be_turned_on(self):
        return self.is_on == True

    def bike_is_on(self):
        return self.is_on == True

    def bike_can_be_turned_off(self):
        return self.is_on

    def bike_can_accelerate_on_gear_one(self,speed):
        if self.gear_one == 1:
            return speed + self.gear_one
        else :
            return speed

    def bike_can_accelerate_on_gear_two(self, speed):
        if self.gear_two == 2:
            return speed + self.gear_two
        else:
            return speed

    def bike_can_accelerate_on_gear_three(self, speed):
        if self.gear_three == 3:
            return speed + self.gear_three
        else:
            return speed

    def bike_can_accelerate_on_gear_four(self, speed):
        if self.gear_four == 4:
            return speed + self.gear_four
        else:
            return speed

    def bike_can_decelerate_on_gear_one(self, speed):
        if self.gear_one == 1:
            return speed - self.gear_one
        else :
            return speed

    def bike_can_decelerate_on_gear_two(self, speed):
        if self.gear_two == 2:
            return speed - self.gear_two
        else:
            return speed

    def bike_can_decelerate_on_gear_three(self, speed):
        if self.gear_three == 3:
            return speed - self.gear_three
        else:
            return speed

    def bike_can_decelerate_on_gear_four(self, speed):
        if self.gear_four == 4:
            return speed - self.gear_four
        else:
            return speed

    def bike_gear_changes_automatically_while_accelerating(self, speed):
        if speed <= self.gear_speed1:
            return speed + self.gear_one
        elif speed == 21 or speed <= self.gear_speed2:
            return speed + self.gear_two
        elif speed == 31 or speed <= self.gear_speed3:
            return speed + self.gear_three
        elif speed >= self.gear_speed4:
            return speed + self.gear_four


    def bike_gear_changes_automatically_while_decelerating(self,speed):
        if speed <= self.gear_speed1:
            return speed - self.gear_one
        elif speed == 21 or speed <= self.gear_speed2:
            return speed - self.gear_two
        elif speed == 31 or speed <= self.gear_speed3:
            return speed - self.gear_three
        elif speed >= self.gear_speed4:
            return speed - self.gear_four
















