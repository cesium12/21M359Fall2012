# Owner: Class
# Summary: Transpose all chords by n semitones
# Notes: Input: chord and number of steps, Output: transposed chord

from module import *
from chord import *

class TransposeByN(Module):
    def generate_output(self):
        chords = self.get_input("in0")
        steps = self.get_input("in1")
        assert len(chords) == len(steps)
        output = []
        for chord, step in zip(chords, steps):
            assert isinstance(chord, Chord)
            assert isinstance(step, int)
            output.append(chord + step)
        self.set_output(output, "out0")
