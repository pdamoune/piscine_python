#!/usr/bin/env python3
import sys


def get_capital():
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"}
    return(capital_cities)


def get_state():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"}
    return(states)


def main():
    if len(sys.argv) != 2:
        return
    state = get_state()
    index = state.get(sys.argv[1])
    if type(index) != str:
        return(print("Unknown state"))
    capital = get_capital()
    print(capital[index])


if __name__ == '__main__':
    main()
