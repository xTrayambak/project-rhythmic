import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')


def play(file: str):
	source = pyglet.media.StaticSource(pyglet.media.load(file))

	player = pyglet.media.Player()
	player.queue(source)
	player.EOS_LOOP = 'loop'
	player.play()

play('ASSETS/SONGS/pv_001.ogg')