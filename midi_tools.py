import midi_constants as mc
import midiutil as util
import sound

class Musicule:
	
	def __init__(self, duration=0):
		self.duration = duration
	
class Note(Musicule):
	
	def __init__(self, pitch=mc.c[3], volume=90, duration=1, legato=1.0):
		super().__init__(duration)
		self.pitch = pitch
		self.volume = volume
		self.legato = legato
	
	def play(self, tape):
		start_time = tape.time
		legato_duration = self.legato * self.duration
		tape.add_note(self.pitch, start_time, legato_duration, self.volume)
		tape.time = start_time + self.duration

class Rest(Musicule):
	
	def __init__(self, duration=1):
		super().__init__(duration)
		
	def play(self, tape):
		tape.time += self.duration

class Seq(Musicule):
	
	def __init__(self, *musicules):
		super().__init__()
		self. musicules = musicules
		duration = 0
		for m in musicules:
			duration += m.duration
		self.duration = duration
	
	def play(self, tape):
		for m in self.musicules:
			m.play(tape)

class Par(Musicule):
	
	def __init__(self, *musicules):
		super().__init__()
		self.musicules = musicules
		duration = 0
		for m in musicules:
			if m.duration > duration:
				duration = m.duration
		self.duration = duration
	
	def play(self, tape):
		time = tape.time
		for m in self.musicules:
			m.play(tape)
			tape.time = time
		tape.time = time + self.duration

class Instrument(Musicule):
	
	def __init__(self, instrument):
		super().__init__()
		self.instrument = instrument
	
	def play(self, tape):
		tape.change_instrument(self.instrument)

class Tempo(Musicule):
	
	def __init__(self, tempo):
		super().__init__()
		self.tempo = tempo
	
	def play(self, tape):
		tape.set_tempo(self.tempo)
		
class Midi_tape:
	
	def __init__(self, name, channel=0):
		self.midi_file = util.MIDIFile(1, adjust_origin=False)
		self.name = name
		self.channel = channel
		self.time = 0
	
	def add_note(self, pitch, time, duration, volume):
		self.midi_file.addNote(track=0, channel=self.channel, 
		pitch=pitch, time=time, duration=duration, volume=volume)
	
	def set_tempo(self, tempo=60, time=-1):
		if time == -1:
			time = self.time
		self.midi_file.addTempo(0, time, tempo)
		
	def change_instrument(self, instrument):
		self.midi_file.addProgramChange(0, self.channel, self.time, instrument)
		
	def save(self):
		with open(self.name + '.mid', 'wb') as output_file:
			self.midi_file.writeFile(output_file)
	
	def play(self):
		self.save()
		player = sound.MIDIPlayer(self.name + '.mid')
		print(self.name, player.duration)
		player.play()
		while player.current_time < player.duration+1:
			pass
		player.stop()
		print('Einde')

		
