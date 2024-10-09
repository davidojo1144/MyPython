class Television:

    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.volume = 1

    def television_is_on(self):
        return self.is_on

    def television_that_tv_can_be_on(self):
        return self.is_on == True

    def television_is_on_now(self):
        return self.is_on == True

    def get_channel(self):
        if self.channel == 1 :
            return 1

    def check_channel_is_one_channel_one(self,channel):
        if channel < 1:
            raise ValueError("Channel must be greater than or equal to 1")

    def channel_can_increase(self,channel):
        if self.channel >= 1 and self.channel < 100:
            return channel + 1









