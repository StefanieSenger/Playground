class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f"has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."


class Tiger(Cat):
    def __init__(self, mass, lifespan, speed, coat_pattern):
        super().__init__( mass, lifespan, speed)
        self.coat_pattern = coat_pattern

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg, "\
            f"has a {self.coat_pattern} coat_pattern, "\
            f"has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."



cat = Cat(3, 15, 40)
print(cat)
tiger = Tiger(180, 30, 80, "striped")
print(tiger)
