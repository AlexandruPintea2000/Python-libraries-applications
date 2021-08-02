o = 1
print(o)

atrib_iter = 0
cls_iter = 0

atrib = [""] * 1000;
cls = [""] * 1000;

atrib_val = [""] * 1000;
cls_val = [""] * 1000;



filename = raw_input( "Filename: " );

def get_lines( filename ):
	with open( filename ) as f:
		lines = f.readlines()
	for i in lines:
		i = i[:len(i) - 1]
	return lines;

def get_file( filename ):
	with open( filename, 'r') as file:
		data = str( file.read().replace( '\n', '' ) )
	return data

def print_array( arr ):
	for i in range( len( arr ) ):
		if arr[ i ] == "":
			break
		print( arr[ i ] )

def had( arr, pos ):
	for i in range( pos ):
		if arr[ pos ] == arr[ i ]:
			return 1
	return 0

data = get_file( filename );
for i in range( len( data ) ):
	if data[ i ] == '[':
		i = i + 1
		while data[ i ] == ' ' or data[ i ] == '	':
			i = i + 1
		
		while data[ i ] != ' ' and data[ i ] != '	':
			atrib[ atrib_iter ] = atrib[ atrib_iter ] + data[ i ]
			i = i + 1
		
		while data[ i ] == ' ' or data[ i ] == '	':
			i = i + 1

		while data[ i ] == ']':
			i = i + 1

		if data[ i ] == '{':
			while 1:
				i = i + 1
				if data[ i ] == '}':
					break
				atrib_val[ atrib_iter ] = atrib_val[ atrib_iter ] + data[ i ]

		atrib_iter = atrib_iter + 1;

	if data[ i ] == '.':
		i = i + 1
		while data[ i ] != ' ' and data[ i ] != '	' and data[ i ] != '{':
			cls[ cls_iter ] = cls[ cls_iter ] + data[ i ]
			i = i + 1
	
		if i <= len( data ) - 1:
			while data[ i ] != '{':
				i = i + 1

		while 1:
			i = i + 1
			if data[ i ] == '}':
				break
			cls_val[ cls_iter ] = cls_val[ cls_iter ] + data[ i ]

		cls_iter = cls_iter + 1;



fo = open( "result", "w+" )

def print_atrib( atrb ):
	result = "[ " + atrb + " ]\n{\n"
	for i in range( atrib_iter ):
		if atrib[ i ] == atrb:
			result = result + atrib_val[ i ] + "\n"
	result = result + "}\n\n";
	return result

def print_cls( cl ):
	result = "." + cl + "\n{\n"
	for i in range( cls_iter ):
		if cls[ i ] == cl:
			result = result + cls_val[ i ] + "\n"
	result = result + "}\n\n";
	return result

for i in range( atrib_iter ):
	if had( atrib, i ) == 0:
		fo.write( print_atrib( atrib[ i ] ) )

for i in range( cls_iter ):
	if had( cls, i ) == 0:
		fo.write( print_cls( cls[ i ] ) )

