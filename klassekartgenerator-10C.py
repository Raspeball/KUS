import random
import numpy as np
#
#
#
#
# Define names and seatmap #
# list and dic
def Klasse10C():
    navneliste = ["Mohammad", "Sarah", "Liselotte", "Helga", "Tiril",
            "Rateb", "Mohamed Yassin", "Mohamed", "Dani", "Oliver",
            "Sofie", "Zara", "Storm", "Markus", "Noah", "Mathea", "Ida"]
    
    navnedic = {i+1:navn for i, navn in enumerate(navneliste)}

    
    return navnedic

# define flags as global for the purpose of this particular class only
flags = [12, 5, 6, 10]

def Seatmap():
    # coordinates: number of students
    layout = {"foran venstre":2, "foran midten":2, "foran høyre":2,
              "midten venstre":2, "midten midten":2, "midten høyre":2,
              "bak venstre":2, "bak høyre": 3}
    
    return layout
#
#
# Define generator #
#
def MakeGrupper(navnedic):#, kartdic):
    # ensure klassekart is a go wrt flags
    go = False
    
    # randomization (can't shuffle dic)
    while go == False:
        #
        grupper = []
        #
        elever = list(navnedic.keys())
        random.shuffle(elever)

        #groups of two
        for i in range(0, len(elever)-3, 2):
            grupper.append(elever[i:i+2])
        
        #last group of three
        grupper.append(elever[-3:])
        
        #check for flags
        f = flags[0]
        for group in grupper:
            if (f and flags[1] in group) or (f and flags[2] in group) or (f and flags[3] in group):
                go = False
            else:
                go = True
                return grupper

# Testing #
test = MakeGrupper(Klasse10C())
print(test)
    






