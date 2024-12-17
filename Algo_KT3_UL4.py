def kolmikotsing(loend, otsitav):

    vasak = 0  # algus
    parem = len(loend) - 1  # lõpp

    while vasak <= parem:
        # jaga loendi pikkus kolmeks osaks
        mid1 = vasak + (parem - vasak) // 3
        mid2 = parem - (parem - vasak) // 3

        # kontrolli, kas otsitav asub keskunktides
        if loend[mid1] == otsitav:
            return mid1
        if loend[mid2] == otsitav:
            return mid2

        # Narrow down the search space
        if otsitav < loend[mid1]:
            parem = mid1 - 1  # kui otsitav esimesest keskpunktist väikse, siis keskendu ainult esimesele kolmandikule
        elif otsitav > loend[mid2]:
            vasak = mid2 + 1  # kui otsitav teisest keskpunktist suurem, keskendu ainult viimasele kolmandikule
        else:
            vasak = mid1 + 1  # kui ei kumbaki, siis keskendu keskmisele kolmandikule
            parem = mid2 - 1

    return -1  # otsitavat ei leitud

# näide:
loend = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
otsitav = 70

# Perform Ternary Search
result = kolmikotsing(loend, otsitav)

# Print the result
if result != -1:
    print(f"Element {otsitav} leiti kohal {result}.")
else:
    print(f"Element {otsitav} ei ole loendis.")
