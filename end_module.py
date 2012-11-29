# DO NOT MODIFY

# Owner: Chris Dolan (cdolan@mit.edu)
# Summary:
# Notes:

from module import *

class End(Module):

    def __init__(self, name, inputs):
        super(End, self).__init__(name, inputs, [])
        self.finished = False

    def generate_output(self):
        if not self.finished:
            self.finished = True
            output = []
            for input in self.input.values():
                output += input
            print "The result is : " + str(output)

    def clock(self):
        pass
