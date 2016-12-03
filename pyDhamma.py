# Ben Woodfield - Random Line Grabber
# Added the first Chapter to the text file (Pairs)
# Has 20 verses - each verse is 1 line in a text file
# The program displays a random line / verse

'''
    TODO
    Do a GUI version in TK
    Add the while book to the text file...
    or...add each chapter to a separate text file,
    then ask the user to select a chapter using input
    showing verses from that chapter..I don't know yet!

    I got 2 PDF's to grab the verses, but had trouble copy/pasting verses,
    so used this link to see the verse contents:
    http://www.accesstoinsight.org/tipitaka/kn/dhp/dhp.01.budd.html
'''

#!usr/bin/env python
import random

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

def restart_program():
        while True:
            restart = input("\n\nDo you want to see another verse? \nType '1' for Yes and 2 for No \n>>> ")
            if restart == 1:
                print '\n',random_line()
            else:
                print "Have a good Day"
                break


print random_line()
restart_program()
