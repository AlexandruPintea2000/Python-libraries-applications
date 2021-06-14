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




import os
def mkdir ( filename ):
	if ( os.path.isdir( filename ) == 0 ): os.mkdir( filename )


def is_numeric ( a ):
	if ( len(a) == 0 ): return 0

	for i in range( len( a ) ):
		if ( a[ i ] >= '0' and a[ i ] <= '9' ): continue
		else: return 0;
	return 1


class Counter:

	def get_counter_id (self):
		if ( os.path.isfile( "counter_num" ) == 0 ): 
			set_file( "counter_num", "1" )
			count = 1
			for i in range(1, 1000):
				if ( os.path.isfile( "counter_" + str( i ) ) ):
					count = i
			set_file( "counter_num", str( count + 1 ) )
			return 1
		else:
			if ( is_numeric( get_file( "counter_num" ) ) == 0  ):
				for i in range(1, 1000):
					if ( os.path.isfile( "counter_" + str( i ) ) ):
						count = i
					else: break
				count = count + 1
			else:
				count = int( get_file( "counter_num" ) )				
			set_file( "counter_num", str( count + 1 ) )
			return count


	def __init__( self, counter_id = -1 ):
		mkdir( "counters" )
		path = os.getcwd()
		os.chdir( "counters" )
		if ( counter_id == -1 ):
			self.num = 0
			self.counter_id = self.get_counter_id()
			set_file( "counter_" + str( self.counter_id ), "0" )
		else:
			if ( os.path.isfile( "counter_" + str( counter_id ) ) ):
				filename = "counter_" + str( counter_id )
				if ( is_numeric( get_file( filename ) ) == 0 ):
					self.num = 0
					set_file( filename, "0" )
				else:
					self.num = int( get_file( filename ) )
				self.counter_id = counter_id
			else:
				if ( is_numeric( get_file( "counter_num" ) ) == 1 ):
					if ( int( get_file( "counter_num" ) ) < counter_id ):
						self.num = 0
						self.counter_id = int( get_file( "counter_num" ) )
						print "Counter \"" + str( counter_id ) + "\" invalid! Count !saved."
						print "Counters available: 0 - " + get_file( "counter_num" )
					else:
						self.num = 0
						self.counter_id = counter_id
						set_file( "counter_" + str( counter_id ), "0" )
				else:
					self.num = 0
					count = 1;
					for i in range(1, 1000):
						if ( os.path.isfile( "counter_" + str( i ) ) ):
							count = i
					count = count + 1
					self.counter_id = count		
					set_file( "counter_num", str( count + 1 ) )
		os.chdir( path )
	
#	def __del__( self ):
#		path = os.getcwd()
#		os.chdir( "counters" )
#		os.remove( "counter_" + str( self.counter_id ) )
#		os.chdir( path )
		
	def __add__ ( self, num ):
		self.num = self.num + num
		path = os.getcwd()
		os.chdir( "counters" )
		self.num = int( self.num )
		if ( self.num < 0 ): self.num = 0
		set_file( "counter_" + str( self.counter_id ), str( self.num ) )
		os.chdir( path )

	def __sub__ ( self, num ):
		self.num = self.num - num
		path = os.getcwd()
		os.chdir( "counters" )
		self.num = int( self.num )
		if ( self.num < 0 ): self.num = 0
		set_file( "counter_" + str( self.counter_id ), str( self.num ) )
		os.chdir( path )

	def __str__( self ):
		return str( self.num )

	def get_count( self ): return self.num
	def get_id( self ): return self.counter_id

counter = Counter()
counter + 1.5
print counter
