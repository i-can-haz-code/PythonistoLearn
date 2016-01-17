#!/usr/bin/env python3


"""
Make a simple decorator to log cookies if they exist.
"""
import functools
import requests

__author__ = 'u/i_can_haz_code'

def decorator(func,*args,**kwargs):
	""" Simple decorator to print cookies. Modify at will. """
	@functools.wraps(func)
	def inner(*args,**kwargs):
		""" Uses functools.wraps to keep from showing this in the help(func) """
		ret = func(*args,**kwargs)
		try:
			cookies = ret.cookies
			print(cookies)
			return(ret)
		except:
			return(ret)
	return(inner)

@decorator
def get_request(url):
	""" Sends a get request, and returns what comes back. """
	r = requests.get(url)
	return(r)

if __name__ == '__main__':
	print(get_request('https://www.google.com/?gws_rd=ssl'))
