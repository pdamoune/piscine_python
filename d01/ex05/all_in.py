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


def get_capital(arg):
    for key in states.items():
        if arg.lower() == key[0].lower():
            return(capital_cities[key[1]], key[0])


def get_state(arg):
    for k, val in capital_cities.items():
        if arg.lower() == val.lower():
            for value, key in states.items():
                if key == k:
                    return(val, value)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()
    string = sys.argv[1]
    split_str = (' '.join(string.split())).split(", ")      # join
    split_str = [x for x in split_str if x]                 # remove empty
    for argv in split_str:
        result = get_capital(argv) or get_state(argv)
        if result:
            print(result[0], "is the capital of", result[1])
        else:
            print(argv, "is neither a capital city nor a state")
