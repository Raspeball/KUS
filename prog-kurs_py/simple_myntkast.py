import random

ant_kast = 1000000

ant_mynt = 0
ant_kron = 0

for forsok in range(ant_kast):
    et_kast = random.randint(0, 1)

    if et_kast == 0:
        ant_mynt = ant_mynt + 1

    else:
        ant_kron = ant_kron + 1


print(f"Det ble kastet {ant_kast} myntkast. {ant_mynt} var mynt; {ant_kron} var kron")


# holder
