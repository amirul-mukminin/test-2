# Question 1:
# [10 marks]
# [CO1/PO1/C4]
# As a developer, you must analyse and create a subclass of Frame 
# which it automatically becomes an attachable component. 
# You can add all of the widgets this class creates, as a package, 
# to any other GUI, just by attaching this Frame to the GUI."""

from sys import exit
from Tkinter import *                   


class Hello(Frame):                     
    def __init__(self, parent=None):
        Frame.__init__(self, parent)    
        self.pack()
        self.data = 42
        self.make_widgets()             
    def make_widgets(self):
        widget = Button(self, text='Button!', command=self.message)
        widget.pack(side=LEFT)
    def message(self):
        self.data = self.data + 1
        print 'Hello frame world %s!' % self.data

parent = Frame(None)                     
parent.pack()
Hello(parent).pack(side=RIGHT)           

Button(parent, text='Text', command=exit).pack(side=LEFT)
parent.mainloop()