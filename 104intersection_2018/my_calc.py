#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## Maths
## File description:
## 104intersection
##

import math as m
import sys
import os

def final_cal(a, b, c, P, V):
    delta = m.pow(b, 2)  - (4 * a * c)
    if delta < 0:
        print("No intersection point.")
    elif delta == 0:
        if b == 0:
            print("There is an infinite number of intersection points.")
        else:
            n = -b / (2 * a)
            print("1 intersection point:")
            print("({0:.3f}, {1:.3f}, {2:.3f})".format(n * V.x+ P.x, n * V.y + P.y, n * V.z + P.z))
    elif delta > 0:
        n1 = (-b + m.sqrt(delta)) / (2 * a)
        n2 = (-b - m.sqrt(delta)) / (2 * a)
        print("2 intersection points:")
        print("({0:.3f}, {1:.3f}, {2:.3f})".format(P.x + n1 * V.x, P.y + n1 * V.y, P.z + n1 * V.z))
        print("({0:.3f}, {1:.3f}, {2:.3f})".format(P.x + n2 * V.x, P.y + n2 * V.y, P.z + n2 * V.z))

def my_sphere(P, V, par):
    print("Sphere of radius {0:d}".format(par))
    print("Line passing through the point ({0:d}, {1:d}, {2:d}) "\
          "and parallel to the vector ({3:d}, {4:d}, {5:d})".format(P.x, P.y, P.z, V.x, V.y, V.z))
    a = m.pow(V.x, 2) + m.pow(V.y, 2) + m.pow(V.z, 2)
    b = (2 * P.x * V.x) + (2 * P.y * V.y) + (2 * P.z * V.z)
    c = m.pow(P.x, 2) + m.pow(P.y, 2) + m.pow(P.z, 2) - m.pow(par, 2)
    final_cal(a, b, c, P, V)

def my_cylinder(P, V, par):
    print("Cylinder of radius {0:d}".format(par))
    print("Line passing through the point ({0:d}, {1:d}, {2:d}) "\
          "and parallel to the vector ({3:d}, {4:d}, {5:d})".format(P.x, P.y, P.z, V.x, V.y, V.z))
    a = m.pow(V.x, 2) + m.pow(V.y, 2)
    b = (2 * P.x * V.x) + (2 * P.y * V.y)
    c = m.pow(P.x, 2) + m.pow(P.y, 2) - m.pow(par, 2)
    final_cal(a, b, c, P, V)

def my_cone(P, V, par):
    print("Cone with a {0:d} degree angle".format(par))
    print("Line passing through the point ({0:d}, {1:d}, {2:d}) "\
          "and parallel to the vector ({3:d}, {4:d}, {5:d})".format(P.x, P.y, P.z, V.x, V.y, V.z))
    a = m.pow(V.x, 2) + m.pow(V.y, 2) - (m.pow(V.z, 2) * m.pow(m.tan(m.radians(par)), 2))
    b = (2 * P.x * V.x) + (2 * P.y * V.y)  - ((2 * P.z * V.z) * m.pow(m.tan(m.radians(par)), 2))
    c = m.pow(P.x, 2) + m.pow(P.y, 2) - ((m.pow(P.z, 2) * m.pow(m.tan(m.radians(par)), 2)))
    final_cal(a, b, c, P, V)

    
