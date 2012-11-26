# Owner: Class
# Summary: <One sentence summary of what your system does>
# Notes:

from modules import *

#======================================================
# initialize start and end
# start is a thru, ie. it passes in0 to out0, in1 to out1, etc...
# thus it must has same number of inputs as outputs
# NOTE: end has no outputs!
#======================================================

start = Start("Start", <input ports>, <output ports>)
end = End("End", <input ports>)

#======================================================
# initialize your modules here
#======================================================

var = ModuleName(<name>, <input ports>, <output ports>)

#======================================================
# connect modules here
#======================================================

start.connect(<output port>, some_var, <input port>)
#other connections go here
some_var.connect(<output port>, end, <input port>)

#======================================================
# create source sequences here
#======================================================

#e.g. source_sequence = [Chord([1,4,7]), Chord([3,4,5])]

#======================================================
# load sources into start inputs here
# loading two sources into an input overwrites the first one
# all start inputs must set
#======================================================

start.set_input(<source_sequence>, <input port>)

#======================================================
# DO NOT MODIFY
# starts the system
#======================================================
start.start()
