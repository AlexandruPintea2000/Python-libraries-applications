
import math

class Point:

	def __init__ ( self, x, y ):
		self.x = x
		self.y = y

	def __str__ ( self ):
		return "Point [ " + str( self.x ) + " , " + str( self.y ) + " ]"


	def __add__ ( self, point ): return Point( self.x + point.x, self.y + point.y )
	def __sub__ ( self, point ): return Point( self.x - point.x, self.y - point.y )

	def get_x ( self ): return self.x

	def get_y ( self ): return self.y

	def set_x ( self, x ): self.x = x

	def set_y ( self, y ): self.y = y

	def distance ( self, point ):
			return math.sqrt( ( self.x - point.get_x() ) * ( self.x - point.get_x() ) + ( self.y - point.get_y() ) * ( self.y - point.get_y() ) )



# ax + by + c = 0
# y = - ( ax + c ) / b
# y = - ax / b - c / b

# y = - ( a1x + c1 ) / b1
# y = - ( a2x + c2 ) / b2
# ( a1x + c1 ) / b1 = ( a2x + c2 ) / b2
# a1x / b1 + c1 / b1 = a2x / b2 + c2/ b2
# x( a1 / b1 - a2 / b2 ) = c2 / b2 - c1 / b1

# x = - ( c1 / b1 - c2 / b2 ) / ( a1 / b1 - a2 / b2 )

class Line:

	def __init__ ( self, a, b, c ):
		self.a = a
		self.b = b
		self.c = c

	def get_common_point ( self, line ):
		x_1 = - ( self.c / self.b - line.get_c() / line.get_b() ) / ( self.a / self.b - line.get_a() / line.get_b() )
		y_1 = - ( self.a * x_1 + self.c ) / self.b
		return Point( x_1, y_1 )

	def get_y ( self, x ):
		return - ( self.a * x + self.c ) / self.b

	def get_x0 ( self ): return - self.c / self.a
	def get_y0 ( self ): return - self.c / self.b

	def get_coef ( self ):
		arr = []
		arr.append( - self.a / self.b )
		arr.append( - self.c / self.b )
		return arr

	def is_in ( self, point ):
		if ( self.a * point.get_x() + self.b * point.get_y() + self.c == 0 ):
			return 1
		return 0

	def __str__ ( self ):
		return "Line [ " + str( self.a ) + "x + " + str( self.b ) + "y + " + str( self.c ) + " ]"

	def get_a ( self ): return self.a
	def get_b ( self ): return self.b
	def get_c ( self ): return self.c

	def set_a ( self, a ): self.a = a
	def set_b ( self, b ): self.b = b
	def set_c ( self, c ): self.c = c

def is_in ( arr, a ):
	for l in arr:
		if ( l == a ):
			return 1
	return 0




def heron ( a, b, c ):
	p = ( a + b + c ) / 2
	return math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ) )

class Shape:

	def __init__ ( self, arr ):
		self.arr = arr



	def perimeter ( self ):
		p = 0
		for i in range( 0, len( self.arr ) - 1 ):
			p = p + self.arr[ i ].distance( self.arr[ i + 1 ] )
		p = p + self.arr[ 0 ].distance( self.arr[ len( self.arr ) - 1 ] )

		return p






	def __str__ ( self ):
		shape = "Shape: "
		for l in range( 0, len( self.arr ) ):
			shape = shape + "[ " + self.arr.get_x() + " , " + self.arr.get_y() + " ]"
			if ( l != len( self.arr ) - 1 ):
				shape = shape + ", "
		return shape



	def area ( self ):
		ar = 0
		consider = []
		arr = []
		while ( len( consider ) != len( self.arr ) ):
			for l in range( len( self.arr ) ):
				if ( is_in( consider, self.arr[ l ] ) == 0 ):
					arr.append( self.arr[ l ] )
				if ( len( arr ) == 3 ):
					a = arr[ 0 ].distance( arr[ 1 ] )
					b = arr[ 1 ].distance( arr[ 2 ] )
					c = arr[ 2 ].distance( arr[ 0 ] )
					ar = ar + heron( a, b, c )
					consider.append( arr[ 1 ] )
					arr = []
		return ar


	def get_shape ( self ):
		return self.arr



def is_triangle ( a, b, c ):
	if ( a >= b + c ): return 0
	if ( b >= c + a ): return 0
	if ( c >= b + a ): return 0

	return 1

def is_isoscel ( a, b, c ):
	if ( is_triangle( a, b, c ) == 0 ):
		return 0

	if ( a == b ): return 1
	if ( c == b ): return 1
	if ( c == a ): return 1

	return 0

def is_ech ( a, b, c ):
	if ( is_triangle( a, b, c ) == 0 ):
		return 0

	if ( a == b and b == c ): return 1

	return 0

def is_pitagora ( a, b, c ):
	arr = [ a, b, c ]
	arr.sort()
	if ( arr[ 2 ] * arr[ 2 ] == arr[ 1 ] * arr[ 1 ] + arr[ 0 ] * arr[ 0 ] ):
		return 1

	return 0

def distance ( x1, y1, x2, y2 ):
	return math.sqrt( ( x1 - x2 ) * ( x1 - x2 ) + ( y1 -y2 ) * ( y1 - y2 ) )




point = Point( 1, 2 )
print point


print is_triangle( 1, 2, 3 )
print is_isoscel( 2, 2, 3 )
print is_ech( 1, 2, 3 )

print Point( 1, 2 ) + Point( 2, 3 )
print Point( 1, 2 ) - Point( 2, 3 )



line = Line( 1, 2, 3 )
print line.get_y( 1 )
print line

print distance ( 1, 2, 3, 4 )

print is_pitagora( 5, 3, 4 )

arr = [ Point( 1, 2 ), Point( 2, 2 ), Point( 2, 1 ), Point( 1, 1 ) ]
shape = Shape( arr )
print shape.perimeter()
print shape.area()
