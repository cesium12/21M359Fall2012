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
end = End("End", ["in0"])

#======================================================
# initialize your modules here
#======================================================

TBN1 = TransposeByN("TBN1", ["in0", "in1"], ["out0"])
#TUO1 = TransposeUpOne("TUO1", ["in0"], ["out0"])
#TUO2 = TransposeUpOne("TUO2", ["in0"], ["out0"])

#======================================================
# connect modules here
#======================================================

start.connect("out0", TBN1, "in0")
start.connect("out1", TBN1, "in1")
TBN1.connect("out0", end, "in0")
#TUO1.connect("out0", TUO2, "in0")
#TUO2.connect("out0", end, "in0")

#======================================================
# create source sequences here
#======================================================

source_sequence = [Chord([1,3,5]), Chord([0,4,7])]

#======================================================
# load sources into start inputs here
# loading two sources into an input overwrites the first one
# all start inputs must set
#======================================================

start.set_input(source_sequence, "in0")
start.set_input([3, 6], "in1")

#======================================================
# DO NOT MODIFY
# starts the system
#======================================================
start.start()
