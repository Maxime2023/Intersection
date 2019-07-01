#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## Maths
## File description:
## 104intersection: display
##

import sys
import os

def my_print_usage():
    print("USAGE\n      ./104intersection opt xp yp zp xv yv zv p\n")
    print("DESCRIPTION")
    print("      opt             surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("      (xp, yp, zp)    coordinates of a point by which the light ray passes through")
    print("      (xv, yv, zv)    coordinates of a vector parallel to the light ray")
    print("      p               parameter: radius of the sphere, radius of the cylinder, or")
    print("                      angle formed by the cone and the Z-axis")
    return (0)

def my_check_arg():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            my_print_usage()
            sys.exit(0)
        else:
            print("USAGE\n      ./104intersection opt xp yp zp xv yv zv p")
            sys.exit(84)
    elif len(sys.argv) != 9:
        print("USAGE\n      ./104intersection opt xp yp zp xv yv zv p")
        sys.exit(84)
    if len(sys.argv) == 9:
        a = 1
        while a < 9:
            for d in sys.argv[a]:
                if ((d >= 'a' and d <= 'z') or (d >= 'A' and d <= 'Z')) and d != '-' and d != '+':
                    print("Int numbers only\n")
                    my_print_usage()
                    sys.exit(84)
            a += 1
        if len(sys.argv[1]) == 1:
            if sys.argv[1][0] != '1' and sys.argv[1][0] != '2' and sys.argv[1][0] != '3':
                print("opt             surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
                sys.exit(84)
        else:
            my_print_usage()
            sys.exit(84)
