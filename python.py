
# Python data

i = 0

# a = b = c = 0;
# a,b,c = 1,4.9,"string"

string = "Python";

print string + " compiles!"
print string[0],
print string[1:5]

string = """string

string""" # multiple line string



# Arr-s



l1 = [ "string_l1", 1, 5.9, "string_l1", 30 ]
l2 = [ 14, "string_l2", [ 1, 2 ] ]
# if they had () they were tples ( const lsts )
tupl = "a", "b", "c"


l3 = { "id": 0, "firstname": "fname", "lastname": "lname" }
# l3 = { "id": 0, "id": 5 } prints 5 for l3l[ "id" ]


print l1
print l2
print len ( l2 )
print l2[ -2 ] # right count -len( l2 ), -len( l2 ) + 1, ... , -2, -1 
print l3
print l3[ "id" ]
print l1 + l2, l3



# Casting



print i
print int( 90.7 ) # also long, complex
# also sqrt and rndm



# Variable with Lambda expression



sum = lambda a, b : a + b
print sum( 1, 2 )



# Output format



print "String = %s and Num = %d" % ( "string", 9 )
# del rmves a variable 





"comment" # also comment


def even ( a ): # referenced
	if ( a % 2 == 0 ):
		return 1
	else:
		return 0

def odd ( a ): # also odd( a = 0 )
	if ( a % 2 == 1 ):
		return 1
	else:
		return 0

def pos ( a ):
	if ( a >= 0 ):
		return 1
	else:
		return 0

def neg ( a ):
	if ( a < 0 ):
		return 1
	else:
		return 0





print even( 2 ),
print odd( 2 ),
print pos( 2 ),
print neg( 2 ),



class Interval:
	def __init__( self, a, b, closed_l = 1, closed_r = 1 ):
		self.a = a
		self.b = b
		self.closed_l = closed_l
		self.closed_r = closed_r

	def __str__( self ) :
		intl_string = ""
		if ( self.closed_l == 1 ):
			intl_string = intl_string + "["
		else:
			intl_string = intl_string + "("

		intl_string = intl_string + ' ' + str( self.a ) + ", " + str( self.b ) + ' '

		if ( self.closed_r == 1 ):
			intl_string = intl_string + "]"
		else:
			intl_string = intl_string + ")"
		return intl_string;

	def __add__( self, intl ): 
		last_a = self.a
		last_b = self.b
		last_l = self.closed_l
		last_r = self.closed_r
		if ( self.a > intl.a ):
			last_a = intl.a
			last_l = intl.closed_l
		if ( self.b < intl.b ):
			last_b = intl.b
			last_r = intl.closed_r
		return Interval( last_a, last_b, last_l, last_r )

	def __sub__( self, intl ): 
		last_a = self.a
		last_b = self.b
		last_l = self.closed_l
		last_r = self.closed_r
		if ( self.a < intl.a ):
			last_a = intl.a
			last_l = intl.closed_l
		if ( self.b > intl.b ):
			last_b = intl.b
			last_r = intl.closed_r
		return Interval( last_a, last_b, last_l, last_r )

	def is_in ( self, l ):
		is_in_l = 0;
		is_in_r = 0;

		if ( self.closed_l == 1 and l >= self.a ): is_in_l = 1
		if ( self.closed_l == 0 and l > self.a ): is_in_l = 1
		if ( self.closed_r == 1 and l <= self.a ): is_in_r = 1
		if ( self.closed_r == 0 and l < self.a ): is_in_r = 1

		if ( is_in_l == 1 and is_in_r == 1 ):
			return 1
		else:
			return 0

intl = Interval( 0, 9 )
print intl.is_in( 5 )
print intl.is_in( -1 )
print Interval.__name__ + ": ",
print intl,
print Interval( 1, 5, 1, 0 ) + Interval( 0, 4 ),
print Interval( 1, 5, 0, 1 ) - Interval( 0, 4 )

# inheritance: Interval(Mathematics):




# string = raw_input( "String = " )
# print string
# string = input( "String = " ) expects a python expression

def get_file ( filename ):
	fi = open( filename, "r" )
	string = fi.read() # read(10) reads chars 0-9, then 9-17; tell() tells you file position 
	fi.close()
	return string

def clear_file ( filename ):
	fo = open( filename, "w" ) # clears file
	fo.close()

def set_file ( filename, a ): 
	clear_file( filename ) # clear file

	fo = open( filename, "w" )
	fo.write( a )
	fo.close()

def add_line_file ( filename, a ): 
	fo = open( filename, "w" )
	fo.write( "\n" + a )
	fo.close()
	
def add_word_file ( filename, a ): 
	fo = open( filename, "w" )
	fo.write( " " + a )
	fo.close()



set_file( "python_file", "Python file\npython" )
print get_file( "python_file" )


import os

os.remove( "python_file" )
os.mkdir( "Python" ) # if make a dir that already is, err
os.rmdir( "Python" ) # rmves dir
os.chdir( "/" ) # gets to a dir
print os.getcwd() # gives our dir

# also chmod, chown, fchdir( file ) gets to dir of file


# import thread
import time
time.sleep( 1 )


