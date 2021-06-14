def set_file ( filename, a ): 
	fo = open( filename, "w" ) # clears file
	fo.close()

	fo = open( filename, "w" )
	fo.write( a )
	fo.close()

def is_numeric ( a ):
	if ( len(a) == 0 ): return 0

	for i in range( len( a ) ):
		if ( a[ i ] >= '0' and a[ i ] <= '9' ): continue
		else: return 0;
	return 1

def is_in ( arr, a ):
	for l in arr:
		if ( l == a ): return 1
	return 0


# get class name
parameters = []
name = raw_input( "Class name: " )
name = name.title()
filename = name + ".py"

# get num. of choices
num = "choices"
while ( is_numeric( num ) == 0 ):
	num = raw_input( "Num. of parameters: " )
num = int( num )

# get choices
for i in range( 1, num + 1 ):
	temp = raw_input( "Parameter " + str( i ) + ": " )
	while( is_in ( parameters, temp ) ):
		print "Already mentioned \"" + temp + "\"!"
		temp = raw_input( "Parameter " + str( i ) + ": " )
	parameters.append( temp )



# class
file_class = "class " + name + ":\n"
file_class = file_class + "	\"Class: '" + name + "' has parameters: "
for i in parameters:
	file_class = file_class + i + ' '
file_class = file_class + "\"\n\n"




# __init__
file_class = file_class + "	def __init__( self, "
for i in range( 0, len( parameters ) ):
	file_class = file_class + parameters[ i ]
	if ( i != len( parameters ) - 1 ):
		file_class = file_class + ", "
file_class = file_class + " ):\n"
for i in parameters:
	file_class = file_class + "		self." + i + " = " + i + "\n"

file_class = file_class + "\n\n"

# __str__
file_class = file_class + "	def __str__( self ):\n"
file_class = file_class + "		class_string = \"" + name + ":\\n\"\n"
for i in parameters:
	file_class = file_class + "		class_string = class_string + \"  " + i + " = \" + str( self." + i + " ) + \"\\n\"\n"
file_class = file_class + "		return class_string\n\n"
file_class = file_class + "\n\n"


# Getters
for i in parameters:
	file_class = file_class + "	def get_" + i + "( self ): return self." + i + "\n\n"
file_class = file_class + "\n"

# Settters
for i in parameters:
	file_class = file_class + "	def set_" + i + "( self, " + i +" ): self." + i + " = " + i + "\n\n"
file_class = file_class + "\n\n"


set_file( filename, file_class )



#class_init = Class( 1, 2, 3, 4, 5 )
#print class_init.set_parameter5( -1 )
#print class_init
#print class_init.get_parameter5()
