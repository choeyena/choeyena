class TV:
     def __init__(self):
         self.channel = 1
         ...
         
     def turnOn(self):
         ...
         
class TV:
     def __init__(self):
         self.channel = 1
         self.volume = 0 
         self.on = False 
         
     def turnOn(self):
         self.on = True
         
     def turnOff(self):
         self.on = False
         
     def setVolume(self, volume):
         self.volume = volume
         
     def setChannel(self, channel):
         self.channel = channel
tv = TV()
tv.turnOn()
tv.setChannel(11)
tv.setVolume(6)

print("TV의 채널: ", tv.channel, "TV의 음량:", tv.volume);