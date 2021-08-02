o = 1
print(o)

atrib_iter = 0
cls_iter = 0

atrib = [""] * 1000;
cls = [""] * 1000;

filename = raw_input( "Filename: " );

def get_lines( filename ):
	with open( filename ) as f:
		lines = f.readlines()
	for i in lines:
		i = i[:len(i) - 1]
	return lines;

def get_file( filename ):
	with open( filename, 'r') as file:
		data = str( file.read().replace('\n', '') )
	return data


data = get_file( filename );
for i in range( len( filename ) ):
	if data[ i ] == '[':
		while data[ i ] == ' ' or data[ i ] == '	':
			i = i + 1
		
		while data[ i ] != ' ' and data[ i ] != '	':
			atrib[ atrib_iter ] = atrib[ atrib_iter ] + data[ i ]
			print( data[ i ] + ' ' )
			i = i + 1
		
		while data[ i ] == ' ' or data[ i ] == '	':
			i = i + 1

		while data[ i ] == ']':
			i = i + 1
		i = i + 1

		print( atrib[ atrib_iter ] )
		atrib_iter = atrib_iter + 1;


		
