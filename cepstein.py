
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

start = Start("Start", ["in0"], ["out0"])
end = End("End", ["in0"])

#======================================================
# initialize your modules here
#======================================================

Reduce01 = ReduceModule("Reduce01", ["in0"], ["out0"])
#TUO2 = TransposeUpOne("TUO2", ["in0"], ["out0"])

#======================================================
# connect modules here
#======================================================

start.connect("out0", Reduce01, "in0")
Reduce01.connect("out0", end, "in0")

#======================================================
# create source sequences here
#======================================================

source_sequence = [Chord([42,-53,15]), Chord([3,14,5])]

#======================================================
# load sources into start inputs here
# loading two sources into an input overwrites the first one
# all start inputs must set
#======================================================

start.set_input(source_sequence, "in0")

#======================================================
# DO NOT MODIFY
# starts the system
#======================================================
start.start()
