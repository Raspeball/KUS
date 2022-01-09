navn = input("Skriv inn navnet ditt: ")

hoyde_cm = float(input("Skriv inn høyden din (cm): "))

# heltallsdivisjon for å finne hele fot
hele_ft = hoyde_cm // 30.48

# finne resten etter å ha gjort om til hele fot
rest_hodye = hoyde_cm % 30.48

# gjøre resten om til inches
rest_inch = rest_hodye / 2.54

# bruker round til å runde av antall inches til nærmeste hele antall
print(f"Hei {navn}! Du er {hoyde_cm}cm, som tilsvarer {hele_ft} ft og {round(rest_inch)} in")

# legger inn hødyen til vin diesel i en variabel
vin_diesel = 185 # cm

# sjekker om høyden er like høy som Vin Diesel
if hoyde_cm == vin_diesel:
    print(f"Fantastisk {navn}. Du er like høy som Vin Diesel")

# hvis høyden ikke er like høy
# sjekker vi om den er høyere eller lavere
else:
    if hoyde_cm > vin_diesel:
        print(f"{navn}, du er faktisk høyere enn Vin Diesel")

    # trenger bare else, og ikke elif
    # siden man enten er like høy, høyere eller lavere
    else:
        print(f"{navn}, du er en touch lavere enn Vin Diesel")


# holder
