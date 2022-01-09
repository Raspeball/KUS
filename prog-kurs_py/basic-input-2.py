# int() gjør om tekst til et tall/heltall; float() gjør om til desimaltall
år = int(input("Skriv inn alderen din:"))

# vi kunne også brukt int() her, og skrevet mnd = int(år)*12
mnd = år*12

print("Du er", mnd, "måneder gammel")

print(f"Du er {mnd} måneder gammel") # f-print er ofte litt enklere
