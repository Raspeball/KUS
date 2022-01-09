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
