class animal:  # parent class
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def sound(self):
        print("General sound")


class dog(animal):    # child class

    def walk(self):
        print("I am walking")

    def sound(self):
        print("Bark ! ")

class cat(animal):

    def sound(self):
        print("meow ! ")


dog1 = dog("tom","black")

print(dog1.name)
print(dog1.color)

dog2 = animal("tom","black")

dog2.sound()

dog1.sound()
dog1.walk()


cat1 = cat("xyz","white")

cat1.sound()


