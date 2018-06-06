#!/usr/bin/env python3
import sys


states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}


capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}


def reverse(value, dict):
    return ([key for key, val in dict.items() if val == value])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()
    string = sys.argv[1]
    print(string.split(",")[0])
