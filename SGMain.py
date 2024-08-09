from math import *
import random
import numpy as np

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

    @staticmethod
    def angle_calc(angle1):
        rad_angle1 = angle1 * pi / 180
        return rad_angle1

    def first_device(self, rad_angle1, amount):

        prob_top = np.abs(np.cos(rad_angle1 / 2)) ** 2
        prob_bot = 1 - prob_top
        top_prob = round(prob_top * amount)
        bot_prob = amount - top_prob
        return top_prob, bot_prob

#######################
# More device classes #
#######################
def dev_number(devnum):
    return devnum

class Devices:
    def __init__(self, device):
        self.angles = []
        self.angle = None
        if device not in ['y', 'n']:
            raise ValueError('Must be either "y" or "n"')
        self.device = device

    def dev_number(devnum):
        return devnum

    def angle_calc(self, angle):
        self.angle = angle
        rad_angle = angle * pi / 180
        self.angles.append(rad_angle)

def moredev():
    global angle
    devices = []
    devnum = 0
    while True:
        try:
            d = Devices(input('Would you like to add another device? (y/n) ').lower().strip())
            if d.device == 'y':
                devices.append(d)
                devnum = dev_number(devnum)
                devnum += 1
            elif d.device == 'n':
                break

            while True:
                try:
                    angle = int(input(f'What is the angle of additional device #{devnum}, in degrees? '))
                    d.angle_calc(angle)
                    break
                except ValueError:
                    print('Invalid input, please enter an integer for the angle.')

        except ValueError as e:
            print(f'Invalid input: {e}')

    print(f'Total number of additional devices: {devnum}')
    return devices


def lin_alg(rad_angle1, devices, top_prob, bot_prob):
    # Initial state for particles after passing through the first SG device
    state_top_channel1 = np.array([[np.cos(rad_angle1 / 2)], [np.sin(rad_angle1 / 2) * 1j]])
    state_bot_channel1 = np.array([[np.sin(rad_angle1 / 2)], [-np.cos(rad_angle1 / 2) * 1j]])

    # Probabilities for the particles after passing through additional devices
    for i, device in enumerate(devices):
        # Calculate the state vectors for the next device angle
        state_device_top = np.array([[np.cos(device.angles[0] / 2)], [np.sin(device.angles[0] / 2) * 1j]])
        state_device_bot = np.array([[np.sin(device.angles[0] / 2)], [-np.cos(device.angles[0] / 2) * 1j]])

        # Calculate projection probabilities
        prob_top_given_top = np.abs(np.dot(np.conj(state_top_channel1.T), state_device_top)) ** 2
        prob_bot_given_top = np.abs(np.dot(np.conj(state_top_channel1.T), state_device_bot)) ** 2
        prob_top_given_bot = np.abs(np.dot(np.conj(state_bot_channel1.T), state_device_top)) ** 2
        prob_bot_given_bot = np.abs(np.dot(np.conj(state_bot_channel1.T), state_device_bot)) ** 2

        # Update probabilities for the next device
        new_top_prob = top_prob * prob_top_given_top + bot_prob * prob_top_given_bot
        new_bot_prob = top_prob * prob_bot_given_top + bot_prob * prob_bot_given_bot

        # Display the calculated probabilities for this step
        print(f"Device #{i + 2}: Top -> {round(new_top_prob[0, 0]):.4f}, Bottom -> {round(new_bot_prob[0, 0]):.4f}")


        # Update the probabilities for the next iteration
        top_prob = new_top_prob[0, 0]
        bot_prob = new_bot_prob[0, 0]


def main():
    global rad_angle1
    while True:
        try:
            amount = int(input("How many random spin 1/2 particles?: "))
            i_p = Particles(amount)
            angle1 = int(input("What is the angle of the SG device, in degrees?: "))
            rad_angle1 = i_p.angle_calc(angle1)  # Performs degrees to radians conversion in the class
            top_prob, bot_prob = i_p.first_device(rad_angle1, amount)  # Performs class calculations
            devices = moredev()  # Calls the function for more devices
            print(f"Device #1: Top -> {top_prob}, Bottom -> {bot_prob}")
            lin_alg(angle1, devices, top_prob, bot_prob)  # Call lin_alg with required parameters
            break
        except ValueError:
            print("Invalid input: Must be an integer.")
            continue

if __name__ == '__main__':
    main()
