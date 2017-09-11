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
len/=100
radius     = float(input("Radius of the cylinder(cm)	:"));
radius/=100
#input	: number of atoms:
atoms	   = float(input("Enter number of atoms	:"));
#input	: parameters of atoms:
hlf_life   = float(input("Half life of meta stable state(s)	:"));
band_gp	   = float(input("Bandgap btw E_c and E_v(eV)	:"));

#To be calculated (trivial)
ambient_photons = pump_power/(6.626E-34 * pump_freq*1E15);
density	   = atoms/len/radius**2/pi 
density_ambient = ambient_photons / atoms
decay_const= 0.693/hlf_life
freq_laser = band_gp*1.6E-19 / 6.626E-34
time_period= 2 * len/ 3E8	#one iteration of simulation
ambient_photons *= time_period	#photons in one round
density_ambient *= time_period	#same reason
if ambient_photons > atoms:
	percentage_interaction = 1
else:
	percentage_interaction = ambient_photons/atoms

#variables to be calculated in simulation
print(ambient_photons)
photon_direction= [0.0]*360;	
#if laser angle is r/l then we split r/l into 360 parts and 
#find photon intensity in each part ignoring the rest

photon_phase	= [0.0]*360;
#We count photons in each phase (taking phase in discrete unit of degrees).
inverted= 0.5
ground	= 0.5
print(decay_const)
#infinite loop for simulation
while True:
	#Excitation due to pump
	inverted+= density_ambient;
	if inverted > 1 : inverted = 1;
	if inverted < 0 : inverted = 0;
	#spontaneous emission of exicited atoms
	spon	 = inverted*(1 -  e**(-time_period*decay_const) )
	inverted -= spon;
	ground 	 = 1 - inverted
	spon *= atoms #till now we were considering ratios
	#spontaneous emission goes into each phase equally
	effective_spon = spon*radius/len/(2*pi);
	#gives those photons which are still in the medium after one round.

	photon_phase = list(np.asarray(photon_phase) + effective_spon/360)
	photon_direction = list(np.asarray(photon_direction) + effective_spon/360) 
	#phtons go randomly to each phase (spontaneous emmission) and direction
	intensity_at_mirror=0;
	for i in range(0,360):
		photon_phase[i] = photon_phase[i] * mir_trans 
		photon_direction[i] = photon_direction[i] * mir_trans 
		intensity_at_mirror += photon_phase[i]*(1-mir_trans)
	#Loss through mirror
	percentage_loss = 0;
	total = 0
	for i in range(0,360):
		total += photon_direction[i];
		percentage_loss += photon_direction[i]*(i/360)  #paraxial approximation
		photon_direction[i] = photon_direction[i] * (1- i/360) 
	percentage_loss /= total;
	#We now assume that each phase looses equally
	photon_phase = list(np.asarray(photon_phase) * percentage_loss)

	#finally the stimulated part:
	#one problematic thing is we are not isolating one phase, but treating all phases as equal
	#however the laser light is generally in phase
	#this is one approximation we had to do, due mainly to lack of expertise, and time.
	if inverted < 0.5:
		gain = 2*inverted
	else:
		gain = (inverted-0.5)* 5 + 1
	photon_phase 	 = list(np.asarray(photon_phase)    * gain)
	photon_direction = list(np.asarray(photon_direction)* gain)
	sum_phase = sum(photon_phase)
	sum_direction = sum(photon_direction)
	print('total photons :',sum_direction);
	print('inverted pop  :',inverted	);
	max_direction = max(photon_direction)
	inverted -= (sum_direction )/atoms
	print("inverted : ",inverted,"\tsum_direction :",sum_direction,"\tatoms : ",atoms)
	#mir_trans = mir_trans* (15/log(sum_direction));
	input("Press enter to go to next round");

