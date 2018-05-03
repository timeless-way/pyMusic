'''
Note numbers
'''

def octaves(start, number=7):
	return list(range(start, start+(12*number)+1, 12))

c = octaves(23)
c_sharp = d_flat = octaves(24)
d = octaves(25)
d_sharp = e_flat = octaves(26)
e = octaves(27)
f = octaves(28)
f_sharp = g_flat = octaves(29)
g = octaves(30)
g_sharp = a_flat = octaves(31)
a = octaves(32)
a_sharp = b_flat = octaves(33)
b = octaves(34)

'''
program change numbers, to select instruments
use midiFile.addProgramChange(track, channel, time, program)
'''

Acoustic_Grand_Piano = 0
Bright_Acoustic_Piano = 1
Harpsichord = 6
Clavi = 7
Celesta = 8
Glockenspiel = 9
Music_Box = 10
Vibraphone = 11
Marimba = 12
Xylophone = 13
Tubular_Bells = 14

Seashore = 122
Bird_Tweet = 123
Telephone_Ring = 124
Helicopter = 125
Applause = 126
Gunshot = 127

'''
percussion instruments, use on channel 9
'''

Acoustic_Bass_Drum = 34
Bass_Drum_1 = 35
Side_Stick = 36
Acoustic_Snare = 37
Hand_Clap = 38
Electric_Snare = 39
Low_Floor_Tom = 40
Closed_Hi_Hat = 41
High_Floor_Tom = 42
Pedal_Hi_Hat = 43
Low_Tom = 44
Open_Hi_Hat = 45
Low_Mid_Tom = 46
Hi_Mid_Tom = 47
Crash_Cymbal_1 = 48
High_Tom = 49
Ride_Cymbal_1 = 50
Chinese_Cymbal = 51
Ride_Bell = 52
Tambourine = 53
Splash_Cymbal = 54
Cowbell = 55
Crash_Cymbal_2 = 56
Vibraslap = 57
Ride_Cymbal_2 = 58
Hi_Bongo = 59
Low_Bongo = 60
Mute_Hi_Conga = 61
Open_Hi_Conga = 62
Low_Conga = 63
High_Timbale = 64
Low_Timbale = 65
High_Agogo = 66
Low_Agogo = 67
Cabasa = 68
Maracas = 69
Short_Whistle = 70
Long_Whistle = 72
Short_Guiro = 73
Long_Guiro = 74
Claves = 75
Hi_Wood_Block = 76
Low_Wood_Block = 77
Mute_Cuica = 78
Open_Cuica = 79
Mute_Triangle = 80
Open_Triangle = 81
