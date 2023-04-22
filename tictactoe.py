import random

def stampa_tabellone(tabellone):
    for i in range(3):
        for j in range(3):
            print(tabellone[i][j], end=" ")
            if j < 2:
                print("|", end=" ")
        print()
        if i < 2:
            print("---------")

def verifica_vittoria(tabellone, simbolo):
    for i in range(3):
        if all([cella == simbolo for cella in tabellone[i]]):
            return True
        if all([tabellone[j][i] == simbolo for j in range(3)]):
            return True
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] == simbolo:
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] == simbolo:
        return True
    return False

def mossa_ia(tabellone):
    caselle_disponibili = [(i, j) for i in range(3) for j in range(3) if tabellone[i][j] == " "]
    return random.choice(caselle_disponibili)

def gioco():
    tabellone = [[" " for _ in range(3)] for _ in range(3)]
    giocatore = "X"
    caselle_libere = 9

    while caselle_libere > 0:
        stampa_tabellone(tabellone)
        if giocatore == "X":
            print("Turno del giocatore umano (X):")
            casella = int(input("Scegli un numero tra 1 e 9 per la casella: ")) - 1
            riga, colonna = divmod(casella, 3)
        else:
            print("Turno dell'IA (O):")
            riga, colonna = mossa_ia(tabellone)

        if tabellone[riga][colonna] != " ":
            print("Casella già occupata, scegli un'altra casella.")
            continue

        tabellone[riga][colonna] = giocatore
        caselle_libere -= 1

        if verifica_vittoria(tabellone, giocatore):
            stampa_tabellone(tabellone)
            print(f"Giocatore {giocatore} ha vinto!")
            break

        giocatore = "O" if giocatore == "X" else "X"

    else:
        print("Pareggio!")

if __name__ == "__main__":
    gioco()