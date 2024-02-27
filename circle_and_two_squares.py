from math import sqrt

def square_areas_difference(r):
    return round((r*2)**2-(sqrt(r**2*2))**2)

print(square_areas_difference(6))