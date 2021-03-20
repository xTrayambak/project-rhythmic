"""
MAIN PACKAGES
"""

import os # OS module
import json # JSON parser
import base64 # Base64 encoder and decoder

"""
Code begins from here.
"""


class Savedata(object):
	def __init__(self, levels, name, experiencePoints):
		self.exp = experiencePoints
		self.level = levels
		self.name = name

	def _send(self):
		return {'level': self.level, 'experiencePoints': self.exp, 'name': self.name}

class methods:
	def get_save_file(profile: int):
		with open('saves/save.rhythm'.format(profile), 'r') as f:
			myfile = json.load(f)
			name = myfile[str(profile)]['name']
			exp = myfile[str(profile)]['experience']
			levels = myfile[str(profile)]['levels']


			save = Savedata(levels=levels, experiencePoints=exp, name=name)
			_save = save._send()
			print("name is {}, levels is {}, experience is {}".format(_save['name'], _save['level'], _save['experiencePoints']))
			return save

methods.get_save_file(1)