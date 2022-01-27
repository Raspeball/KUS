import random

hemmelig_tall = random.randint(1, 20)

gjett = int(input("Gjett hvilket tall jeg tenker på: "))

while gjett != hemmelig_tall:

    print("Beklager, det var ikke riktig.")
    gjett = int(input("Gjett på nytt: "))

print("Gratulerer, du gjettet riktig til slutt")

# holder
