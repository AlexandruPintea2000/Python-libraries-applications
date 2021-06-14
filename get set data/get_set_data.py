
def get ( a = "" ):	return raw_input( a )
def set ( a ): print a,

def get_array ( num = 0, a = "" ):
	if ( a != "" ):
		print "\nSet " + a + ":"
	else:
		print "\nSet array:"

	arr = []
	for i in range( 0, num ):
		arr.append( get( " [" + str( i + 1 ) + "]: " ) )
	return arr

def set_array ( arr ):
	for i in range( 0, len( arr ) ):
		if ( i != len( arr ) - 1 ):
			set( arr[ i ] + ',' )
		else:
			set( arr[ i ] )
			


def get_sets ( a ):
	a = get()
	set( a )

num = 0
get_sets( num )

arr = get_array( 5, "Arr" )
set_array( arr )
