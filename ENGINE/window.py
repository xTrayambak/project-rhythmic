"""
PACKAGE IMPORTS - RENDERING BACKEND
"""
import pyglet
from pyglet.gl 		import *

FPS_CAP = 60

class Window(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)

		# WINDOW ELEMENTS (RENDERING)
		self.fps = int(pyglet.clock.get_fps())

		#UI ELEMENTS
		self.fps_counter = pyglet.text.Label('FPS: 0', font_name='Arial', font_size = 18,
			x=30, y=self.height - 10, anchor_x='left', anchor_y='top',
            color=(255, 0, 0, 255)
			)

		# DEBUG UI
		self.debug_ui = {'framerate': self.fps_counter}

		# LIST TO DRAW CONSISTENT GUI RENDER FUNCTIONS
		self.uiDrawCall = [self.draw_fps_label]

		### SCHEDULE LOGIC UPDATE SO ON_DRAW KEEPS GETTING CALLED
		pyglet.clock.schedule_interval(self.update, 1.0 / FPS_CAP)

	def draw_fps_label(self):
		self.debug_ui['framerate'].text = 'FPS: '+str(self.fps)
		if self.fps < 20:
			self.debug_ui['framerate'].color = (255, 0, 0, 255)
		elif self.fps > 38:
			self.debug_ui['framerate'].color = (0, 255, 0, 255)
		elif self.fps < 35:
			self.debug_ui['framerate'].color = (240, 228, 15, 255)
		self.debug_ui['framerate'].draw()



	def draw_ui(self):
		"""
		Render GUI elements
		"""
		for rendFunct in self.uiDrawCall:
			rendFunct()

	def refresh_fps(self):
		self.fps = int(pyglet.clock.get_fps())



	def update(self, dt):
		#TODO: Add game logic later
		pass

	def on_draw(self):
		"""
		Pyglet's standard draw call.
		"""
		self.refresh_fps()
		print("[Window]: Draw call at a rate of {}".format(self.fps))
		self.clear()
		self.draw_ui()
		glColor3d(1, 1, 1)

Window(width=1280, height=720, caption='CreativePlex', resizable=True)
pyglet.app.run()