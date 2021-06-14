def get_file ( filename ):
	fi = open( filename, "r" )
	string = fi.read() 
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
	string = get_file( filename )
	fo = open( filename, "w" )
	fo.write( string + "\n" + a )
	fo.close()

def add_string_file ( filename, a ): 
	string = get_file( filename )
	fo = open( filename, "w" )
	fo.write( string + a )
	fo.close()

def is_numeric ( a ):
	if ( len(a) == 0 ): return 0

	for i in range( len( a ) ):
		if ( a[ i ] >= '0' and a[ i ] <= '9' ): continue
		else: return 0;
	return 1

def have_ext ( filename ):
	for i in filename:
		if ( i == '.' ): return 1
	return 0

# get filename and num. of chocies
filename = raw_input( "Filename: " )
if ( have_ext( filename ) == 0 ):
	filename = filename + ".py"
num = "choices"
while ( is_numeric( num ) == 0 ):
	num = raw_input( "Num. of choices: " )
num = int( num )

# get choices
choices = []
for i in range( 1, num + 1 ):
	temp = raw_input( "Choice " + str( i ) + ": " )
	choices.append( temp )


# set choices
set_file( filename, "choices = [ " )
for i in range( len( choices ) ):
	add_string_file( filename, "\"" + choices[ i ] + "\"" )
	if ( i != len( choices ) - 1 ):
		add_string_file( filename, ", " )
add_string_file( filename, " ]\n" )


add_line_file( filename, get_file( "choices files/choice1" ) )

for i in range( 0, len( choices ) ):
	add_line_file( filename, "	if ( choice == " + str( i + 1 ) + " ):" )
	add_line_file( filename, "		code = 1 # your code\n" )

add_line_file( filename, get_file( "choices files/choice2" ) )
