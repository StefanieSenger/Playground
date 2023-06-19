# Create a class called Camera and a class called MobilePhone that will be the
# base classes of a derived class called CameraPhone. The CameraPhone class
# should be initialized with the memory attribute and should have a
# take_picture() method that prints out the message, Say cheese!.

# Create a Camera class with a take_picture() method that prints the message,
# "Say cheese!".

# Create a MobilePhone class that will be initialized with a memory attribute.

# Create a CameraPhone class that inherits from both the MobilePhone and Camera
# classes.

class Camera():

    def take_picture(self):
        print('Say cheese!')


class MobilePhone():

    def __init__(self, memory):
        self.memory = memory


class CameraPhone(Camera, MobilePhone):
    pass


cameraphone = CameraPhone("200KB")
cameraphone.take_picture()
print(cameraphone.memory)
