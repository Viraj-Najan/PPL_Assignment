class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(Animals):
    def place(self):
        print("Jungle")


class carnivores(wild_animals):
    def food(self):
        print("Meat")


class tiger(carnivores):
    def speak(self):
        print("Roar")

    def colour(self):
        print("Orange")


class lion(carnivores):
    def speak(self):
        print("Roar")

    def colour(self):
        print("Yellow")


class hyena(carnivores):
    def speak(self):
        print("laugh")

    def colour(self):
        print("Grey")
class wolf(carnivores):
    def speak(self):
        print("Roar")

    def colour(self):
        print("Grey")
class Fox(carnivores):
    def speak(self):
        print("Bark")

    def colour(self):
        print("Grey")

class Leopard(carnivores):
    def speak(self):
        print("Roar")

    def colour(self):
        print("Yellow")

class herbivores(wild_animals):
    def food(self):
        print("Plant based")


class deer(herbivores):
    def speak(self):
        print("dummyvalue")

    def colour(self):
        print("Brown")


class elephant(herbivores):
    def speak(self):
        print("dummyvalue")

    def colour(self):
        print("Grey")


class zebra(herbivores):
    def speak(self):
        print("idk")

    def colour(self):
        print("Black and white")



class monkey(herbivores):
    def speak(self):
        print("whoop whoop")

    def colour(self):
        print("Black and Grey")

class domestic_animals(Animals):

    def place(self):
        print("Areas habitated by human beings")


class dog(domestic_animals):
    def speak(self):
        print("bark")

    def colour(self):
        print("brown, black, white, golden, etc")


class cat(domestic_animals):
    def speak(self):
        print("meow")

    def colour(self):
        print("Grey,brown, black, white, etc")


class cow(domestic_animals):
    def speak(self):
        print("moo")

    def colour(self):
        print("white, brown,etc")


class goat(domestic_animals):
    def speak(self):
        print("dummyvalue")

    def colour(self):
        print("black, brown, white. etc")

class sheep(domestic_animals):
    def speak(self):
        print("dummyvalue")

    def colour(self):
        print("black, brown, white. etc")

p = Animals(4, 3)
Max = monkey()
Max.speak()
Max.place()
Max.colour()
print(Max.eyes)
print(Max.legs)


