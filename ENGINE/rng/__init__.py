import random
import keyboard
import time

class properties:
	restart_key = 'R'

class o:
	def sub(a, b):
		return a - b

	def add(a, b):
		return a + b

	def mult(a, b):
		return a * b

	def div(a, b):
		try:
			return a / b
		except ZeroDivisionError:
			return a * b / 1


class PRNG():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c


		self.operationTranslate = {'mult': o.mult, 'div': o.div, 'add': o.add, 'sub': o.sub}
		self.operations = ['mult', 'div', 'add', 'sub']
		self.nos = [self.a, self.b, self.c]
		self.types = {'int': int, 'float': float, 'str': str}

	def _change(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def _gen(self, res, max_size):
		result = 0 # max calculated
		final_result = 0 # limited
		for x in range(random.choice(self.nos)):
			extraNo = x * self.c * 2 or x / self.c * 2
			op_tab = random.choice(self.operations)

			if extraNo < 1:
				result += x * self.operationTranslate[op_tab](x * random.choice(self.nos) * random.choice(self.nos) * self.c, random.choice(self.nos))
			elif extraNo > 1:
				result += self.operationTranslate[op_tab](random.choice(self.nos) * random.choice(self.nos), random.randrange(-10, 45))


		return self.types[res](result)

		
e = PRNG(a=30, b=43, c=9)
while True:
	if keyboard.is_pressed(properties.restart_key):
		a = random.randint(1,50) 
		b=random.randint(1,100)
		c=random.randint(1,150)
		e._change(a=a, b=b, c=c)
		print(e._gen(res='int', max_size=3))
		time.sleep(0.2)