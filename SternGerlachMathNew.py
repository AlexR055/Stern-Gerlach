from math import *
import numpy as np
from moredev import moredev

# Need to consider states collapsing for top and bottom
######################################################
# Library of eigenvectors in z-basis #
# |+z> = np.array([[1],[0]])
# |-z> = np.array([[0],[1]])
# |+x> = np.array([[np.sqrt(.5)],[np.sqrt(.5)]])
# |-x> = np.array([[np.sqrt(.5)],[(-1)*np.sqrt(.5)]])
# |+y> = np.array([[np.sqrt(.5)],[np.sqrt(.5)*1j]])
# |-y> = np.array([[np.sqrt(.5)*1j],[np.sqrt(.5)]])
# |+th> = np.array([[cos(angle/2)],[sin(angle/2)*1j]])
# |-th> = np.array([[cos(angle/2)*1j],[sin(angle/2)]])
######################################################

class Particles:
    def __init__(self, amount):
        self.angle1 = None
        self.rad_angledev1 = None
        if isinstance(amount, int):
            pass
        else:
            raise ValueError("Amount must be an integer.")
        self.amount = amount

    def angle_calc(self, angle1):
        self.angle1 = angle1
        rad_angle1 = angle1 * pi / 180
        return rad_angle1

    def linear_alg1(self, rad_angledev1):
        self.rad_angledev1 = rad_angledev1


...
...
...


def main():
    while True:
        try:
            i_p = Particles(int(input("How many random spin 1/2 particles?: ")))
            angle1 = int(input("What is the angle of the SG device, in degrees?: "))
            rad_angledev1 = i_p.angle_calc(angle1)  # Performs degrees to radians conversion in the class
            i_p.linear_alg1(rad_angledev1)  # Performs linear algebra calculations for first device
            break
        except ValueError:
            print(f"Invalid input: Must be an integer. ")
            continue
    moredev()  # Calls the function for more devices


if __name__ == '__main__':
    main()
