import math

# This code is for adding extra devices
# Challenge is associating angle with device number
# Devices will be zero ordered

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
        rad_angle = angle * math.pi / 180
        self.angles.append(rad_angle)


def moredev():
    devices = []
    devnum = 0
    while True:
        try:
            d = Devices(input('Would you like to add another device? (y/n) '))
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

    # Print the list of radian angles for each device
    for i, device in enumerate(devices):
        print(f'Additional Device #{i+1} radian angles: {device.angles}')

