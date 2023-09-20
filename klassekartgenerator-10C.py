import random
import numpy as np
# markdown
from mdutils.mdutils import MdUtils
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
    # data is finalseatmap
    # create file
    mdFile = MdUtils(file_name ="klassekart_10C", title = "Klassekart 10C uke XX")
    

    # create tables
    pos = list(finalseatmap.keys())
    foran = pos[0:3]
    eleverforan = []
    #midten = pos[3:6]
    #bak = [pos[-3], "bak midten", pos[-1]]

    #for pos in foran:
    #    for elev in finalseatmap[pos]:
    #    foran.extend([elev[0] + elev[1], ])

    foran.extend(["omg", "lol", "hei"])
    
    mdFile.new_line()
    mdFile.new_table(columns = 3, rows = 2, text = foran, text_align = "center")
    mdFile.create_md_file()

# Generate seat map as text file
def GenerateTxtFile(finalseatmap):
    f = open("klasseklart_10C.txt", "a")

    # create rows
    pos = list(finalseatmap.keys())
    foran = pos[0:3]
    midten = pos[3:6]
    bak = [pos[-2], "bak midten", pos[-1]]

    rows = []
    sep = "  "*5
    
    # foran
    toprow1 = ""
    for i in foran:
        toprow1 += "|" + i + "|" + sep
    
    toprow2 = ""
    for par in foran:
        temp = ""
        for elev in finalseatmap[par]:
            temp += " " + elev
        toprow2 += "|" + temp + "|" + sep
    
    rows.append([toprow1, toprow2])

    # midten
    midrow1 = ""
    for i in midten:
        midrow1 += "|" + i + "|" + sep
    
    midrow2 = ""
    for par in midten:
        temp = ""
        for elev in finalseatmap[par]:
            temp += " " + elev
        midrow2 += "|" + temp + "|" + sep
    
    rows.append([midrow1, midrow2])

    # bakerst
    bakrow1 = ""
    for i in bak:
        bakrow1 += "|" + i + "|" + sep
    
    bakrow2 = ""
    for par in bak:
        temp = ""
        if par in finalseatmap.keys():
            for elev in finalseatmap[par]:
                temp += " " + elev
            bakrow2 += "|" + temp + "|" + sep
        else:
            bakrow2 += "|" + sep + "|" + sep
    
    rows.append([bakrow1, bakrow2])
    
    for row in rows:
        for line in row:
            f.write(line + "\n")
        f.write("\n\n")
    
    f.write("\n"+"-----------------------------------------------------------------------------------"+"\n\n")
    
    f.close() 
#
#
#
# Testing #
#test = MakeGrupper(Klasse10C())
grupper = MakeGrupper(Klasse10C())
klassekart = MakeKlassekart(grupper, Klasse10C(), Seatmap())
GenerateMdFile(klassekart)
#GenerateTxtFile(klassekart)
    






