
def round( a ):
	if ( int( a + 1 ) - a < a - int( a ) ):
		return int( a + 1 )
	else:
		return int( a )


def round_asc ( a ): return int( a + 1 )
def round_desc ( a ): return int( a )

print round( 5.9 )
print round_asc( 0.9 )
print round_desc( 5.9 )
