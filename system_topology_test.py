
# Owner: Class
# Summary: This is the configuration for a system that transposes
# a list of chords up two steps using two single step transpose modules in series
# Notes:

from modules import *

#======================================================
# initialize start and end
# start is a thru, ie. it passes in0 to out0, in1 to out1, etc...
# thus it must has same number of inputs as outputs
# NOTE: end has no outputs!
#======================================================

start = Start("Start", ["in0", "in1"], ["out0", "out1"])
end = End("End", ["in0", "in1", "in2", "in3"])

class WireModule(Module):
    def generate_output(self):
        inp = self.get_input("in0")
        print self.name, inp
        self.set_all_outputs(inp)

#======================================================
# initialize your modules here
#======================================================

W1 = WireModule("W1", ["in0"], ["out0", "out1"])
W2 = WireModule("W2", ["in0"], ["out0"])
W3 = WireModule("W3", ["in0"], ["out0"])
W4 = WireModule("W4", ["in0"], ["out0"])
MG = MidiModule("MG", ["in0", "in1"], [])

#======================================================
# connect modules here
#======================================================

start.connect("out0", W1, "in0")
W1.connect("out0", W2, "in0")
W1.connect("out1", W3, "in0")
W2.connect("out0", end, "in0")
W3.connect("out0", W4, "in0")
W4.connect("out0", MG, "in1")
start.connect("out1", MG, "in0")

#======================================================
# create source sequences here
#======================================================

#======================================================
# load sources into start inputs here
# loading two sources into an input overwrites the first one
# all start inputs must set
#======================================================

start.set_input([Chord([0, 4, 7]), Chord([0, 5, 9]), Chord([0, 4, 7]), Chord([2, 7, 11]), Chord([0, 4, 7])], "in0")
start.set_input([Chord([7]), Chord([9]), Chord([10]), Chord([11]), Chord([12])], "in1")

#======================================================
# DO NOT MODIFY
# starts the system
#======================================================
start.start()
