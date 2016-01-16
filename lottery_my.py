#!/usr/bin/env python

__author__ = 'u/i_can_haz_code'

import random


class Lottery(object):
	"""
	Lottery class to handle things to do.
	"""
	def __init__(self):
		try:
			self.wanttowatch = raw_input('Do you want to watch it work for a winner? (y/n)  ').lower()
			self.feelinglucky = raw_input('do you want some winning numbers? (y/n):  ').lower()
			self.showmenow =raw_input('Do you want to see your guess compared to the winner (y/n):  ').lower()
			self.bestguess = int(raw_input('Enter in a whole number between 1 and 292000000: ' ))
			if self.bestguess > 292000000:
				self.bestguess = random.choice(range(292000000))
			self.powerballlist = []
		except Exception as e:
			print('User input error. {}'.format(e))
			exit()
		return

	def powerballpicker(self):
	    pb =  random.randint(1,27)
	    return pb

	def numbergenerator(self,inti):
		if inti <= 69:
			if inti not in self.powerballlist:
				self.powerballlist.append(inti)
			else:
				pass
		else:
			z = random.randrange(1,70)
			self.powerballlist.append(z)
		return(self.powerballlist)

	def draw_numbers(self):
		self.cur = random.sample(range(1,70),4)
		self.cur.append(random.choice(range(27)))


	def powerballvalidation(self):
		lenlist = len(self.powerballlist)    
		while lenlist <5:
			generated = random.randrange(1,70)
			if generated not in powerballlist :
				self.powerballlist.append(generated)
				lenlist = lenlist + 1
			else :
				lenlist = lenlist
		return (lenlist)
	def run_sim(self):
		self.draw_numbers()
		if self.cur == self.powerballlist:
			print('Winner Found!!!!! {}'.format(self.powerballlist))
		else:
			print('Nope.... damn... {}'.format(self.cur))

lottery = Lottery()

print(lottery.powerballpicker())
for i in range(5):
	lottery.numbergenerator((2**i)%69)
print(lottery.powerballvalidation())
print('My numbers are: {}'.format(lottery.powerballlist))


for i in range(int(raw_input('how many tickets do you buy?'))):
	lottery.run_sim()
