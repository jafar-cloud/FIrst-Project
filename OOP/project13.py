from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("Moving human")


class Dog(Animal):
    def move(self):
        print("Moving Dog")