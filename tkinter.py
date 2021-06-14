import Tkinter
from Tkinter import *
import tkMessageBox
top = Tkinter.Tk()
top.title( "Python" )

top.minsize( 250, 150 )
top.maxsize( 250, 150 )

def message():
	if ( str( firstname.get() ) != "" and str( lastname.get() ) != "" ):
		tkMessageBox.showinfo( "Welcome!", "Welcome to Python, " + str( firstname.get() ) + ' ' + str( lastname.get() ) + " !")
	else:
		tkMessageBox.showinfo( "Requirement", "Please enter your full name!" )	

B = Tkinter.Button(
top, text ="Hello",
activebackground="#a1a1a1",
padx = 41,
pady = 3,

bd=1,
command=message )


fname_label = Label(top, text="Firstname: ")
fname_label.pack()

firstname = Entry(top, bd=1)
firstname.pack()

lname_label = Label(top, text="Lastname: ")
lname_label.pack()

lastname = Entry(top, bd=1)
lastname.pack()
B.pack()


top.mainloop()

