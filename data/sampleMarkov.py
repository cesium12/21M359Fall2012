# Owner: Michael Wu
# Notes: A basic MarkovModel that sees if the last chord is major/minor/other
# and returns its L, P, or R chord with set probabilities

class LPRMarkov(MarkovModel):
    def __init__(self, table = [[1, 1, 1], [1, 1, 1]]):
        self.table = [self.normalize(row) for row in table]

    def getNext(self, chords):
        if not chords:
            return None
        lastChord = chords[-1]
        choices = [lastChord.getLChord(), lastChord.getPChord(), lastChord.getRChord()]
        if lastChord.isMajorTriad():
            return self.select(choices, table[0])
        if lastChord.isMinorTriad():
            return self.select(choices, table[1])
        return None
