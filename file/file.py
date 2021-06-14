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
	string = get_file( filename )
	fo = open( filename, "w" )
	fo.write( string + "\n" + a )
	fo.close()

def add_string_file ( filename, a, sep = "" ):
	string = get_file( filename )
	fo = open( filename, "w" )
	fo.write( string + sep + a )
	fo.close()






def have_ext ( filename ):
	for i in filename:
		if ( i == '.' ): return 1
	return 0

def get_filename ( filename ):
	result = ""
	for i in filename:
		if ( i == '.' ): break
		result = result + i

	return result

def get_ext ( filename ):
	if ( have_ext( filename ) == 0 ): return ""

	l = 0
	for i in range( 0, len( filename ) ):
		if ( filename[ i ] == '.' ):
			l = i;
			break
	l = l + 1;

	result = ""
	for i in range( l, len( filename ) ):
		result = result + filename[ i ]
	return result


# def filename_ext ( filename, ext ):
#	ext = get_ext( filename )
#	filename = get_filename( filename )










import os
def is_file ( filename ):
	if ( os.path.isfile( filename ) ): return 1
	return 0

def is_dir ( filename ):
	if ( os.path.isdir( filename ) ): return 1
	return 0

def remove ( filename ):
	if ( os.path.isfile( filename ) ):
		os.remove( filename )
		return
	if ( os.path.isdir( filename ) ): 
		os.rmdir( filename )
		return
	print "File / Dir.: \"" + filename + "\" invalid. Removal failed."

def mkdir ( filename ):
	if ( os.path.isdir( filename ) == 0 ): os.mkdir( filename )
	else: print "Dir.: \"" + filename + "\" already made!"

def path (): return os.getcwd()

def chdir( path ): os.chdir( path )

set_file( "python_file", "Python file\npython" )
print get_file( "python_file" )
print is_file( "python_file" )
remove( "python_file" )
mkdir( "Python" ) # if make a dir that already is, err
remove( "Python" ) # rmves dir
chdir( "/" ) # gets to a dir
print path() # gives our dir


print have_ext( "file.py" )

filename = get_filename( "file.py" )
ext = get_ext( "file.py" )


print filename
print ext
