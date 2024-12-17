 #Algoritmid ja andmestruktuurid kodutöö 3. ül 1 Tiina Mandel
 
 for i in range(len(nimekiri)):
        if nimekiri[i] == otsitav:
            return i  # kui otsitav on leitud, siis tagastab otsitava indeksi "nimekirjas"
    return -1  # Tagastab cväeruse -1  kui otsitav pole nimekirjas

# nimekiri ja otsitav
nimekiri = [10, 20, 40, 50, 60, 70, 83, 11, 8, 47, 27, 89, 42 ]
otsitav = 11