class Ac:

    def __init__(self):
        self.is_off = False
        self.increment = 1
        self.decrement = 1
        self.highest_temp = 30
        self.lowest_temp = 16


    def check_ac_is_off(self):
        return self.is_off


    def check_ac_has_been_switched_on(self):
        return self.is_off == True

    def check_ac_is_on(self):
        return self.is_off == True

    def check_ac_temperature_increased(self, temperature):
        return temperature + self.increment


    def check_ac_temperature_decreased(self, temperature):
        return temperature - self.decrement


    def ac_temp_cannot_go_beyond_30(self, temperature):
        if temperature < self.highest_temp:
            return temperature + self.increment
        elif temperature > self.highest_temp:
            return self.highest_temp


    def ac_temp_cannot_get_below_16(self, temperature):
        if temperature > self.lowest_temp:
            return temperature + self.increment
        elif temperature < self.lowest_temp:
            return self.lowest_temp


