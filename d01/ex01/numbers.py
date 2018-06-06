#!/usr/bin/env python3


def main():
    with open('numbers.txt', 'r') as file:
        for num in file:
            print(num.replace(",", "\n"), end='')


if __name__ == '__main__':
    main()
