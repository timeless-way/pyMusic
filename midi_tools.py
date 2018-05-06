import midiutil as util
import sound

class Musicule:
	
	def __init__(self, duration=0):
		self.duration = duration
	
class Note(Musicule):
	
	def __init__(self, pitch=59, volume=90, duration=1, legato=1.0, channel=None):
		super().__init__(duration)
		self.pitch = pitch
		self.volume = volume
		self.legato = legato
		self.channel = channel
	
	def set_channel(self, channel):
		self.channel = channel
	
	def play(self, tape):
		start_time = tape.time
		legato_duration = self.legato * self.duration
		tape.add_note(self.channel, self.pitch, start_time, legato_duration, self.volume)
		tape.time += self.duration

class Rest(Musicule):
	
	def __init__(self, duration=1):
		super().__init__(duration)
	
	def set_channel(self, channel):
		pass
		
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
	
	def set_channel(self, channel):
		for m in self.musicules:
			m.set_channel(channel)
	
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
	
	def set_channel(self, channel):
		for m in self.musicules:
			m.set_channel(channel)
	
	def play(self, tape):
		time = tape.time
		for m in self.musicules:
			m.play(tape)
			tape.time = time
		tape.time = time + self.duration

class Instrument(Musicule):
	
	def __init__(self, channel, instrument):
		super().__init__()
		self.instrument = instrument
		self.channel = channel
	
	def set_channel(self, channel):
		self.channel = channel
	
	def play(self, tape):
		tape.change_instrument(self.channel, self.instrument)

class Tempo(Musicule):
	
	def __init__(self, tempo):
		super().__init__()
		self.tempo = tempo
	
	def set_channel(self, channel):
		pass
	
	def play(self, tape):
		tape.set_tempo(self.tempo)

class Channel(Musicule):
	
	def __init__(self, channel):
		super().__init__()
		self.channel = channel
	
	def set_channel(self, channel):
		pass
	
	def play(self, tape):
		tape.channel = self.channel
		
class Track(Musicule):
	
	def __init__(self, track):
		super().__init__()
		self.track = track
	
	def set_channel(self, channel):
		pass
	
	def play(self, tape):
		tape.current_track = self.track
		
class Midi_tape:
	
	def __init__(self, name, track=0, channel=0, numTracks=1):
		self.midi_file = util.MIDIFile(numTracks, adjust_origin=False)
		self.name = name
		self.current_track = track
		self.channel = channel
		self.time = 0
	
	def add_note(self, channel, pitch, time, duration, volume):
		chan = channel if channel else self.channel
		self.midi_file.addNote(track=self.current_track, channel=chan, 
		pitch=pitch, time=time, duration=duration, volume=volume)
	
	def set_tempo(self, tempo=60, time=-1):
		if time == -1:
			time = self.time
		self.midi_file.addTempo(self.current_track, time, tempo)
		
	def change_instrument(self, channel, instrument):
		chan = channel if channel else self.channel
		self.midi_file.addProgramChange(self.current_track, chan, self.time, instrument)
		
	def save(self):
		with open(self.name + '.mid', 'wb') as output_file:
			self.midi_file.writeFile(output_file)
	
	def play(self):
		self.save()
		player = sound.MIDIPlayer(self.name + '.mid')
		player.play()
		while player.current_time < player.duration+1:
			pass
		player.stop()

def perform(musicule, tape=None):
	if not tape:
		tape = Midi_tape('temp')
	musicule.play(tape)
	tape.play()
	return tape
