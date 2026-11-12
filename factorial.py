#!/usr/bin/env python3
# Created by: Elohim Conteh
# Created on: Nov 2026
# This program calculates the factorial of a whole number using a do..while loop


def main():
    # this function calculates the factorial of a whole number
    loop_counter = 0
    factorial_answer = 1

    # input
    user_number_as_string = input("Enter a whole number: ")
    print("")

    # process & output
    try:
        user_number = int(user_number_as_string)

        if user_number >= 0:
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                if loop_counter >= user_number:
                    break

            print("{0}! = {1}".format(user_number, factorial_answer))
        else:
            print("Please enter a positive integer.")
    except Exception:
        print("Invalid input. Please enter a whole number.")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
