# Esercizio 4
# Ordini semplici
# Definisci il dizionario menu = {"pizza": 8, "pasta": 7, "insalata": 5}.
# Chiedi all'utente di scegliere un piatto finché non digita "stop".
# Se il piatto non è nel menu, chiedi il prezzo e aggiungilo al dizionario.
# Somma i prezzi dei piatti scelti e stampa il totale finale.

# Scrivi qui sotto:

menu = {"pizza": 8, "pasta": 7, "insalata": 5}
condizione = True
conto = 0

while condizione:
    scelta = input("Cosa desidera ordinare? Se non vuole altro scriva 'stop'")
    scelta = scelta.lower()
    if scelta == 'stop':
        break
    if scelta in menu:
        conto = conto + menu[scelta]
    else:
        prezzo = input("Il piatto scelto non è nel menu, quale costo merita? ")
        try:
            prezzo = int(prezzo)
        except ValueError:
            print("Prezzo non valido")
            continue
        if prezzo in range(1, 22):
            menu.setdefault(scelta, prezzo)
            conto = conto + menu[scelta]
        else:
            print("Prezzo non valido")
            continue

print(f"Ecco a lei il totale da pagare: {conto}")