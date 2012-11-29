# DO NOT MODIFY

# Owner: Chris Dolan (cdolan@mit.edu)
# Summary: Start module acts like a thru
# Notes: Each input it transferred to the corresponding output, in the order given at initialization

from module import *

class Start(Module):

    def __init__(self, name, input_ports, output_ports):
        if len(input_ports) != len(output_ports):
            raise Exception("Initialization Error. Start module must have same number of inputs as outputs.")
        super(Start, self).__init__(name, input_ports, output_ports)
        self.input_ports = input_ports
        self.output_ports = output_ports

    def start(self):
        self.process()
        self.clock()

    def process(self):
        if None not in self.input.values():
            self.generate_output()
        else:
            raise Exception("Start block has None inputs for port(s) {0}.".format(",".join([port for port, value in self.input if value is None])))

    def generate_output(self):
        for i in range(len(self.input_ports)):
            self.set_output(self.get_input(self.input_ports[i]), self.output_ports[i])

    
