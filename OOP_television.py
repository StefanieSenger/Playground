
class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.listOfChannels = list(range(1, 11)) # 10 channels from 1 to 10
        self.currentChannel = 1
        self.listOfVolumes = list(range(21)) # 21 volumes from 0 to 20
        self.currentVolume = 10

    def turn_on_and_off(self):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True

    def channel_up(self):
        if self.isOn:
            if self.currentChannel < max(self.listOfChannels):
                self.currentChannel += 1
            else:
                self.currentChannel = 1

    def channel_down(self):
        if self.isOn:
            if self.currentChannel > min(self.listOfChannels):
                self.currentChannel -= 1
            else:
                self.currentChannel = max(self.listOfChannels)

    def set_channel(self, input):
        self.currentChannel = input

    def raise_volume(self):
        if self.isOn:
            if self.currentVolume < max(self.listOfVolumes):
                self.currentVolume += 1
            if self.currentVolume  != 0:
                self.isMuted = False

    def lower_volume(self):
        if self.isOn:
            if self.currentVolume > min(self.listOfVolumes):
                self.currentVolume -= 1
            if self.currentVolume  == 0:
                self.isMuted = True

    def __str__(self):
        return f"The TV is on: {self.isOn}. "\
                f"The TV is muted: {self.isMuted}. "\
                f"The current channel is: {self.currentChannel}. "\
                f"The current volume is: {self.currentVolume}. "\
                "___________________________________"


old_fashioned_tv = TV()
print(old_fashioned_tv)
old_fashioned_tv.turn_on_and_off()
print(old_fashioned_tv)
old_fashioned_tv.channel_down()
print(old_fashioned_tv)
for i in range(15):
    old_fashioned_tv.raise_volume()
print(old_fashioned_tv)
old_fashioned_tv.turn_on_and_off()
print(old_fashioned_tv)
old_fashioned_tv.lower_volume()
print(old_fashioned_tv)
old_fashioned_tv.turn_on_and_off()
old_fashioned_tv.channel_up()
for i in range(21):
    old_fashioned_tv.lower_volume()
print(old_fashioned_tv)
old_fashioned_tv.set_channel(4)
print(old_fashioned_tv)
