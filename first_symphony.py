#from midiutil import MIDIFile
import midi_constants as mc
import midi_tools as mt
import midiutil as midi
import sound

#degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
#degrees = [note for note in [mc.c[3]+i for i in [0,2,4,5,7,9,11,12]]]
degrees = mc.c
track    = 0
channel  = 0
time     = 0     # In beats
duration = 1.5   # In beats
tempo    = 400   # In BPM
volume   = 63    # 0-127, as per the MIDI standard

MyMIDI = midi.MIDIFile(1, adjust_origin=False)
# One track, defaults to format 1 (tempo track automatically created)

MyMIDI.addTempo(track,time,tempo)

MyMIDI.addProgramChange(track, channel, time, mc.Acoustic_Grand_Piano)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1
    
#MyMIDI.addProgramChange(track, channel, time, mc.Marimba)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

#MyMIDI.addProgramChange(track, channel, time, mc.Xylophone)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

#MyMIDI.addProgramChange(track, channel, time, mc.Tubular_Bells)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

#MyMIDI.addProgramChange(track, channel, time, mc.Music_Box)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    
player = sound.MIDIPlayer("major-scale.mid")
player.play()
#sound.play_effect('arcade:Laser_4')

