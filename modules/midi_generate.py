from modules import *
from data import *
import midi

def noteon(t, track, pitch, start, duration, velocity):
    on = midi.NoteOnEvent()
    on.pitch = pitch
    on.velocity = velocity
    on.tick = start
    on.channel = track
    t.add_event(on)
    off = midi.NoteOffEvent()
    off.pitch = pitch
    off.velocity = velocity
    off.tick = start + duration
    off.channel = track
    t.add_event(off)

class MidiModule(Module):
    def generate_output(self):
        TEMPO = int(Start.kwargs.get('tempo', 60))
        OUTPUT = Start.kwargs.get('out', 'out.mid')
        t = midi.new_stream(resolution=120, tempo=TEMPO)
        for i, inp in enumerate(self.input.values()):
            for j, item in enumerate(inp):
                if isinstance(item, Chord):
                    pitches = [ p + 60 for p in item.pitch_classes ] # XXX
                else:
                    raise TypeError('Only chords supported for MIDI out right now')
                for pitch in pitches:
                    noteon(t, i, pitch, j * 120, 100, 100)
        midi.write_midifile(t, OUTPUT)
