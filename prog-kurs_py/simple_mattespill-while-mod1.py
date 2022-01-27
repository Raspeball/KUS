import random

ant_oppgaver = 5

for i in range(ant_oppgaver):

    faktor1 = random.randint(2, 10)
    faktor2 = random.randint(2, 10)

    fasit = faktor1*faktor2

    print("Hva er ", faktor1, "ganger", faktor2, "?")

    svar = int(input("Skriv inn svaret ditt: "))

    while svar != fasit:
        print("dessverre ikke riktig")

        svar = int(input("Prøv igjen: "))

    print("Yay, riktig.")
    # Vi trenger ingen if og else her
    # for while-løkka vil holde det gående helt
    # til vi har svart riktig
    # da trenger vi heller ikke å telle antall riktige

print("Gratulerer, du fullførte alle oppgavene")

# holder
