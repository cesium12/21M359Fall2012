# Owner: Class
# Summary: Transpose all chords by n semitones
# Notes: Input: chord and number of steps, Output: transposed chord

from module import *
from chord import *

class TransposeByN(Module):
        
    def generate_output(self):
        
        steps=self.get_input("in1")
        assert isinstance(steps,int)
        chords = self.get_input("in0")
        for chord in chords:
            assert isinstance(chord,Chord)
        output = []
        for chord in chords:
            output.append(chord.transpose(steps))
        self.set_output(output,"out0")
        #your code goes here

        #input to module can be accessed by calling self.get_input(<input port>)        

        #Once processing is complete, set the output(s) of the module by calling self.set_output(<output>, <output port>)

    
        
