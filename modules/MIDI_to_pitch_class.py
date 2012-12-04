#!/usr/bin/env python
# Owner: <your name> (<your email>)
# Summary: takes a list of MIDI chords and outputs the list of pitch class set classes,
# and their corresponding octaves

from module import *

class MIDIToPitchClass(Module):
        
    def generate_output(self):
        #obtain list of MIDI values as chords (i.e., lists)
        MIDIChords = self.get_input("in0")
        #obtain "base" note which will be labeled 0 in every octave in MIDI form
        MIDIBase = self.get_input("in1")

        pitch_classes = []
        octaves = []
        for chord in MIDIChords:
            pitch_classes.append([(note-MIDIBase)%12 for note in chord])
            octave.append([int(round(note-MIDIBase/12)) for note in chord])

        #Once processing is complete, set the output(s) of the module by calling self.set_output(<output>, <output port>)
        self.set_output(pitch_classes, "out0")
        self.set_output(octaves, "out1")
