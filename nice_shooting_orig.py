#!/usr/bin/env python3

import random


#Defining Game 
def game(scenario,chance):
	x=random.random()
	if chance > x:
		print (scenario)
	
#Scenarios, Probabilities
bad_shooting = game("We shoot really badly.", 0.50) 
good_shooting = game("We shoot really well.", 0.50) 
bad_defense = game("Their defense sucks.", 0.60)

#Mutually Exclusive Events
bool (bad_shooting) ^ bool (good_shooting)
