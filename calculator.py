
from re import X
from typing_extensions import Self

from click import prompt


class Calculator():

    def __init__(self):
        self.x = int(input("Enter first Number "))
        self.y = int(input("Enter second Number "))

    def add(self):
        add = self.x + self.y
        print(add)

    def subtraction(self):
        sub = self.x - self.y
        print(sub)

    def multiply(self):
        ans = self.x * self.y
        print(ans)

    def divide(self):
        jibu = self.x//self.y
        print(jibu)

calc = Calculator()
calc.add()
calc.multiply()