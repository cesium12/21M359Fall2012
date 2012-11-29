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
    def order(self):
    	pitch_classes = sorted(self.pitch_classes)
    	return Chord(pitch_classes)
    def fix(self):
    	pitch_classes = self.pitch_classes[:]
       	for i in range(len(pitch_classes)):
       		pitch_classes[i] = pitch_classes[i]%12
    	return Chord(pitch_classes)
    def zero(self):
    	pitch_classes = [a - self.pitch_classes[0] for a in self.pitch_classes]
    	return Chord(pitch_classes)
    def invert(self):
   		pitch_classes = [self.pitch_classes[2]-pc for pc in self.pitch_classes]
   		pitch_classes = pitch_classes[::-1]
   		return Chord(pitch_classes)
    def transpose(self, steps):
        if not isinstance(steps, int):
            raise Exception("Transpose steps but be an int. Chord {0} got: {1} which is {2}".format(str(self), steps, type(steps)))
        pitch_classes = [pc + steps for pc in self.pitch_classes]
        return Chord(pitch_classes)

    def __repr__(self):
        return "({0})".format(",".join([str(pc) for pc in self.pitch_classes]))
    
