#!/usr/bin/env python

"""
This is a simple implementation of Rock, Paper, Scissors, Spock, Lizard. Ported to python 2
"""
import random

__author__ = 'u/i_can_haz_code'

choices = ['rock','paper','scissors','spock','lizard'] # List of choices is not really necessary as we could use beats.keys()
beats = {'rock':['scissors', 'lizard'], 'paper': ['rock', 'spock'], 'scissors': ['paper','lizard'], 
'spock':['scissors','rock'], 'lizard': ['spock','paper']} # using lists as the values for this dictionary allows us to not have to write crazy stuff later.
def user_choice():
	""" Gets the user choice. If it is invalid. Raise a ValueError """
	choice = raw_input('Please choose one of the following {} {} {} {} {} : '.format(*choices)).lower()
	if choice in choices:
		return (choice)
	else:
		print('invalid option selected. {} '.format(choice))
		raise (ValueError)
def computer_choice():
	""" This function arguably only exists for readability later on... """
	return(random.choice(choices))
def compare(user,computer):
	""" Figure out who wins. """
	if user == computer:
		print('Draw user chose: {} computer chose: {}'.format(user,computer))
	if user in beats[computer] :
		print('Computer wins {}  to {}'.format(computer,user))
	if computer in beats[user] :
		print('User wins {}  to {}'.format(user,computer))
def game():
	""" Play one game. """
	canary = 0
	while canary != 1:
		try:
			uc = user_choice()
			canary = 1
		except ValueError:
			pass
	cc = computer_choice()
	compare(uc,cc)
if __name__ == '__main__':
	game()
