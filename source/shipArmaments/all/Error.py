from tkinter import *

def importFTLRand():
	import Program

test = Tk()
test.geometry("200x100")
test.title("Error Checker")


btnCheck = Button(test, text='check', command=importFTLRand)
btnCheck.grid(row=0, column=0)


test.mainloop()
