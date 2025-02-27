class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

# instantiate the Parrot class
blu = Parrot("Blu", 10, "red")
woo = Parrot("Woo", 15, "orange")

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attribute age
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# access the instance attribute colour
print("{}'s main colour is {}".format( blu.name, blu.colour))
print("{}'s main colour is {}".format( woo.name, woo.colour))
