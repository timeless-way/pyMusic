'''
Note numbers
'''

def octaves(start, number=7):
	return list(range(start, start+(12*number)+1, 12))

key_nr = 23
c = octaves(key_nr)
c_sharp = d_flat = octaves(key_nr+1)
d = octaves(key_nr+2)
d_sharp = e_flat = octaves(key_nr+3)
e = octaves(key_nr+4)
f = octaves(key_nr+5)
f_sharp = g_flat = octaves(key_nr+6)
g = octaves(key_nr+7)
g_sharp = a_flat = octaves(key_nr+8)
a = octaves(key_nr+9)
a_sharp = b_flat = octaves(key_nr+10)
b = octaves(key_nr+11)

'''
program change numbers, to select instruments
use midiFile.addProgramChange(track, channel, time, program)
Note the off-by-one error that is inherent in the spec!
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
Dulcimer = 15
Drawbar_Organ = 16
Percussive_Organ = 17
Rock_Organ = 18
Church_Organ = 19
Reed_Organ = 20
Accordion = 21
Harmonica = 22
Tango_Accordion = 23
Acoustic_Guitar_nylon = 24
Acoustic_Guitar_steel = 25
Electric_Guitar_jazz = 26
Electri_Guitar_clean = 27
Electric_Guitar_muted = 28
Overdriven_Guitar = 29
Distortion_Guitar = 30
Guitar_harmonics = 31
Acoustic_Bass = 32
Electric_Bass_finger = 33
Electric_Bass_pick = 34
Fretless_Bass = 35
Slap_Bass_1 = 36
Slap_Bass_2 = 37
Synth_Bass_1 = 38
Synth_Bass_2 = 39
Violin = 40
Viola = 41
Cello = 42
Contrabass = 43
Tremolo_Strings = 44
Pizzicato_Strings = 45
Orchestral_Harp = 46
Timpani = 47
String_Ensemble_1 = 48
String_Ensemble_2 = 49
SynthStrings_1 = 50
SynthStrings_2 = 51
Choir_Aahs = 52
Voice_Oohs = 53
Synth_Voice = 54
Orchestra_Hit = 55
Trumpet = 56
Trombone = 57
Tuba = 58
Muted_Trumpet = 59
French_Horn = 60
Brass_Section = 61
SynthBrass_1 = 62
SynthBrass_2 = 63
Soprano_Sax = 64
Alto_Sax = 65
Tenor_Sax = 66
Baritone_Sax = 67
Oboe = 68
English_Horn = 69
Bassoon = 70
Clarinet = 71
Piccolo = 72
Flute = 73
Recorder = 74
Pan_Flute = 75
Blown_Bottle = 76
Shakuhachi = 77
Whistle = 78
Ocarina = 79
Lead_1_square = 80
Lead_2_sawtooth = 81
Lead_3_calliope = 82
Lead_4_chiff = 83
Lead_5_charang = 84
Lead_6_voice = 85
Lead_7_fifths = 86
Lead_8_bass_and_lead = 87
Pad_1_new_age = 88
Pad_2_warm = 89
Pad_3_polysynth = 90
Pad_4_choir = 91
Pad_5_bowed = 92
Pad_6_metallic = 93
Pad_7_halo = 94
Pad_8_sweep = 95
FX_1_rain = 96
FX_2_soundtrack = 97
FX_3_crystal = 98
FX_4_atmosphere = 99
FX_5_brightness = 100
FX_6_goblins = 101
FX_7_echoes = 102
FX_8_sci_fi = 103
Sitar = 104
Banjo = 105
Shamisen = 106
Koto = 107
Kalimba = 108
Bag_pipe = 109
Fiddle = 110
Shanai = 111
Tinkle_Bell = 112
Agogo = 113
Steel_Drums = 114
Woodblock = 115
Taiko_Drum = 116
Melodic_Tom = 117
Synth_Drum = 118
Reverse_Cymbal = 119
Guitar_Fret_Noise = 120
Breath_Noise = 121
Seashore = 122
Bird_Tweet = 123
Telephone_Ring = 124
Helicopter = 125
Applause = 126
Gunshot = 127

'''
percussion instruments, use on channel 9. 
Note, there is NO off-by-one error in this part of the spec. 
'''

Acoustic_Bass_Drum = 35
Bass_Drum_1 = 36
Side_Stick = 37
Acoustic_Snare = 38
Hand_Clap = 39
Electric_Snare = 40
Low_Floor_Tom = 41
Closed_Hi_Hat = 42
High_Floor_Tom = 43
Pedal_Hi_Hat = 44
Low_Tom = 45
Open_Hi_Hat = 46
Low_Mid_Tom = 47
Hi_Mid_Tom = 48
Crash_Cymbal_1 = 49
High_Tom = 50
Ride_Cymbal_1 = 51
Chinese_Cymbal = 52
Ride_Bell = 53
Tambourine = 54
Splash_Cymbal = 55
Cowbell = 56
Crash_Cymbal_2 = 57
Vibraslap = 58
Ride_Cymbal_2 = 59
Hi_Bongo = 60
Low_Bongo = 61
Mute_Hi_Conga = 62
Open_Hi_Conga = 63
Low_Conga = 64
High_Timbale = 65
Low_Timbale = 66
High_Agogo = 67
Low_Agogo = 68
Cabasa = 69
Maracas = 70
Short_Whistle = 71
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
