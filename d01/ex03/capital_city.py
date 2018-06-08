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


def get_capital():
    if len(sys.argv) != 2:
        sys.exit()
    state = states.get(sys.argv[1])
    if not state:
        sys.exit("Unknown state")
    print(capital_cities[state])


if __name__ == '__main__':
    get_capital()
