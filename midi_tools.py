import midi_constants as mc

class Musicule:
	
	def __init__(self, beats=1, duration=1):
		self.beats = beats
		self.duration = duration
	
class Note(Musicule):
	
	def __init__(self, pitch=mc.c[3], volume=90, beats=1, duration=1):
		super().__init__(beats, duration)
		self.pitch = pitch
		self.volume = volume

class Rest(Musicule):
	
	def __init__(self, beats, duration):
		super().__init__(beats, duration)
