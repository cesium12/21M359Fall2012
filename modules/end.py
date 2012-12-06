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
            print "The result is :", self.input.values()

    def clock(self):
        pass
