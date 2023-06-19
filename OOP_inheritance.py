# Let’s assume that an image can either be a GIF or a JPG. Implement these subclasses of Image,
# then override the display method in each to also include a reference to what type it is.

from abc import ABC, abstractmethod

class Image(ABC):

    @abstractmethod
    def __str__(self):
        pass


class GIF(Image):

    def __str__(self):
        return f'This image is of type {type(self).__name__.lower()}.'


class JPG(Image):

    def __str__(self):
        return f'This image is of type {type(self).__name__.lower()}.'


gif1 = GIF()
jpg1 = JPG()

print(gif1)
print(jpg1)


# Image() class not instantializable, becaus it is an abstract class. In order
# to be one it needs to inherit from ABC and have at least one abstract method
# and it should not have a `def __init__(self): pass` defined.

# image1 = Image()
# print(image1)
