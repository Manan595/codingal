from abc import ABC, abstractmethod

class animal(ABC):
    def move (self):
        pass

class Human(animal):
    def move (self):
        print(" I can walk and run")

class Snake(animal):
    def move (self):
        print(" I can crawl")

class Dog(animal):
    def move (self):
        print(" I can bark")

class Lion(animal):
    def move (self):
        print(" I can roar")      

r=Human()
r.move()

k=Snake()
k.move()
r=Dog()
r.move()
k=Lion()
k.move()