# Owner: Class
# Summary: class representing a chord
# Notes:

class Chord:
    def __init__(self, pitch_classes):
        if not isinstance(pitch_classes, list):
            raise Exception("Chord must be initialized with a list of pitch classes. Got: {0}, which is {1}".format(pitch_classes, type(pitch_classes)))

        for entry in pitch_classes:
            if not isinstance(entry, int):
                raise Exception("Chord must be initialized with a list of pitch classes. Got entry of list: {0}, which is {1}".format(entry, type(entry)))

        self.pitch_classes = pitch_classes
        
    def transpose(self, steps):
        if not isinstance(steps, int):
            raise Exception("Transpose steps but be an int. Chord {0} got: {1} which is {2}".format(str(self), steps, type(steps)))
        pitch_classes = [pc + steps for pc in self.pitch_classes]
        return Chord(pitch_classes)

    def str(self):
        return str(self.pitch_classes)

    def __repr__(self):
        return "({0})".format(",".join([str(pc) for pc in self.pitch_classes]))
    
