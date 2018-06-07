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


def get_state(arg):
    if len(sys.argv) != 2:
        sys.exit()
    codes = reverse(sys.argv[1], capital_cities)
    for code in codes:
        print(*reverse(code, states))


if __name__ == '__main__':
    get_state()
