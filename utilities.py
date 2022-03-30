import pygame

import math


def inrange(loc1, loc2, max_distance):
    distance = math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    return distance < max_distance
