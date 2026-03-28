# Lezione 04 - Esempi ed esercizi su indici, enumerate, metodi e contenitori
#
# Questo file contiene:
# 1. alcuni esempi in linea con gli appunti della lezione 4
# 2. esercizi da svolgere
# 3. possibili soluzioni commentate in fondo
#
# In questa lezione lavoriamo soprattutto con:
# - iterazione tramite indice
# - enumerate()
# - metodi di stringhe e contenitori
# - liste, tuple, insiemi e dizionari
# - attenzione alla modifica di una lista durante un ciclo


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Iterazione tramite indice
lista_numeri = [2, 5, 7, 9]
for indice in range(len(lista_numeri)):
    print(indice, lista_numeri[indice])

print()

# Iterazione con enumerate()
for indice, elemento in enumerate(lista_numeri):
    print(indice, elemento)

print()
print(list(enumerate(lista_numeri)))

print()

# Verità e falsità dei contenitori
print(bool([]))
print(bool([10]))
print(bool({}))
print(bool(set()))
print(bool({'a': 1}))

print()

# Metodi delle stringhe
frase = 'Prova Dimostrativa'
print(frase.lower())
print(frase.upper())
print(frase.find('Prova'))
print(frase.find('gnomo'))

print()

# Metodi principali delle liste
valori = [1, 2, 3]
valori.append(4)
print(valori)
valori.insert(1, 99)
print(valori)
print(valori.pop(2))
print(valori)
valori.remove(99)
print(valori)

print()

# Tuple: lettura e metodi non distruttivi
coordinate = (10, 20, 10, 30)
print(coordinate[1])
print(coordinate.count(10))
print(coordinate.index(20))

print()

# Insiemi: niente ordine garantito e niente duplicati
insieme = {1, 2, 2, 3}
insieme.add(4)
print(insieme)
print(2 in insieme)

print()

# Dizionari: chiavi, valori e coppie
studente = {'nome': 'Anna', 'eta': 21}
print(studente.keys())
print(studente.values())
print(studente.items())
for chiave, valore in studente.items():
    print(chiave, valore)

print()

# Attenzione: modificare una lista mentre la si scorre può creare problemi
originale = [10, 20, 30, 40, 50]
nuova_lista = []
for elemento in originale:
    if elemento != 30:
        nuova_lista.append(elemento)
print(nuova_lista)


# ====================
# ESERCIZI
# ====================

# Esercizio 1
# Lista di frutta
# Crea la lista frutta = ["mela", "banana", "arancia"].
# Aggiungi due frutti nuovi con un ciclo for.
# Stampa tutti gli elementi con il loro indice a partire da 1.

# Scrivi qui sotto:


# Esercizio 2
# Voti di studenti
# Partendo da un dizionario vuoto voti = {}, chiedi nome e voto finché l'utente inserisce "fine".
# Controlla che il voto sia un numero intero tra 1 e 10.
# Salva ogni coppia nome:voto nel dizionario.
# Alla fine stampa:
# - quanti studenti hanno voto almeno 6
# - la tabella completa dei nomi e dei voti

# Scrivi qui sotto:
tabella = {}




# Esercizio 3
# Numeri unici
# Aggiungi dei numeri inseriti da tastiera alla lista nums = [].
# Continua finché l'utente digita "stop".
# Stampa i numeri senza duplicati in ordine crescente.

# Scrivi qui sotto:


# Esercizio 4
# Ordini semplici
# Definisci il dizionario menu = {"pizza": 8, "pasta": 7, "insalata": 5}.
# Chiedi all'utente di scegliere un piatto finché non digita "stop".
# Se il piatto non è nel menu, chiedi il prezzo e aggiungilo al dizionario.
# Somma i prezzi dei piatti scelti e stampa il totale finale.

# Scrivi qui sotto:


# Esercizio 5
# Indovina numero
# Importa random.
# Genera un numero segreto tra 1 e 20.
# Dai all'utente 5 tentativi per indovinarlo.
# Dopo ogni tentativo stampa "alto", "basso" oppure "giusto".
# Alla fine stampa se ha vinto o perso e quanti tentativi ha usato.

# Scrivi qui sotto:


# Esercizio 6
# enumerate() e indici
# Crea la lista nomi = ["Luca", "Anna", "Marco", "Sara"].
# Stampala con enumerate() mostrando indice ed elemento.
# Poi ristampa gli stessi dati con indice che parte da 1.

# Scrivi qui sotto:


# Esercizio 7
# Metodi delle liste
# Crea la lista numeri = [10, 20, 30].
# Esegui in ordine queste operazioni:
# - append(40)
# - insert(1, 15)
# - pop() salvando il valore estratto in una variabile
# - remove(20)
# Stampa ogni volta la lista e infine il valore estratto.

# Scrivi qui sotto:


# Esercizio 8
# Slice assignment
# Crea la lista valori = [1, 2, 3, 4, 5, 6].
# Sostituisci gli elementi da indice 2 a indice 4 compreso con le lettere della stringa "abc".
# Poi usa uno slice assignment con lista vuota per eliminare due elementi consecutivi.
# Stampa la lista dopo ogni modifica.

# Scrivi qui sotto:


# Esercizio 9
# Insiemi
# Crea due insiemi A = {1, 2, 3, 4} e B = {3, 4, 5, 6}.
# Stampa:
# - unione
# - intersezione
# - differenza A - B
# - differenza simmetrica

# Scrivi qui sotto:


# Esercizio 10
# Dizionari e metodi
# Crea il dizionario prodotto = {"nome": "penna", "prezzo": 2.5}.
# Usa get() per leggere la chiave "prezzo" e una chiave mancante con valore di default.
# Usa setdefault() per aggiungere la chiave "quantita" con valore 10.
# Stampa poi keys(), values() e items().

# Scrivi qui sotto:


# Esercizio 11
# Truthiness dei contenitori
# Verifica con if quali tra questi contenitori sono vuoti e quali no:
# [], [0], {}, {"x": 1}, set(), {5}
# Stampa per ciascuno se viene interpretato come True oppure False.

# Scrivi qui sotto:


# Esercizio 12
# Dizionario ordinato per chiavi
# Crea un dizionario con almeno quattro coppie materia:voto.
# Estrai le chiavi in una lista, ordinale con sort() e poi stampa il dizionario
# seguendo l'ordine alfabetico delle chiavi.

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1
# frutta = ["mela", "banana", "arancia"]
# for _ in range(2):
#     nuovo_frutto = input("Inserisci un frutto: ")
#     frutta.append(nuovo_frutto)
#
# for indice, frutto in enumerate(frutta, start=1):
#     print(indice, frutto)

# Soluzione esercizio 2
# voti = {}
#
# while True:
#     nome = input("Nome studente (o 'fine'): ")
#     if nome == "fine":
#         break
#
#     while True:
#         testo_voto = input("Voto da 1 a 10: ")
#         if testo_voto.isdigit():
#             voto = int(testo_voto)
#             if 1 <= voto <= 10:
#                 break
#         print("Voto non valido")
#
#     voti[nome] = voto
#
# promossi = 0
# for voto in voti.values():
#     if voto >= 6:
#         promossi += 1
#
# print("Studenti con voto >= 6:", promossi)
# for nome, voto in voti.items():
#     print(nome, voto)

# Soluzione esercizio 3
# nums = []
#
# while True:
#     testo = input("Inserisci un numero (o 'stop'): ")
#     if testo == "stop":
#         break
#     if testo.lstrip("-").isdigit():
#         nums.append(int(testo))
#     else:
#         print("Valore non valido")
#
# unici = list(set(nums))
# unici.sort()
# print(unici)

# Soluzione esercizio 4
# menu = {"pizza": 8, "pasta": 7, "insalata": 5}
# totale = 0
#
# while True:
#     piatto = input("Scegli un piatto (o 'stop'): ").lower()
#     if piatto == "stop":
#         break
#
#     if piatto not in menu:
#         prezzo = float(input(f"Prezzo di {piatto}: "))
#         menu[piatto] = prezzo
#
#     totale += menu[piatto]
#
# print("Totale:", totale)
# print("Menu finale:")
# for piatto, prezzo in menu.items():
#     print(piatto, prezzo)

# Soluzione esercizio 5
# import random
#
# segreto = random.randint(1, 20)
# tentativi_usati = 0
# vinto = False
#
# for tentativo in range(1, 6):
#     numero = int(input("Tentativo: "))
#     tentativi_usati = tentativo
#
#     if numero == segreto:
#         print("giusto")
#         vinto = True
#         break
#     elif numero < segreto:
#         print("basso")
#     else:
#         print("alto")
#
# if vinto:
#     print("Hai vinto")
# else:
#     print("Hai perso")
#
# print("Tentativi usati:", tentativi_usati)
# print("Numero segreto:", segreto)

# Soluzione esercizio 6
# nomi = ["Luca", "Anna", "Marco", "Sara"]
# for indice, nome in enumerate(nomi):
#     print(indice, nome)
#
# print()
# for indice, nome in enumerate(nomi, start=1):
#     print(indice, nome)

# Soluzione esercizio 7
# numeri = [10, 20, 30]
# print(numeri)
#
# numeri.append(40)
# print(numeri)
#
# numeri.insert(1, 15)
# print(numeri)
#
# estratto = numeri.pop()
# print(numeri)
#
# numeri.remove(20)
# print(numeri)
#
# print("Valore estratto:", estratto)

# Soluzione esercizio 8
# valori = [1, 2, 3, 4, 5, 6]
# valori[2:5] = list("abc")
# print(valori)
#
# valori[1:3] = []
# print(valori)

# Soluzione esercizio 9
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)
# print(A & B)
# print(A - B)
# print(A ^ B)

# Soluzione esercizio 10
# prodotto = {"nome": "penna", "prezzo": 2.5}
# print(prodotto.get("prezzo", 0))
# print(prodotto.get("colore", "non presente"))
# print(prodotto.setdefault("quantita", 10))
# print(prodotto.keys())
# print(prodotto.values())
# print(prodotto.items())

# Soluzione esercizio 11
# contenitori = [[], [0], {}, {"x": 1}, set(), {5}]
# for contenitore in contenitori:
#     if contenitore:
#         print(contenitore, "-> True")
#     else:
#         print(contenitore, "-> False")

# Soluzione esercizio 12
# voti = {
#     "matematica": 28,
#     "fisica": 25,
#     "analisi": 30,
#     "python": 29,
# }
#
# chiavi = list(voti.keys())
# chiavi.sort()
# for chiave in chiavi:
#     print(chiave, voti[chiave])
