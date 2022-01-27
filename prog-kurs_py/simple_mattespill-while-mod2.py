import random

ant_oppgaver = 5
liv = 4

for i in range(ant_oppgaver):

    faktor1 = random.randint(2, 10)
    faktor2 = random.randint(2, 10)

    fasit = faktor1*faktor2

    print("Hva er ", faktor1, "ganger", faktor2, "?")

    svar = int(input("Skriv inn svaret ditt: "))

    while svar != fasit:
        print("Dessverre ikke riktig")
        liv = liv - 1
        print("Du har", liv, "liv igjen")

        if liv != 0:
            svar = int(input("Prøv igjen: "))

        else:
            print("Beklager, du har 0 liv igjen, og har tapt.")
            break

    print("Yay, riktig.")

print("Gratulerer, du fullførte alle oppgavene")

# holder
