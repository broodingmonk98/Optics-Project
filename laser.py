#!/usr/local/bin/python3
import math
# inputs: PUMP - power of device, frequency
pump_power = int(input("Power of the pump in Watt	:"));
pump_freq  = int(input("Frequency of pump		:"));
# input	: transperancy of mirror
mir_trans  = int(input("Enter transperancy of mirror(in percentage)	:"));
mir_trans = mir_trans/100;
#input	: lenght of laser tube, radius of tube
len	   = int(input("Distance btw mirrors	:"));
radius     = int(input("Radius of the cylinder	:"));

#input	: number of atoms:
atoms	   = int(input("Enter number of atoms	:"));
density	   = atoms/len/radius**2/math.pi
#input	: parameters of atoms:
#TODO
print(density)
