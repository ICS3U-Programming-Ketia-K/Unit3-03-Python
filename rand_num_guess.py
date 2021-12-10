#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 2021
# This program checks if the guessed number is equal to
# the generated random number


import random


def main():
    # This function checks if the guessed number is equal to
    # the generated random number

    # input
    random_number = random.randint(0, 9)
    guessed_number = int(input("Guess a number between 0 and 9: "))
    print("")

    # process and output
    if guessed_number == random_number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong.")
        print("The correct number is {}".format(random_number))


if __name__ == "__main__":
    main()
