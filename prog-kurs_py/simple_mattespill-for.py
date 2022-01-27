import random

ant_oppgaver = 5
riktig = 0

for i in range(ant_oppgaver):

    faktor1 = random.randint(2, 10)
    faktor2 = random.randint(2, 10)

    fasit = faktor1*faktor2

    print("Hva er ", faktor1, "ganger", faktor2, "?")

    svar = int(input("Skriv inn svaret ditt: "))

    if svar == fasit:
        print("Yay, riktig. Godt jobba!")
        riktig = riktig + 1

    else:
        print("Det var dessverre feil. Prøv igjen på neste oppgave.")

print("Du fikk", riktig, "riktige svar av", ant_oppgaver)

# holder
