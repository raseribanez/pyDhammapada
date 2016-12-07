# Ben Woodfield
# 03/12/2016
# Verses from the Dhammapada
# A book written from a collection of wise sayings in Buddhism
# The sayings were from Siddartha Gautama - or as we know him - Buddha
#
# The book is freely available for non-profit copying and sharing
# I have included Every verse from all of the chapters.
#
# This GUI version allows the user to click a button to see a random verse
# and displays the text in the Shell window.
#
# Written in Python 3
# Uses Tkinter - needs no additional modules installed

import random
import Tkinter as tk
from Tkinter import *

''' This class template was my original one. It includes a lot of arguments of which
    I feel my level of programs don't need. I have since made a lighter class template
    for my GUI apps and plan to update them all soon. For now I have commented out any
    un-needed args '''

class MainApplication(tk.Frame):
    def __init__(self, parent):  #, *args, **kwargs):
        tk.Frame.__init__(self, parent)  #, *args, **kwargs)
        self.parent = parent

        def random_line():
            line_num = 0
            selected_line = ''
            with open('dhammapada.txt') as f:
                while 1:
                    line = f.readline()
                    if not line: break
                    line_num += 1
                    if random.uniform(0, line_num) < 1:
                        selected_line = line
                        
            return selected_line.strip()

        # Py 3 required the print parentheses
        def print_a_verse():
            print (random_line())
            print ("\n")

        btn_result = Button(self, fg='Red', text='New Verse', bg='Black', font='freesansbold, 16', command=print_a_verse) #textvariable=cvt_to, font='freesansbold, 16', fg='Blue')
        btn_result.pack(fill=X,side=TOP)#fill=BOTH, expand=1)

        lbl_one = Label(self, bg='DarkGrey', fg='White',  text='Dhammapada', font='freesansbold, 22')
        lbl_one.pack(fill=BOTH, expand=1)

        lbl_thr = Label(self, bg='DarkGrey', fg='White', text='The Dhammapada \nSiddartha Gautama - Buddha', font='freesansbold, 18')
        lbl_thr.pack(fill=BOTH, expand=1)

        lbl_two = Label(self, bg='DarkGrey', fg='Grey', text='"Assembled from the sayings of Gautama \nGiven on some three hundred different occasions \nThe philosophies and wisdom within these verses \nAre still applicable \nEven in our modern times.\nBen Woodfield"', font='freesans, 16')
        lbl_two.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400,400)
    #root.configure(bg='Black')
    root.title('Python - Dhammapada Verses')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
