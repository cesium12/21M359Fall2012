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

        self.pitch_classes = tuple(sorted( p % 12 for p in pitch_classes ))
        #We should reinitialize this to accept octaves and note names (like C#4 vs C#6, we don't want them both to be '2')

    def transpose(self, steps):
        if not isinstance(steps, int):
            raise Exception("Transpose steps must be an int. Chord {0} got: {1} which is {2}".format(str(self), steps, type(steps)))
        pitch_classes = [(pc + steps) % 12 for pc in self.pitch_classes]
        return Chord(pitch_classes)


    def invert(self, top):
        if not isinstance(top, int):
            raise Exception("Invert top must be an int. Chord {0} got: {1} which is {2}".format(str(self), top, type(top)))
        pitch_classes = [(top - pc) % 12 for pc in self.pitch_classes]
        return Chord(pitch_classes)

    def expand(self, factor):
        if not isinstance(factor, int):
            raise Exception("Expand factor must be an int. Chord {0} got: {1} which is {2}".format(str(self), factor, type(factor)))
        pitch_classes = [(pc * factor) % 12 for pc in self.pitch_classes]
        return Chord(pitch_classes)

    def interval_vector(self):
        from collections import defaultdict
        intervals = defaultdict(int)
        for i, pci in enumerate(self.pitch_classes):
            for pcj in self.pitch_classes[i+1:]:
                interval = (pcj - pci) % 12
                if interval > 6:
                    interval = 12 - interval
                intervals[interval] += 1
        return tuple( intervals[i + 1] for i in range(6) )

    def zero_shifted(self):
        sorted_pitch_classes = [] 
        sorted_pitch_classes = sorted(pitch_classes)
        if sorted_pitch_classes[0] == 0:
            return Chord(sorted_pitch_classes)
        else:
            shifting_factor = sorted_pitch_classes[0]
            for i in sorted_pitch_classes:
                sorted_pitch_classes[i] = sorted_pitch_classes[i]-shifting_factor
            return Chord(sorted_pitch_classes)


    def __repr__(self):
        return "({0})".format(",".join([str(pc) for pc in self.pitch_classes]))

    def __add__(self, interval):
        return self.transpose(interval)
    def __sub__(self, interval):
        return self.transpose(-interval)
    def __mul__(self, factor):
        return self.expand(factor)
    def __radd__(self, interval):
        return self.transpose(interval)
    def __rsub__(self, interval):
        return self.invert(0).transpose(interval)
    def __rmul__(self, factor):
        return self.expand(factor)
    def __pos__(self):
        return self
    def __neg__(self):
        return self.invert(0)
