# Stern-Gerlach
Stern-Gerlach experiment simulation

This code is intended to simulate the Stern-Gerlach experiment in quantum mechanics.
The code works by capturing user input for the number of particles to be sent through the device,
and the angle from the z-axis of the first device. The program then prompts the user if they would like
to add additional, connected devices, and the angles of these devices.

Then, the probability of the particles exiting the top and bottom channels of the device are calculated. 

These probabilities are multiplied by the particle amount. This amount is then used in the computation of the states for subsequent devices, to be added by the user. 
Linear algebra is used to calculate the probability that a specific eigenvector collapses to eigenstate inputted by the user.

The Stern-Gerlach experiment is foundational to the formulation of the idea of spin and the quantization of angular momentum in quantum mechanics.

