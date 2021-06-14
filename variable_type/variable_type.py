def is_numeric ( a ):
	if ( len(a) == 0 ): return 0

	for i in range( len( a ) ):
		if ( a[ i ] >= '0' and a[ i ] <= '9' ): continue
		else: return 0;
	return 1


def type ( a ):
	if ( is_numeric( a ) == 1 ): return "numeric"

	return "string"

a = "5"
b = type( a )
print b



name = ""
