import random
import sys
import numpy
from math import *

def main():
    moredev()



def moredev(): # Need to add calculations for angles in here
    devnumber = 0
    # First device code
    while True:
        try:
            additionaldev = input("Would you like to add another device? (y/n): ")
            if additionaldev == "y":
                devnumber += 1
                while True:
                    try:
                        additangle1 = int(input(f"What is the angle of additional device #{devnumber}?: "))
                        break
                    except ValueError:
                        continue
                while True:
                    try:
                        additionaldev2 = input("Would you like to add another device? (y/n): ")
                        if additionaldev2 == "y":
                            devnumber += 1
                            while True:
                                try:
                                    additangle2 = int(input(f"What is the angle of additional device #{devnumber}?: "))
                                    return devnumber, additangle1, additangle2
                                except ValueError:
                                    continue


                        elif additionaldev2 == "n":
                            break
                        else:
                            pass
                    except ValueError:
                        pass
                break
            elif additionaldev == "n":
                break
            else:
                pass
        except ValueError:
            continue

if __name__ == "main":
    main()