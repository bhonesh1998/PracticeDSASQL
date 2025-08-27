
from abc import ABC , abstractmethod

class animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    def move(self): # concrete method
        print("I am moving")

class dog(animal):

    def speak(self):
        print("Bark")

class cat(animal):

    def speak(self):
        print("Meow")

dog1 =dog()
dog1.speak()

cat().speak()

dog1.move()



