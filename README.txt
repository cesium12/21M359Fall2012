21M359 Fall 2012
Music Composition Software
Instructor: Peter Whincop
Students:
	Chris Dolan (cdolan@mit.edu)
	<add your name here> (<add your email here>)

To run in Linux or Mac OSX:
       launch Terminal
       cd into the directory containing this file
       type 'python system.py' and press enter

Overview:
	The architecture of this project is based on the the idea of
	"black box" modules. Each module has some number of input ports,
	some number of output ports, takes as input some type of data 
	(primitives like lists, integers, floats and other defined data
	structures like chords) and gives as output
	some type of data.

	Modules are linked by connecting the output of one module to
	the input of another module as specified in system.py. For
	this project THERE CAN NEVER BE ANY CYCLES, meaning the
	output of a module can not be the input to an ancestor
	module. The program will either run forever or not start if
	you do this!

	The system must take the following form:

	START ---> (our module network goes here) ----> END

	There can only be one START and one END module.
	All initial inputs are loaded into START, which acts as a thru
	and passes its inputs to its corresponding outputs. The outputs
	pass through the module network until they get to END, which
	prints the result.

	If END has more than one input, it concatenates all the
	inputs in order to generate the result.

Creating Modules:
	 Where does your crazy idea actually go? In a custom module. First
	 create a subclass of Module, then override the
	 generate_output method. The inputs to the module are
	 available by calling self.get_input(<input port>). Once your
	 processing is finished, you must set the module's output by calling
	 self.set_output(<output>, <output port>). See
	 transpose_up_one_module.py for an example of how to do this.

Instantiating and Connecting Modules:
	In code, modules are instantiated by:
	ModuleName(<some descriptive name for debugging>, <list of
	input ports>, <list of output ports>)

	Ports are specified by unique strings.

	In code, modules are connected using the connect method:
	<module A>.connect(<output port of A>, <module B>, <input port
	of B>)

	Example:
	Suppose we have two modules, A and B:
	A = SomeModule("ModuleA", ["in1"] , ["out1", "out2"])
	B = SomeOtherModule("ModuleB", ["in1", "in2"] , ["out1", "out2"])

	Then the following connects output 1 of A to input 2 of B:
	A.connect("out1", B, "in2")
	
system.py:
	This is the configuration file for the program where instances of
	modules are instantiated and connected. Running this file
	runs the program.

modules.py:
	The list of all modules and data structures available for use in
	system.py. IF YOU CREATE A NEW MODULE OR DATA STRUCTURE, YOU
	MUST ADD IT TO THIS FILE TO USE IT IN SYSTEM.PY.

Adding new files:
       When adding a new file include the header:
       # Owner: <your name> (<your email address>)
       # Summary: <A one sentence description of what your module does>
       # Notes: <a list of inputs and outputs, any other notes>
       If the file is going to be modified by the class, use "Owner: class"
       See transpose_up_one_module.py for an example.

Modifying files:
	Do not modify files or functions that are labeled #DO NOT
	MODIFY. No, like actually. Just don't do it.




