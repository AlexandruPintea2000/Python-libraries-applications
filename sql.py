import MySQLdb


def get_databases ():
	conn = MySQLdb.connect("localhost","root","" )
	crs = conn.cursor();
	
	# execute SQL query using execute() method.
	crs.execute( "SHOW DATABASES;" )

	# Fetch a single row using fetchone() method.
	dbs_tuples = crs.fetchall()

	dbs = []
	for i in dbs_tuples:
		dbs.extend( i )

	return dbs

def get_db_conn ( db ):
	conn = MySQLdb.connect("localhost","root","", db )
	return conn.cursor();	

def get_tables ( db ):
	conn = MySQLdb.connect("localhost","root","", db )
	db = conn.cursor();	
	
	# execute SQL query using execute() method.
	db.execute( "SHOW TABLES;" )

	# Fetch a single row using fetchone() method.
	table_tuples = db.fetchall()

	tables = []
	for i in table_tuples:
		tables.extend( i )

	return tables



for i in range( 1, 10000 ):
	dbs = get_databases()

	print "\033cDatabases:"
	if ( len( dbs ) == 0 ):
		print "Does not have databases."
	else:
		for i in range( len( dbs ) ):
			print " " + str( i + 1 ) + ". " + dbs[ i ]
		print " " + "exit. Exits"

	db_id = raw_input( "Db: " )
	if ( db_id == "exit" ):
		print "Exited."
		break
	else:
		db_id = int( db_id )

	db = ""
	for i in range ( len( dbs ) ):
		if ( db_id == i + 1 ):
			db = dbs[ i ]
			break

	print "\033c\"" + db + "\" tables: "





	tables = get_tables( db )

	if ( len( tables ) == 0 ):
		print "Does not have tables."
	else:
		for i in range( len( tables ) ):
			print " " + str( i + 1 ) + ". " + tables[ i ]

	con = raw_input( "[ ']' + Enter ] to continue: " )
	

