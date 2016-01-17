#!/usr/bin/env python3
""" Implement rock paper scissors in python3. Use few lines. """
__author__ = 'u/i_can_haz_code'
import random
choices = ['rock','paper','scissors']
beats = {'rock':'scissors','scissors':'paper','paper':'rock'}
def user_choice():
	""" Gets the user choice. If it is invalid. Raise a ValueError """
	choice = input('Please choose one of the following {} {} {} : '.format(choices[0],choices[1],
		choices[2])).lower()
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
	if beats[computer] == user:
		print('Computer wins {}  to {}'.format(computer,user))
	if beats[user] == computer:
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