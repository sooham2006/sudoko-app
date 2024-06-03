from tkinter import *
import os
 
root = Tk()
root.geometry("700x700+380+70")
 
 
def set_difficulty():
	root.withdraw()
	os.system("python game.py")
	root.deiconify()

img = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//my2.png")
imgbutton = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//play.png")
imgdiff = PhotoImage(file = "/Users//Carl//Desktop//PlaySudoku//Images//diff2.png")



label1 = Label(root,image = img)
label1.place(relx=0, rely=0, width=700, height=700)


button1 = Button(root,image = imgbutton)

button1.place(relx=0.65, rely=0.73, width=160, height=80)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffde59")
button1.configure(cursor="hand2")
button1.configure(borderwidth="0")
button1.configure(command = set_difficulty)


root.mainloop()