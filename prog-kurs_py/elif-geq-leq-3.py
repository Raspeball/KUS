a = 42
b = 69

bruker_tall = int(input("Skriv inn et heltall: "))

if bruker_tall > a:
    # sjekker om tallet er nøyaktik lik 69
    # NB! Enda et "hopp" inn
    if bruker_tall == b:
        print("lol")
    # hvis det ikke er 69, men fortsatt større enn 42
    else:
        print("Ditt tall er større enn 42")

elif bruker_tall < a:
    print("Ditt tall er mindre enn 42")


# holder
