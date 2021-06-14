



class Graph:

	def __init__( self, arr, oriented = 0 ):
		self.arr = arr;
		maxim = 0
		for i in arr:
			if ( i[ 0 ] > maxim ): maxim = i[ 0 ]
			if ( i[ 1 ] > maxim ): maxim = i[ 1 ]
		self.size = maxim + 1
		if ( oriented != 0 and oriented != 1 ):
			self.oriented = 1
		else:
			self.oriented = oriented


	def __str__( self ):
		string = "";
		for l1 in range( 0, self.size ):
			for l2 in range( 0, self.size ):
				if ( self.is_in( [ l1, l2 ] ) ): string = string + "1 "
				else: string = string + "0 "
			if ( l1 != self.size - 1 ):
				string = string + "\n"
		return string

	def is_in ( self, arr ):
		if ( self.oriented != 0 ):
			for i in self.arr:
				if ( i[ 0 ] == arr[ 0 ] and i[ 1 ] == arr[ 1 ] ): return 1
		else:
			for i in self.arr:
				if ( i[ 0 ] == arr[ 0 ] and i[ 1 ] == arr[ 1 ] ): return 1
				if ( i[ 0 ] == arr[ 1 ] and i[ 1 ] == arr[ 0 ] ): return 1

		return 0



	def get_size ( self ):	return self.size
	def get ( self ): return self.arr
	def get_oriented( self ): return self.oriented

	def set ( self, arr ): self.arr = arr
	def set_oriented( self ): self.oriented = oriented




arr = [ [ 0, 1 ], [ 1, 2 ], [ 0, 2 ], [ 1, 5 ] ]
graph = Graph( arr )
print graph
