def kahendotsing(loend, otsitav):

    vasak = 0  # Starting index of the array
    parem = len(loend) - 1  # Ending index of the array

    while vasak <= parem:
        mid = vasak + (parem - vasak) // 2  # leiab keskmise elemendi
        
        # kas  keskmine element on otsitav?
        if loend[mid] == otsitav:
            return mid

        # kui otsitav on keskmisest elemendist väiksem, keskendu vasakule poolele
        elif otsitav < loend[mid]:
            parem = mid - 1

        # kui otsitav on suurem, keskendu paremale poolele (keskpunkt+1  väärtus saab uus vasak lõpp)
        else:
            vasak = mid + 1

    # kui ei leia, tagastab -1
    return -1

# Näide:
loend = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
otsitav = 120

# viib  otsingu läbi
result = kahendotsing(loend, otsitav)

# Print the result
if result != -1:
    print(f"Element {otsitav} leitud kohal {result}.")
else:
    print(f"Element {otsitav} ei ole loendis.")
