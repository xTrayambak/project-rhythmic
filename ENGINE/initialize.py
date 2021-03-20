import os

def firstrun():
	try:
		with open('FIRSTRUN') as e:
			return True
	except FileNotFoundError:
		return False