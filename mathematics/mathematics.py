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

def lc ( a, b ):
	while ( a != 0 and b != 0 ):
		if ( a > b ): a = a % b
		else: b = b % a
	if ( a != 0 ): return a
	else: return b

def gc ( a, b ):
	return a * b / lc( a, b )







def prime ( a ):
	if ( a == 0 ): return 0
	if ( a == 1 ): return 0
	if ( a == 2 ): return 1

	for i in ( 3, a ):
		if ( a % i == 0 ): return 0

	return 1


import math
def squ ( a ): return math.sqrt( a )

def is_squ ( a ):
	if ( squ( a ) == int( squ( a ) ) ):
		return 1
	return 0

def invert_arr ( a ):
	b = []
	for i in range( len( a ) ):
		b.append( a[ len( a ) - 1 - i ] )
	return b

def digits ( a ):
	d = []
	b = a
	while ( b > 0 ):
		d.append( b % 10 )
		b = b / 10
	return invert_arr( d )

def num_digits ( a ):
	d = digits( a )
	return len( d )

def sum_digits ( a ):
	d = digits( a )
	sm = 0
	for i in range( len( d ) ):
		sm = sm + d[ i ]
	return sm

def cnl ( a ):
	if ( a >= 0 ):	b = a
	else: b = -a
	while ( b > 9 ):
		b = sum_digits( b )
	return b

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

print even( 2 ),
print odd( 2 ),
print pos( 2 ),
print neg( 2 ),

intl = Interval( 0, 9 )
print intl.is_in( 5 )
print intl.is_in( -1 )
print Interval.__name__ + ": ",
print intl,
print Interval( 1, 5, 1, 0 ) + Interval( 0, 4 ),
print Interval( 1, 5, 0, 1 ) - Interval( 0, 4 )

print lc( 25, 15 )
print gc( 25, 15 )

print prime( 2 )
print digits( 10 )
print num_digits( 10 ), sum_digits( 10 )
print cnl( 1049 )

print is_squ( 25 )
