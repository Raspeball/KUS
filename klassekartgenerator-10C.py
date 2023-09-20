import random
import numpy as np
# markdown
import Mdutils
#
#
#
#
# Define names and seatmap #
# list and dic
#
def Klasse10C():
    navneliste = ["Mohammad", "Sarah", "Liselotte", "Helga", "Tiril",
            "Rateb", "Mohamed Yassin", "Mohamed", "Dani", "Oliver",
            "Sofie", "Zara", "Storm", "Markus", "Noah", "Mathea", "Ida"]
    
    navnedic = {i+1:navn for i, navn in enumerate(navneliste)}

    
    return navnedic

# define flags as global for the purpose of this particular class only
flags = [12, 5, 6, 10]

# Function to hold seatmap
def Seatmap():
    koord = ["foran venstre","foran midten","foran høyre","midten venstre","midten midten","midten høyre","bak venstre","bak høyre"]
    
    # all but the largest key in layout dic hold 2 students
    layout = {i+1: pos for i, pos in enumerate(koord)}
    
    return layout
#
#
#
# Make groups of students
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
#
#
# Make the final seatmap
def MakeKlassekart(grupper, navnedic, kartdic):
    # generate a printable/showable seatmap
    # grupper is a list of lists of ints
    # navnedic is a dic of int:names
    # kartdic is numberofstudents:coordinates
    
    posisjoner = list(kartdic.values())
    klassekart = {pos:"" for pos in posisjoner}

    for nr, group in enumerate(grupper):
        names = [navnedic[i] for i in group]

        klassekart[posisjoner[nr]] = names
    
    return klassekart
#
#
# Generate seat map as markdown
def GenerateMdFile(finalseatmap):
    # create file
    mdFile = Mdutils(file_name = "klassekart-10C", title = "Klassekart 10C uke XX")
    mdFile.create_md_file()




# Testing #
#test = MakeGrupper(Klasse10C())
grupper = MakeGrupper(Klasse10C())
test2 = MakeKlassekart(grupper, Klasse10C(), Seatmap())
print(test2)

    






