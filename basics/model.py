#!/usr/bin/python3

class Calculator:

    @staticmethod
    def addition(x, y):
        added = x + y
        print(added)

    def subtraction(self, x, y):
        sub = x - y
        print(sub)

    def multiplication(self, x, y):
        mult = x * y
        print(mult)

    def division(self, x, y):
        div = x / y
        print(div)


Calculator.addition(3, 5)