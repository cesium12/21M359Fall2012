# Owner: Class
# Summary: class representing a pitch
# Notes: 

from module import *

step_to_pc = { 'C' : 0, 'D' : 2, 'E' : 4, 'F' : 5,'G' : 7, 'A' : 9, 'B' : 11,}
step_names = ['C','D','E','F','G','A','B']


class Pitch:
    def __init__(self, pitch):
        if not isinstance(pitch, str or int):
            raise Exception("Pitch must be represented as a string or an int. Got: {0}, which is {1}".format(pitch, type(pitch)))

    #TODO: Link sharps '#' and flats '-' to pitch names

    #TODO: Octave and octave equivalence

    #TODO: Function that converts pitches (like E4) to pitch classes (4)

    #TODO: Function that converts pitch classes to a string



