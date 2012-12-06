# DO NOT MODIFY

# Owner: Chris Dolan (cdolan@mit.edu)
# Summary: Start module acts like a thru
# Notes: Each input it transferred to the corresponding output, in the order given at initialization

from module import *
from sys import argv

class Start(Module):
    args = []
    kwargs = {}

    def __init__(self, name, input_ports, output_ports, *args, **kwargs):
        if len(input_ports) != len(output_ports):
            raise Exception("Initialization Error. Start module must have same number of inputs as outputs.")
        super(Start, self).__init__(name, input_ports, output_ports)
        self.input_ports = input_ports
        self.output_ports = output_ports
        Start.args = args
        Start.kwargs = kwargs

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
        
        args = []
        kwargs = Start.kwargs
        option = None
        for i, arg in enumerate(argv[1:]):
            if option is not None:
                kwargs[option] = arg
                option = None
            elif '=' in arg:
                kwargs.update([ arg.lstrip('-').split('=', 1) ])
            elif arg.startswith('-'):
                option = arg.lstrip('-')
            else:
                args.append(arg)
        
        Start.args = args or Start.args
        Start.kwargs = kwargs
