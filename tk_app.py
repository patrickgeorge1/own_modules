from tkinter import *

window = Tk()
window.title("Test")
window.resizable(0, 0)

#button = Button(text="First")
#button.grid()

class Application(Frame):
	"""app = Application(Frame_Name).grid()"""
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.createWidgets()

	def createWidgets(self):

		self.display = Entry(self, font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
		self.display.insert(0, "Text la misto")
		self.display.grid(row = 0, column = 0)


app = Application(window).grid()

window.mainloop()