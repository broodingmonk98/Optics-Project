#!/usr/local/bin/python3
from math import *
import numpy as np
# inputs: PUMP - power of device, frequency
pump_power = float(input("Power of the pump in Watt	:"));
pump_freq  = float(input("Frequency of pump(10E15Hz)	:"));
# input	: transperancy of mirror
mir_trans  = float(input("Transperancy of mirror(0-1)	:"));
#input	: lenght of laser tube, radius of tube
len	   = float(input("Distance btw mirrors(cm)	:"));
radius     = float(input("Radius of the cylinder(cm)	:"));

#input	: number of atoms:
atoms	   = float(input("Enter number of atoms	:"));
#input	: parameters of atoms:
hlf_life   = float(input("Half life of meta stable state	:"));
band_gp	   = float(input("Bandgap btw E_c and E_v(eV)	:"));

#To be calculated (trivial)
ambient_photons = pump_power/(6.626E-19 * pump_freq);
density	   = atoms/len/radius**2/pi
density_ambient = ambient_photons / len/radius**2/pi
decay_const= 0.693/hlf_life
freq_laser = band_gp*1.6E-19 / 6.626E-34
time_period= 2 * len/ 3E10	#one iteration of simulation
ambient_photons *= time_period	#photons in one round
density_ambient *= time_period	#same reason
if ambient_photons > atoms:
	percentage_interaction = 1
else:
	percentage_interaction = ambient_photons/atoms

#variables to be calculated in simulation

photon_direction= [0.0]*360;	
#if laser angle is r/l then we split r/l into 360 parts and 
#find photon intensity in each part ignoring the rest

photon_phase	= [0.0]*360;
#We count photons in each phase (taking phase in discrete unit of degrees).
inverted= 0
ground	= 1

#infinite loop for simulation
while True:
	#Excitation due to pump
	inverted = ambient_photons;
	#spontaneous emission of exicited atoms
	spon	 = inverted*(1 -  e**(-time_period/decay_const) )
	inverted -= spon;
	ground 	 = 1 - inverted   ;
	#spontaneous emission goes into each phase equally
	effective_spon = spon*r/l/(2*pi);
	#gives those photons which are still in the medium after one round.

	photon_phase = list(np.asarray(photon_phase) + effective_spon/360)
	photon_direction = list(np.asarray(list1) + effective_spon/360) 
	#phtons go randomly to each phase (spontaneous emmission) and direction
	gain = 5 #TODO
	intensity_at_mirror=0;
	for i in range(0,360):
		photon_phase[i] = photon_phase[i] * transperancy
		photon_direction[i] = photon_direction[i] * transperancy
		intensity_at_mirror += photon_phase[i]*(1-transperancy)
	#Loss through mirror
	for i in range(0,360):
		photon_direction[i] = photon_direction[i] * (1- (i/360*l/r) 




