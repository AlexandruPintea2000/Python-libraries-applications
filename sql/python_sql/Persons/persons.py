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


class Person:

	def __init__ ( self, id, firstname, lastname, email, date, type, gender, inter ):
		self.id = id
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.date = date
		self.type = type
		self.gender = gender
		self.inter = inter




	def get_id ( self ): return self.id
	def get_firstname ( self ): return self.firstname
	def get_lastname ( self ): return self.lastname
	def get_email ( self ): return self.email
	def get_date ( self ): return self.date
	def get_type ( self ): return self.type
	def get_gender ( self ): return self.gender
	def get_inter ( self ): return self.inter


	def __str__ ( self ):
		person_string =  "Person ";
		person_string = person_string + "id = " + str( self.id )
		person_string = person_string + ": firstname = " + str( self.firstname )
		person_string = person_string + ", lastname = " + str( self.lastname )
		person_string = person_string + ", email = " + str( self.email )
		person_string = person_string + ", date = " + str( self.date )
		person_string = person_string + ", type = " + str( self.type )
		person_string = person_string + ", gender = " + str( self.gender )
		person_string = person_string + ", inter = " + str( self.inter )
		return person_string



def get_persons ():
	db = Database( "localhost", "root", "", "python" )
	table = Table( "persons", db )
	
	rows = table.get_table();

	persons = []
	for i in range( 0, len( rows ) ):
		if ( i % 8 != 0 ): continue
		persons.append( Person( rows[ i ], rows[ i + 1 ], rows[ i + 2 ], rows[ i + 3 ], rows[ i + 4 ], rows[ i + 5 ], rows[ i + 6 ], rows[ i + 7 ] ) )

	return persons



def show_persons ():
	db = Database( "localhost", "root", "", "python" )
	table = Table( "persons", db )
	
	rows = table.get_table();

	title = [ "Id", "Firstname", "Lastname", "Email", "Date", "Type", "Gender", "Inter" ]
	maxlen = [ 0, 0, 0, 0, 0, 0, 0, 0 ]

	for i in range( len( title ) ):
		if ( len( str( title[ i ] ) ) > maxlen[ i % 8 ] ):
			maxlen[ i % 8 ] = len( str( title[ i ] ) )

	for i in range( len( rows ) ):
		if ( len( str( rows[ i ] ) ) > maxlen[ i % 8 ] ):
			maxlen[ i % 8 ] = len( str( rows[ i ] ) )

	for i in range( len( title ) ):
		print title[ i ],
		for l in range(  len( str( title[ i ] ) ), maxlen[ i % 8 ] ):
			print "",
		print "",

	print "\n------------------------------------------------------------------",

	for i in range( len( rows ) ):
			if ( i % 8 == 0 ): print ""
			print rows[ i ],
			for l in range(  len( str( rows[ i ] ) ), maxlen[ i % 8 ] ):
				print "",
			print "",


if ( have_db( "localhost", "root", "", "python" ) == 0 ):
	create_db( "localhost", "root", "", "python" )
	print "Created db \"python\"."

db = Database( "localhost", "root", "", "python" )

if ( db.have_table( "persons" ) == 0 ):
	names = [ "firstname", "lastname", "email", "date", "type", "gender", "inter" ]
	types = [ "varchar( 255 )", "varchar( 255 )", "varchar( 255 )", "date", "int", "int", "int" ]
	db.create_table( "persons", names, types )
	print "Created table \"persons\"."


print db.get_tables()

table = Table( "persons", db )


row = [ table.get_id(), "fname", "lname", "email", "2005-10-10", 1, 0, 1 ]
# table.insert_row( row )
# row = [ 1, "fname", "lname", "email", "2005-10-10", 1, 0, 1 ]
# table.insert_row( row )
# print table.get_row_through_id( 0 )
# row = [ 0, "fname_0", "lname_0", "email_0", "2005-10-10", 1, 0, 1 ]
# table.update_row( row )
# print table.get_row_through_id( 0 )


show_persons()
