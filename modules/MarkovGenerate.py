# Owner: Michael Wu
# Summary: generates chords using a MarkovModel and a given list of chords
# Notes: Input: inp0 is a list of chords, inp1 is a MarkovModel, inp2 is the number of steps to run
#        Output: inp1 extended by a certain number of chords
# See MarkovModel for details

from module import *

class MarkovGenerate(Module):
        
    def generate_output(self):
        print "{0} processing on input {1} ".format(self.name, str(self.get_input("in0")))
        self.check_inputs()
        
        chords = self.get_input("in0")
        model = self.get_input("in1")
        steps = self.get_input("in2")

        for i in range(steps):
            nextChord = model.getNext(chords)
            if nextChord is None:
                print "Markov process ended early"
                break
            chords.append(nextChord)

        self.set_output(chords, "out0")
        print "{0} processing complete. output is {1}".format(self.name, str(self.get_output("out0")))

    def check_inputs(self):
        chords = self.get_input("in0")
        if not isinstance(chords, list):
            raise Exception("in0 is not a list")
        for chord1 in chords:
            if not isinstance(chord1, chord):
                raise Exception("in0 is not a list of chords")
            
        if not isinstance(self.get_input("in1"), MarkovModel):
            raise Exception("in1 is not a MarkovModel")

        if not isinstance(self.get_input("in2"), int):
            raise Exception("in2 is not an int")
