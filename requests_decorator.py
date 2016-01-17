#!/usr/bin/env python3


"""
Make a simple decorator to log cookies if they exist.
"""
import functools
import requests

def decorator(func,*args,**kwargs):
	@functools.wraps(func)
	def inner(*args,**kwargs):
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
	r = requests.get(url)
	return(r)

if __name__ == '__main__':
	print(get_request('https://www.google.com/?gws_rd=ssl'))
