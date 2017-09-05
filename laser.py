#!/usr/local/bin/python3
import math
# inputs: PUMP - power of device, frequency
pump_power = int(input("Power of the pump in Watt	:"));
pump_freq  = int(input("Frequency of pump(10E15Hz)	:"));
# input	: transperancy of mirror
mir_trans  = int(input("Enter transperancy of mirror(in percentage)	:"));
mir_trans = mir_trans/100;
#input	: lenght of laser tube, radius of tube
len	   = float(input("Distance btw mirrors	:"));
radius     = float(input("Radius of the cylinder	:"));

#input	: number of atoms:
atoms	   = int(input("Enter number of atoms	:"));
#input	: parameters of atoms:
hlf_life   = float(input("Half life of meta stable state	:"));
band_gp	   = float(input("Bandgap btw E_c and E_v	:"));

#To be calculated (trivial)
ambient_photons = pump_power/(6.626E-19 * pump_freq);
density	   = atoms/len/radius**2/math.pi
density_ambient = ambient_photons / len/radius**2/math.pi
decay_const = 0.693/hlf_life
if ambient_photons > atoms:
	percentage_interaction = 1
else:
	percentage_interaction = ambient_photons/atoms

#variables to be calculated in simulation
photon_direction = [0]*360;

