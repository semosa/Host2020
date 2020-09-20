import random

def lagerandom():
    liste = []
    for i in range(20):
        tall = random.randint(-200, 200)
        liste.append(tall)

    return liste


def sorter(liste):
    for index in range(len(liste)):
        if index >= 1:
            if liste[index] < liste[index-1]:
                var = liste[index]
                liste[index-1] = var
                liste[index] = liste[index-1]

    print(liste) 

if __name__ == "__main__":
    a = lagerandom()
    b = sorter(a)
    print(a)
    print(b)