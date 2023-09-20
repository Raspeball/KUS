import random
#
#
#
#
# Define names and seatmap #
# list
def Klasse10C():
    navneliste = ["Mohammad", "Sarah", "Liselotte", "Helga", "Tiril",
            "Rateb", "Mohamed Yassin", "Mohamed", "Dani", "Oliver",
            "Sofie", "Zara", "Storm", "Markus", "Noah", "Mathea", "Ida"]
    
    return navnliste

def Seatmap():
    layout = {"foran venstre":2, "foran midten":2, "foran høyre":2,
              "midten venstre":2, "midten midten":2, "midten høyre":2,
              "bak venstre":2, "bak høyre": 3}
    
    return layout
#
#
# Define generator #
#
def MakeKlassekart(navneliste, kartdic):
    # ensure klassekart is a go wrt flags
    go = "False"
    
    # randomization (can't shuffle dic)
    while go == False:
        random.shuffle(navneliste)
        navnedic = {navn:"" for navn in navneliste}
        # set flags
        flags = ["Rateb", "Tiril", "Oliver"]
        for ele in flags:
            navnedic[ele] = "x"
        
        #mapping
        kart = []
        for g in kartdic.values():
            kart.append(["seat"]*g)
        
        
        
        
        
        

test = Klasse10C()
random.shuffle(test)
print(test)
    






