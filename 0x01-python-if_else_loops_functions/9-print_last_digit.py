#!/usr/bin/python3
def print_last_digit(number):
    number = (number * -1) if number < 0 else number
    print("{:d}".format(number % 10), end="")
    return (number % 10)
