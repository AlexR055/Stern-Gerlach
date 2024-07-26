import random
import sys
import numpy
from math import *
from SGadditionaldevices import main

devnumber = 0 # Keeps track of number of devices
additangle1 = 0
additangle2 = 0

## Probabilities

# Enters number of particles
while True:
    try:
        particles = int(input("How many random spin 1/2 particles?: ")).strip().lower()

        if particles > 100000:
            print("Too many random spin 1/2 particles! Must be 100000 or less.")
            continue
        else:
            while True:
                try:
                    angle = int(input("What is the angle in degrees?: ")).strip()
                    break
                except ValueError:
                    pass
    except ValueError:
        continue


    break

# Call main
main()

radangle = angle * pi / 180  # Converts angle to radians
upper = (particles*((cos(radangle/2))**2))
lower = (particles*((sin(radangle/2))**2))
# Creates the random element for particle distribution
randupper = random.randint((round(upper)-random.randint(1,100)),round(upper)+random.randint(1,100))
randlower = particles-randupper

# Ensures that neither var is negative
while randlower > particles or randupper > particles:
    randupper = random.randint((round(upper) - random.randint(1, 100)), round(upper) + random.randint(1, 100))
    randlower = particles - randupper

# Additional devices # Can probably condense all of this to a for loop

# 1 Additional Device
if devnumber == 1:
    radangle1 = additangle1*pi/180
    upper1 = randupper*(cos(radangle1/2)**2)
    lower1 = randlower*(sin(radangle1/2)**2)
    print(
        f"Upper channel: {round(upper1)}, Lower channel: {round(lower1)}, Total: {round(upper1 + lower1)}")

# 2 Additional Devices
elif devnumber == 2:
    radangle1 = additangle1 * pi / 180
    radangle2 = additangle2* pi / 180
    upper1 = randupper * (cos(radangle1 / 2) ** 2)
    lower1 = randlower * (sin(radangle1 / 2) ** 2)
    upper2 = upper1 * (cos(radangle2 / 2))**2
    lower2 = lower1 * (sin(radangle2 / 2))**2
    print(
        f"Upper channel: {round(upper2)}, Lower channel: {round(lower2)}, Total: {round(upper2 + lower2)}")

# No additional devices
elif devnumber == 0:
    print(
        f"Upper channel: {round(randupper)}, Lower channel: {round(randlower)}, Total: {round(randupper + randlower)}")










