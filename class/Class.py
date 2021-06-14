class Class:
	"Class: 'Class' has parameters: parameter1 parameter2 parameter3 parameter4 parameter5 "

	def __init__( self, parameter1, parameter2, parameter3, parameter4, parameter5 ):
		self.parameter1 = parameter1
		self.parameter2 = parameter2
		self.parameter3 = parameter3
		self.parameter4 = parameter4
		self.parameter5 = parameter5


	def __str__( self ):
		class_string = "Class:\n"
		class_string = class_string + "  parameter1 = " + str( self.parameter1 ) + "\n"
		class_string = class_string + "  parameter2 = " + str( self.parameter2 ) + "\n"
		class_string = class_string + "  parameter3 = " + str( self.parameter3 ) + "\n"
		class_string = class_string + "  parameter4 = " + str( self.parameter4 ) + "\n"
		class_string = class_string + "  parameter5 = " + str( self.parameter5 ) + "\n"
		return class_string



	def get_parameter1( self ): return self.parameter1

	def get_parameter2( self ): return self.parameter2

	def get_parameter3( self ): return self.parameter3

	def get_parameter4( self ): return self.parameter4

	def get_parameter5( self ): return self.parameter5


	def set_parameter1( self, parameter1 ): self.parameter1 = parameter1

	def set_parameter2( self, parameter2 ): self.parameter2 = parameter2

	def set_parameter3( self, parameter3 ): self.parameter3 = parameter3

	def set_parameter4( self, parameter4 ): self.parameter4 = parameter4

	def set_parameter5( self, parameter5 ): self.parameter5 = parameter5


class_init = Class( 1, 2, 3, 4, 5 )
print class_init.set_parameter5( -1 )
print class_init
print class_init.get_parameter5()
