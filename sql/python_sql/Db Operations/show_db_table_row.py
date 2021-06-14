import MySQLdb



def get_databases ( server, user, password ):
	conn = MySQLdb.connect( server, user, password )
	crs = conn.cursor();

	# execute SQL query using execute() method.
	crs.execute( "SHOW DATABASES;" )
	dbs_tuples = crs.fetchall()

	dbs = []
	for i in dbs_tuples:
		dbs.extend( i )

	conn.close();

	return dbs

def have_db ( server, user, password, db ):
	dbs = get_databases( server, user, password )

	for i in dbs:
		if ( i == db ):
			return 1
	return 0


def create_db ( server, user, password, db ):
	conn = MySQLdb.connect( server, user, password )
	crs = conn.cursor();

	# execute SQL query using execute() method.
	crs.execute( "CREATE DATABASE " + db + ";" )
	conn.close();


class Database:

	def get_server ( self ): return self.server
	def get_user ( self ): return self.user
	def get_password ( self ): return self.password
	def get_db ( self ): return self.db
	def get_conn ( self ): return self.conn

	def __init__ ( self, server, user, password, db ):
		self.server = server
		self.user = user
		self.password = password
		self.db = db
		conn = MySQLdb.connect( self.server, self.user, self.password, self.db )
		self.conn = conn.cursor()


	def __str__ ( self ):
		return "Database: " + self.db

	def get_tables ( self ):
		conn = MySQLdb.connect( self.server, self.user, self.password, self.db )
		db = conn.cursor();	
	
		# execute SQL query using execute() method.
		db.execute( "SHOW TABLES;" )
		table_tuples = db.fetchall()

		tables = []
		for i in table_tuples:
			tables.extend( i )

		return tables

	def have_table ( self, table ):
		tables = self.get_tables();

		for i in tables:
			if ( i == table ):
				return 1
		return 0


	def create_table ( self, table, names, types ):
		if ( len( names ) != len( types ) ):
			print "Length of 'names' != Length of 'types'!"
			return

		sql = "CREATE TABLE " + table + " ( ";
		
		size = len( names )
		sql = sql + "\n	id int,";
		for i in range( 0, size ):
			sql = sql + "\n	" + names[ i ] + " " + types[ i ] + ","

		sql = sql + "\n	PRIMARY KEY (id)";
		sql = sql + "\n);"

		print sql

		self.conn.execute( sql )


		def __del__ ( self ):
			self.conn.close()


class Table(Database):

	def __init__ ( self, table, db ):
		if ( db.have_table( table ) == 0 ):
			print "Database \"" + db.get_db() + "\" does not have table '" + table + "'."
			return
		self.table = table


		self.server = db.get_server()
		self.user = db.get_user()
		self.password = db.get_password()
		self.db_name = db.get_db()

		conn = MySQLdb.connect( self.server, self.user, self.password, db.get_db() )
		db_conn = conn.cursor()

		db_conn.execute( "DESC " + table + "; " )
		column_tuples = db_conn.fetchall()

		names = []
		types = []
		for i in column_tuples:
			names.append( i[ 0 ] )
			types.append( i[ 1 ] )

		self.names = names
		self.types = types

		self.conn = db.get_conn()

	def __str__ ( self ):
		return "Table: " + self.table


	def get_table_name ( self ): return self.table
	def get_names ( self ): return self.names
	def get_types ( self ): return self.types

	def insert_row ( self, row ):
		size = len( self.names )
		if ( len( row ) != size ):
			print "Length of row is: " + len( row ) + ", but should be: " + size;
			return
		sql = "INSERT INTO " + self.table + " ( "
		for i in range( 0, size ):
			sql = sql + self.names[ i ];
			if ( i != size - 1 ):
				sql = sql + ", "
		sql = sql + " ) VALUES ( "
		for i in range( 0, size ):
			sql = sql + "\"" + str( row[ i ] ) + "\"";
			if ( i != size - 1 ):
				sql = sql + ", "
		sql = sql + " );"

		db_conn = MySQLdb.connect( self.server, self.user, self.password, self.db_name )
		db_conn.cursor().execute( sql )
		db_conn.commit()
		db_conn.close()

	def update_row ( self, row ):
		size = len( self.names )
		if ( len( row ) != size ):
			print "Length of row is: " + len( row ) + ", but should be: " + size;
			return
		sql = "UPDATE " + self.table + "\n"
		sql = sql + "SET "
		for i in range( 1, size ):
			sql = sql + self.names[ i ] + "=\"" + str( row[ i ] ) + "\"";
			if ( i != size - 1 ):
				sql = sql + ", "
		sql = sql + "\n WHERE id=" + str( row[ 0 ] ) + "; "

		db_conn = MySQLdb.connect( self.server, self.user, self.password, self.db_name )
		db_conn.cursor().execute( sql )
		db_conn.commit()
		db_conn.close()

	def get_row_through_id ( self, id ):
		self.conn.execute( "SELECT * FROM " + self.table + " WHERE id=" + str( id ) + "; " )
		row_tuples = self.conn.fetchall()

		row = []
		for i in row_tuples:
			row.extend( i )

		return row

	def delete_row_through_id ( self, id ):
		db_conn = MySQLdb.connect( self.server, self.user, self.password, self.db_name )
		db_conn.cursor().execute( "DELETE FROM " + self.table + " WHERE id=" + str( id ) + "; " )
		db_conn.commit()
		db_conn.close()


	def get_table ( self ):
		self.conn.execute( "SELECT * FROM " + self.table + "; " )
		row_tuples = self.conn.fetchall()

		row = []
		for i in row_tuples:
			row.extend( i )

		return row

	def get_id ( self ):
		rows = self.get_table()

		id = 0;
		for i in range( 0, len( rows ) ):
			if ( i % len( self.names ) != 0 ):
				continue;

			if ( rows[ i ] == id ):
				id = id + 1
			else: 
				return id

		return id





def show_table ( table, db ):
	db = Database( "localhost", "root", "", db.get_db() )
	table = Table( table.get_table_name(), db )
	
	rows = table.get_table()

	title = table.get_names()
	size = len( title )

	for i in range( size ):
		title[ i ] = title[ i ].title()
	title[ 0 ] = " " + title[ 0 ]

	maxlen = []

	for i in range( len( title ) ):
		maxlen.append( 0 )

	for i in range( len( title ) ):
		if ( len( str( title[ i ] ) ) > maxlen[ i % size ] ):
			maxlen[ i % size ] = len( str( title[ i ] ) )

	for i in range( len( rows ) ):
		if ( len( str( rows[ i ] ) ) > maxlen[ i % size ] ):
			maxlen[ i % size ] = len( str( rows[ i ] ) )


	print "\033c\"" + db.get_db() + "\" / \"" + table.get_table_name() + "\" rows: \n"


	for i in range( len( title ) ):
		print title[ i ],
		for l in range(  len( str( title[ i ] ) ), maxlen[ i % size ] ):
			print "",
		print "",

	print ""




	for i in range( len( rows ) ):
		if ( i % size == 0 ): 
			print ""
			rows[ i ] = " " + str( rows[ i ] )
		print rows[ i ],
		for l in range(  len( str( rows[ i ] ) ), maxlen[ i % size ] ):
			print "",
		print "",



for i in range( 1, 10000 ):
	dbs = get_databases( "localhost", "root", "" )

	print "\033cDatabases:"
	if ( len( dbs ) == 0 ):
		print "Does not have databases."
		print "Exited."
		break
	else:
		for i in range( len( dbs ) ):
			print " " + str( i + 1 ) + ". " + dbs[ i ]
		print " " + "exit. Exits"

	db_id = raw_input( "Db: " )

	if ( db_id.isdigit() == 0 and db_id != "exit" ): 
		print "Invalid. Exited."
		break;

	if ( db_id == "exit" ):
		print "Exited."
		break
	else:
		db_id = int( db_id )

	if ( db_id <= 0 ): 
		print "Invalid. Exited."
		break;

	if ( db_id > len( dbs ) ): 
		print "Invalid. Exited."
		break;

	db = ""
	for i in range ( len( dbs ) ):
		if ( db_id == i + 1 ):
			db = dbs[ i ]
			break

	print "\033c\"" + db + "\" tables: "

	db = Database( "localhost", "root", "", db )

	tables = db.get_tables()

	if ( len( tables ) == 0 ):
		print "Does not have tables."
		con = raw_input( "[ ']' + Enter ] to continue: " )
		continue
	else:
		for i in range( len( tables ) ):
			print " " + str( i + 1 ) + ". " + tables[ i ]

	table_id = raw_input( "Table: " )

	if ( table_id.isdigit() == 0 ): 
		print "Invalid. Exited."
		break;

	table_id = int( table_id )


	if ( table_id <= 0 ): 
		print "Invalid. Exited."
		break;

	if ( table_id > len( tables ) ): 
		print "Invalid. Exited."
		break;

	table_id = int( table_id )

	table = ""
	for i in range ( len( tables ) ):
		if ( table_id == i + 1 ):
			table = tables[ i ]
			break

	table = Table( table, db )
	show_table( table, db )

	con = raw_input( "\n\n[ ']' + Enter ] to continue: " )
