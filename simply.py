#!/usr/local/bin/python3
import matplotlib.pyplot as plt
atoms  = 10E5
pump   = 1.4E-3
decay  = 0.01
mirror= 0.99

#first graph (purple)
photon = 0
inverted = 0.0
list = []
list1 = []
for x in range(0,10000):
	inverted += pump

	spon = inverted*decay
	inverted -= spon
	photon += spon * atoms

	list.append(photon*(1-mirror))
	photon *= mirror
	
	gain = 2*inverted
	photon *= gain
	inverted -= (gain-1)*photon/atoms
	list1.append(inverted)

plt.plot(list)

#second green
pump   = 1.3E-3
decay  = 0.01
mirror= 0.99

photon = 0
inverted = 0.0
list = []
list1= []
for x in range(0,10000):
	inverted += pump

	spon = inverted*decay
	inverted -= spon
	photon += spon * atoms

	list.append(photon*(1-mirror))
	photon *= mirror
	
	gain = 2*inverted
	photon *= gain
	inverted -= (gain-1)*photon/atoms
	list1.append(inverted)


plt.plot(list)
plt.show()
