#!/usr/bin/env python3
import string
import turtle


class Time():
    """docstring for ."""
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __repr__(self):
        return("Time(%d, %d, %d)" % (self.h, self.m, self.s))

    def __str__(self):
        return("Il est %dh %dm %ds" % (self.h, self.m, self.s))

    def affiche_heure(self):
        print("%d:%d:%d" % (self.h, self.m, self.s))


if __name__ == '__main__':

    time = Time(1, 2, 3)
    print(time)
