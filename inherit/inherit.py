x = 4
print(x)

fi = open( "file", "r+" )
data = fi.read()
fi.close()

for i in range( len( data ) ):
	if data[ i ] == '':
