import random

def stampa_griglia(n, pos, uscita):

    for i in range(n):
        for j in range(n):
            if pos[0] == i and pos[1] == j:
                print("G", end="")
            elif uscita[0] == i and uscita[1] == j:
                print("U", end="")
            else:
                print(".", end="")
        print()
    return 0


def muovi(pos, mossa):
    mossa = mossa.lower().strip()
    if mossa=="n":
        pos[0]=pos[0]-1
    elif mossa=="s":
        pos[0]=pos[0]+1
    elif mossa=="e":
        pos[1]=pos[1]+1
    elif mossa=="o":
        pos[1]=pos[1]-1
    else:
        print("La lettera inserita non risponde ad alcun comando")
    return pos

def gestisci_livello(livello):
    n = livello + 2
    pos=[0,0]
    x = random.randint(0, n-1)
    if x == (n-1):
        y=0
    else:
        y = random.randint(0, n-1)
    pos=[x, y]
    uscita = [n - 1, n - 1]
    risultato = None
    while risultato is None:
        stampa_griglia(n, pos, uscita)
        mossa=input("Inserisci la tua mossa: (n, s, e, o)")
        posizione=muovi(pos, mossa)
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= n:
            print("Sei uscito dalla griglia! Hai perso.")
            risultato=False
        if pos[0] == uscita[0] and pos[1] == uscita[1]:
            print("Uscita trovata! Livello completato.")
            risultato=True
    return risultato


def main():
    print("=== Benvenuto in Room Escape ===")
    livello = 0
    max_livello = 5

    while livello <= max_livello:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            print("Hai perso")
            break

main()