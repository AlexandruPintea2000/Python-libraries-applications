def sort ( a ):
	for i in range( 0, len( a ) ):
		for l in range( i + 1, len( a ) ):
			if ( a[ l ] < a[ i ] ):
				temp = a[ l ]
				a[ l ] = a[ i ]
				a[ i ] = temp
def sort_asc ( a ): return sort( a )
def sort_desc ( a ):
	for i in range( 0, len( a ) ):
		for l in range( i + 1, len( a ) ):
			if ( a[ l ] > a[ i ] ):
				temp = a[ l ]
				a[ l ] = a[ i ]
				a[ i ] = temp





arr = [ 2, 1, 3 ]
sort( arr )
print arr
sort_desc( arr )
print arr
sort_asc( arr )
print arr
