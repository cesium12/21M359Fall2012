#!/usr/bin/env python
# Owner: <your name> (<your email>)
# Summary: <One sentence summary of module functionality>
# Notes: Input: <what the input is>, Output: <what the output is>, <other notes>

from module import *

class ReduceModule(Module):
        

    def generate_output(self):
               
        #input to module can be accessed by calling self.get_input(<input port>)
        print "{0} processing on input {1} ".format(self.name, str(self.get_input("in0")))
        
        output = []
        for chord in self.get_input("in0"):
        	a1 = chord.fix()
        	a2 = a1.order()
        	a3 = a2.zero()
        	a4 = a3.invert()
        	if a4.pitch_classes[1] < a3.pitch_classes[1]:
        		output.append(a4)
        	else:
        		output.append(a3)

        #Once processing is complete, set the output of the module by calling self.set_output(<ouput>, <output port>)
        self.set_output(output, "out0")
		
        
        print "{0} processing complete. output is {1}".format(self.name, str(self.get_output("out0")))

        #your code goes here

        #input to module can be accessed by calling self.get_input(<input port>)        

        #Once processing is complete, set the output(s) of the module by calling self.set_output(<output>, <output port>)

   