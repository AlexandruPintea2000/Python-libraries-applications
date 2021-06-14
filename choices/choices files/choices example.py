choices = [ "choice1", "choice_choice2", "choice3", "choice4", "choice5", "choice1", "choice2", "choice3", "choice4", "choice5" ]


def is_numeric ( a ):
	if ( len(a) == 0 ): return 0

	for i in range( len( a ) ):
		if ( a[ i ] >= '0' and a[ i ] <= '9' ): continue
		else: return 0;
	return 1




def enter ():
	a = raw_input( "[ \']\' + Enter ] to continue: " )



def show_choices():

	print "Available choices: "

	maxlen = [ 0, 0, 0, 0, 0 ]
	for i in range( len( choices ) ):
		if ( len( choices[ i ] ) > maxlen[ i % 5 ] ):
			maxlen[ i % 5 ] = len( choices[ i ] )

	for i in range( len( choices ) ):
		print " ",
		print str( i + 1 ) + ". " + choices[ i ],
		for l in range( len( choices[ i ] ), maxlen[ i % 5 ] ): print "",
		if ( ( i + 1 ) % 5 == 0 and i + 1 != len( choices ) ):
			print "\n",
	print "\n  exit. Exits"


def get_choice ():
	choice = raw_input( "\n Choice: " )

	if ( is_numeric( choice ) == 0 and choice != "exit" ): return




	if ( choice == 1 ):
		code = 1 # your code




	if ( choice == "exit" ):
		print " Exited.\n";

	return choice

print "\033c",
show_choices()
while ( get_choice() != "exit" ):
	print "\033c",
	show_choices()


