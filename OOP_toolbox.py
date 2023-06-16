# Exercise on OOP
#
# The classes Screw and Nail are given, then ....

class Screw:
    MAX_TIGHTNESS = 5
    def __init__(self):
        self.tightness = 0
    def loosen(self):
        if (self.tightness > 0):
            self.tightness -= 1
    def tighten(self):
        if (self.tightness < self.MAX_TIGHTNESS):
            self.tightness += 1
    def __str__(self):
        return "Screw with tightness {}".format(self.tightness)

class Nail:
    def __init__(self):
        self.in_wall = False
    def nail_in(self):
        if (not self.in_wall):
            self.in_wall = True
    def remove(self):
        if (self.in_wall):
            self.in_wall = False
    def __str__(self):
        return "Nail {}in wall.".format("" if self.in_wall else "not ")


# 1. Instantiate a toolbox, a screwdriver, and a hammer.

class Toolbox:
    has_screwdriver = False
    has_hammer = False

class Screwdriver:
    def tighten(self, screw):
        screw.tighten()

class Hammer:
    def hammer_in(self, nail):
        nail.nail_in()

toolbox = Toolbox()
screwdriver = Screwdriver()
hammer = Hammer()


# 2. Put the hammer and screwdriver in the toolbox.

if screwdriver:
    toolbox.has_screwdriver = True
if hammer:
    toolbox.has_hammer = True


# 3. Instantiate a screw, and tighten it using the screwdriver. Print the screw before and after it's been tightened.

screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)


# 4. Instantiate a nail, then hammer it in using the hammer. Print the nail before and after it’s been hammered in.
nail = Nail()
print(nail)
hammer.hammer_in(nail)
print(nail)
