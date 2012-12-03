# Owner: Michael Wu
# Notes: skeleton for a Markov model
# To make a particular Markov model, create a class that extends MarkovModel
# and implements a getNext method that takes chords and produces the next chord
import random

class MarkovModel():
    def __init__(self):
        pass

    def getNext(self, chords):
        pass

    def normalize(self, probs):
        total = sum(probs)
        return [float(x) / total for x in probs]

    def select(self, choices, probs):
        if len(choices) != len(probs):
            raise Exception("Choices do not match probs")
        total = 0
        target = random.random()
        for i in range(len(probs)):
            total += probs[i]
            if total >= target:
                break
        return choices[i]
