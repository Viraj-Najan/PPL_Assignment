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






class herbivores(wild_animals):

    def food(self):

        print("Plant based")



class deer(herbivores):

    def speak(self):

        print("click")

    def colour(self):

        print("Brown")


class elephant(herbivores):

    def speak(self):

        print("trumpet")

    def colour(self):

        print("Grey")


class zebra(herbivores):

    def speak(self):

        print("idk")

    def colour(self):

        print("Black and white")







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

        print("ba aa aaaa")

    def colour(self):

        print("black, brown, white. etc")



p1=Animals(4, 3)

Max = lion()

Max.speak()

Max.place()

Max.colour()

print(Max.eyes)

print(Max.legs)