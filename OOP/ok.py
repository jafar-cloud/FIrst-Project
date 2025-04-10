from random import choice


class Fruit:
    def __init__(self, fruits: dict):
        self.fruits = fruits

    def enter_quiz(self):
        print("WELCOME TO THE QUIZ!")
        fruit = choice(self.fruits.items())

        user_inp = input(f"What is the color of: {fruit}? ")

        if user_inp == self.fruits[fruit]:
            print("YOU WIN!")
        else:
            print("WRONG INPUT!!")