#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program tells if your integer is +, - or 0
# with user input


def main():
    # This function tells if your integer is +, - or 0

    # input
    your_number = int(input("Enter any number of your choice: "))

    # process
    if your_number > 0:
        # output
        print("")
        print("a+ , It is a positive number!")

    elif your_number < 0:
        # output
        print("")
        print("a- , It is a negative number!")

    else:
        print("")
        print("0")


if __name__ == "__main__":
    main()
