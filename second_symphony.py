import midi_constants as mc
import midi_tools as mt
import midiutil as midi
import sound

def scale_up(pitches, volume, duration, legato):
	return mt.Seq(*[mt.Note(pitch, volume, duration, legato) for pitch in pitches])
	
def scale_down(pitches, volume, duration, legato):
	return mt.Seq(*[mt.Note(pitch, volume, duration, legato) for pitch in reversed(pitches)])

notes_1 = scale_up(range(mc.c[3], mc.c[4]), 63, 1, 0.4)
notes_2 = scale_down(range(mc.c[3], mc.c[4]), 32, 1, 1.5)

tempo300 = mt.Tempo(300)
tempo600 = mt.Tempo(600)
tubular_bells = mt.Instrument(mc.Tubular_Bells)
marimba = mt.Instrument(mc.Marimba)

etude = mt.Seq(tempo300, tubular_bells, notes_1, tempo600, marimba, notes_2)

tape = mt.Midi_tape("etude_1")
etude.play(tape)
tape.play()



