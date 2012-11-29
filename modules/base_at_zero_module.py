# Owner: Chris Dolan (cdolan@mit.edu)
# Summary: This module takes a chord representation and puts it in normal form.
# Notes: Input is a list of chords, output is a list of chords

from module import *

class BaseAtZero(Module):
        
    def generate_output(self):
        #input to module can be accessed by calling self.get_input(<input port>)
        print "{0} processing on input {1} ".format(self.name, str(self.get_input("in0")))
        
        output = []
        for chord in self.get_input("in0"):
            output.append(sorted(chord.transpose(-min(chord))))

        #Once processing is complete, set the output of the module by calling self.set_output(<ouput>, <output port>)
        self.set_output(output, "out0")

        
        print "{0} processing complete. output is {1}".format(self.name, str(self.get_output("out0")))

    
