a = 42
b = 69

bruker_tall = int(input("Skriv inn et heltall: "))

# sjekker først om tallet er lik b
if bruker_tall == b:
    print("lol")

# hvis tallet ikke er lik b, så kan vi
# si om det er større eller mindre enn a
else:
    if bruker_tall > a:
        # bruker f-print
        print(f"Tallet ditt er større enn {a}")

    elif bruker_tall < a:
        print(f"Tallet ditt er mindre enn {a}")

    # kan ha else, for det er bare et alternativ igjen
    else:
        print(f"Tallet ditt er {a}")


# holder
