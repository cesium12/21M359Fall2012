# DO NOT MODIFY

# Owner: Chris Dolan (cdolan@mit.edu)
# Summary: Base class for all modules
# Notes: Create your own modules by subclassing Module and overriding generate_output(self) method

class Module(object):
    def __init__(self, name, input_ports, output_ports, verbose=False):
        if not isinstance(name, str):
            raise InitializationError("Module name must be an str." + \
                                      " Got: {0} which is {1}".format(name, type(name)))

        if not isinstance(input_ports, list):
            raise InitializationError("{0} input_ports must be a list." + \
                                      " Got: {1} which is {2}".format(name, input_ports, type(input_ports)))

        for port in input_ports:
            if not isinstance(port, str):
                 raise InitializationError("{0} input_ports elements must be a str." + \
                                           " Got element: {1} which is {2}".format(name, port, type(port)))

        if not isinstance(output_ports, list):
            raise InitializationError("{0} output_ports must be a list." + \
                                      " Got: {1} which is {2}".format(name, output_ports, type(output_ports)))

        for port in output_ports:
            if not isinstance(port, str):
                 raise InitializationError("{0} output_ports elements must be a str." + \
                                           " Got element: {1} which is {2}".format(name, port, type(port)))
        
        self.name = name
        self.connections = []
        self.input = {}
        self.output = {}
        
        for port in input_ports:
            if port in self.input.keys():
                raise InitializationError("{0} has duplicate input port name: {1}.".format(self.name, port))
            else:
                self.input[port] = None
                
        for port in output_ports:
            if port in self.output.keys():
                raise InitializationError("{0} has duplicate output port name: {1}.".format(self.name, port))
            else:
                self.output[port] = None
        
        print self.name + " initialized"

    def connect(self, output_port, connection, input_port):
        if not connection.has_input_port(input_port):
            raise ConnectionError("Attemped to connect {0} output port {1} to {2} input port {3}," + \
                                  " but {2} has no input port named {3}.".format(self.name, output_port, connection.name, input_port))
        if not self.has_output_port(output_port):
             raise ConnectionError("Attemped to connect {0} output port {1} to {2} input port {3}," + \
                                   " but {0} has no output port named {1}.".format(self.name, output_port, connection.name, input_port))
        
        self.connections.append((output_port, connection, input_port))
        
    def has_input_port(self, port):
        return port in self.input.keys()

    def has_output_port(self, port):
        return port in self.output.keys()

    def set_input(self, input, input_port):
        if self.has_input_port(input_port):
            self.input[input_port] = input
        else:
            raise SetInputException("{0} has no input port named {1}.".format(self.name, input_port))          

    def get_input(self, input_port):
        if self.has_input_port(input_port):
            return self.input[input_port]
        else:
            raise GetInputError("{0} has no input port named {1}.".format(self.name, input_port))

    def get_output(self, output_port):
        if self.has_output_port(output_port):
            if self.output[output_port] is not None:
                return self.output[output_port]
            else:
                raise GetOutputError("{0} has None output on port {1}".format(self.name, output_port))
        else:
            raise GetOutputError("{0} has no output port named {1}.".format(self.name, output_port))

    def set_output(self, output, output_port):
        if self.has_output_port(output_port):
            self.output[output_port] = output
        else:
            raise SetOutputException("{0} has no output port named {1}.".format(self.name, output_port))

    def set_all_outputs(self, output):
        for output_port in self.output.keys():
            self.set_output(output, output_port)
            
    def process(self):
        if None not in self.input.values():
            self.generate_output()

    def generate_output(self):
        raise NotImplementedError("Subclasses of Module must implement generate_output method.")
        
    def clock(self):
        for output_port, connection, input_port in self.connections:                
            connection.set_input(self.get_output(output_port), input_port)

        for output_port, connection, port in self.connections:
            connection.process()

        for output_port, connection, port in self.connections:
            connection.clock()

class CustomError(Exception, object):
    def __init__(self, message):
        super(CustomError, self).__init__()
        self.message = message
        
    def __str__(self):
        return str(self.message)

class ConnectionError(CustomError):
    def __init__(self, message):
        super(ConnectionError, self).__init__(message)

class GetOutputError(CustomError):
    def __init__(self, message):
        super(GetOutputError, self).__init__(message)

class GetInputError(CustomError):
    def __init__(self, message):
        super(GetInputError, self).__init__(message)

class SetOutputError(CustomError):
    def __init__(self, message):
        super(SetOutputError, self).__init__(message)

class SetInputError(CustomError):
    def __init__(self, message):
        super(SetInputError, self).__init__(message)

class InitializationError(CustomError):
    def __init__(self, message):
        super(InitializationError, self).__init__(message)
