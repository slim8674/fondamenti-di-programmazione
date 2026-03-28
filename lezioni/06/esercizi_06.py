# Lezione 06 - Esempi ed esercizi su funzioni, contenitori, sort e argomenti
#
# Questo file contiene:
# 1. esempi introduttivi coerenti con gli appunti della lezione 6
# 2. esercizi da svolgere con priorità agli esercizi forniti dal docente
# 3. alcune integrazioni mirate sui punti più importanti della lezione
# 4. possibili soluzioni commentate in fondo
#
# In questa lezione lavoriamo soprattutto con:
# - funzioni e valori di ritorno
# - liste, tuple, dizionari e insiemi
# - sort() e sorted() con key
# - argomenti opzionali
# - effetti collaterali e default mutabili
# - input controllato con try/except


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Esempio 1: funzione che restituisce un risultato

def area_rettangolo(base, altezza):
    return base * altezza


print(area_rettangolo(4, 5))

print()

# Esempio 2: modifica di una lista passata come argomento
valori = [10, 20, 30, 40]


def elimina_terzo(lista):
    lista.pop(2)


print("Prima:", valori)
elimina_terzo(valori)
print("Dopo:", valori)

print()

# Esempio 3: argomento opzionale

def saluta(nome, punteggiatura="!"):
    return "Ciao " + nome + punteggiatura


print(saluta("Anna"))
print(saluta("Luca", "..."))

print()

# Esempio 4: sorted con key
parole = ["banana", "kiwi", "mela", "ananas"]
print(sorted(parole, key=len))

print()

# Esempio 5: packing e unpacking
primo, *mezzo, ultimo = [1, 2, 3, 4, 5]
print(primo)
print(mezzo)
print(ultimo)


# ====================
# ESERCIZI DEL DOCENTE
# ====================

# Esercizio 1.1 - Manipolazione base
# Crea una lista con i numeri da 1 a 10.
# Scrivi del codice per:
# - aggiungere il numero 11 alla fine
# - inserire il numero 0 all'inizio
# - rimuovere il numero 5
# - stampare la lunghezza della lista finale

# Scrivi qui sotto:


# Esercizio 1.2 - Operazioni con liste
# Data la lista numeri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]:
# - trova la somma di tutti gli elementi
# - trova il valore massimo e minimo
# - conta quante volte appare il numero 1
# - crea una nuova lista con solo i numeri pari

# Scrivi qui sotto:


# Esercizio 1.3 - Liste annidate
# Crea una lista di liste che rappresenti una matrice 3x3:
# 1 2 3
# 4 5 6
# 7 8 9
# Scrivi codice per stampare la diagonale principale (1, 5, 9).

# Scrivi qui sotto:


# Esercizio 2.1 - Conteggio caratteri
# Scrivi una funzione che prenda una stringa e restituisca un dizionario
# con il conteggio di ogni carattere.
#
# Test:
# print(conta_caratteri("hello world"))
# Output atteso:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Scrivi qui sotto:


def conta_caratteri(testo):
    pass


# Esercizio 2.2 - Unione dizionari
# Dati due dizionari, scrivi codice per unirli.
# Se una chiave è presente in entrambi, somma i valori.
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# Risultato atteso: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# Scrivi qui sotto:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


# Esercizio 3.1 - Coordinate
# Crea una lista di tuple che rappresentino coordinate (x, y):
# - crea 5 punti casuali
# - trova il punto più lontano dall'origine (0, 0)
# - ordina i punti per distanza dall'origine

# Scrivi qui sotto:
import math


# Esercizio 3.2 - Swap di variabili
# Usando le tuple, scrivi codice per scambiare i valori di due variabili
# senza usare una variabile temporanea.
#
# a = 10
# b = 20
# print(f"a = {a}, b = {b}")  -> dovrebbe stampare: a = 20, b = 10

# Scrivi qui sotto:
a = 10
b = 20


# Esercizio 3.3 - Ritorno multiplo
# Scrivi una funzione che prenda una lista di numeri e restituisca
# una tupla con (minimo, massimo, media).
#
# Test:
# print(statistiche([1, 5, 3, 9, 2]))   -> (1, 9, 4.0)

# Scrivi qui sotto:


def statistiche(numeri):
    pass


# Esercizio 4.1 - Operazioni base sugli insiemi
# Dati due insiemi di numeri:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Calcola:
# - unione
# - intersezione
# - differenza (elementi in set1 ma non in set2)
# - differenza simmetrica

# Scrivi qui sotto:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


# Esercizio 4.2 - Rimozione duplicati
# Scrivi una funzione che prenda una lista e restituisca una nuova lista
# senza duplicati, mantenendo l'ordine.
#
# Test:
# print(rimuovi_duplicati([1, 2, 2, 3, 1, 4, 5, 4]))   -> [1, 2, 3, 4, 5]

# Scrivi qui sotto:


def rimuovi_duplicati(lista):
    pass


# Esercizio 4.3 - Lettere uniche
# Scrivi una funzione che prenda due parole e restituisca
# le lettere che appaiono in entrambe.
#
# Test:
# print(lettere_comuni("python", "java"))   -> {'a'}

# Scrivi qui sotto:


def lettere_comuni(parola1, parola2):
    pass


# Esercizio 5.1 - Ordinamento personalizzato
# Data una lista di nomi, ordinali:
# - in ordine alfabetico
# - per lunghezza (dal più corto al più lungo)
# - per lunghezza inversa (dal più lungo al più corto)

# Scrivi qui sotto:
nomi = ["Alice", "Bob", "Charlie", "Diana", "Eve"]


# Esercizio 5.2 - Ordinamento di dizionari
# Data una lista di dizionari rappresentanti persone,
# ordinali per età crescente.

# Scrivi qui sotto:
persone = [
    {'nome': 'Alice', 'eta': 25},
    {'nome': 'Bob', 'eta': 30},
    {'nome': 'Charlie', 'eta': 20}
]


# Esercizio 5.3 - Ordinamento complesso
# Data una lista di tuple (nome, voto), ordinala:
# - prima per voto decrescente
# - poi per nome alfabetico in caso di parità

# Scrivi qui sotto:
studenti = [('Alice', 85), ('Bob', 92), ('Charlie', 85), ('Diana', 78)]


# Esercizio 6.1 - Funzione con parametri opzionali
# Scrivi una funzione che calcoli l'area di un rettangolo.
# Se viene passato solo un parametro, considera il rettangolo come un quadrato.
#
# Test:
# print(area_rettangolo_opz(5))     -> 25
# print(area_rettangolo_opz(4, 6))  -> 24

# Scrivi qui sotto:


def area_rettangolo_opz(larghezza, altezza=None):
    pass


# Esercizio 6.2 - Elaborazione dati studenti
# Scrivi un programma che gestisca i voti degli studenti.
# Spezza il programma in funzioni piccole.
#
# La funzione deve ricevere una lista di tuple (nome, [lista_voti]) e restituire:
# - dizionario con nome -> media voti
# - lista studenti ordinata per media decrescente
# - set degli studenti che hanno almeno un voto >= 9
# - statistiche globali (media classe, voto max, voto min)

# Scrivi qui sotto:


def elabora_voti(dati_studenti):
    pass


# ====================
# INTEGRAZIONI MIRATE
# ====================

# Esercizio 7 - Default mutabile: osservazione del problema
# Definisci una funzione accumula(x, lista=[]) che aggiunge x alla lista
# e la restituisce.
# Chiamala tre volte senza passare il secondo argomento e osserva cosa accade.

# Scrivi qui sotto:


# Esercizio 8 - Versione corretta con None
# Riscrivi la funzione accumula in modo corretto usando None come default.
# Chiamala tre volte senza passare la lista e verifica che ogni volta
# venga creata una lista nuova.

# Scrivi qui sotto:


# Esercizio 9 - Input intero controllato
# Chiedi all'utente un intero da 1 a 10.
# Continua a chiederlo finché non inserisce un valore valido.
# Usa try/except per evitare errori in caso di testo non numerico.
# Alla fine stampa il numero scelto.

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1.1
# lista = list(range(1, 11))
# lista.append(11)
# lista.insert(0, 0)
# lista.remove(5)
# print(lista)
# print(len(lista))

# Soluzione esercizio 1.2
# numeri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# print(sum(numeri))
# print(max(numeri))
# print(min(numeri))
# print(numeri.count(1))
# pari = []
# for numero in numeri:
#     if numero % 2 == 0:
#         pari.append(numero)
# print(pari)

# Soluzione esercizio 1.3
# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(3):
#     print(matrice[i][i])

# Soluzione esercizio 2.1
# def conta_caratteri(testo):
#     conteggi = {}
#     for carattere in testo:
#         if carattere in conteggi:
#             conteggi[carattere] += 1
#         else:
#             conteggi[carattere] = 1
#     return conteggi
#
# print(conta_caratteri("hello world"))

# Soluzione esercizio 2.2
# risultato = dict1.copy()
# for chiave, valore in dict2.items():
#     if chiave in risultato:
#         risultato[chiave] += valore
#     else:
#         risultato[chiave] = valore
# print(risultato)

# Soluzione esercizio 3.1
# import random
# punti = []
# for _ in range(5):
#     x = random.randint(-10, 10)
#     y = random.randint(-10, 10)
#     punti.append((x, y))
#
# def distanza_origine(punto):
#     x, y = punto
#     return math.sqrt(x ** 2 + y ** 2)
#
# print(punti)
# print(max(punti, key=distanza_origine))
# print(sorted(punti, key=distanza_origine))

# Soluzione esercizio 3.2
# a, b = b, a
# print(f"a = {a}, b = {b}")

# Soluzione esercizio 3.3
# def statistiche(numeri):
#     minimo = min(numeri)
#     massimo = max(numeri)
#     media = sum(numeri) / len(numeri)
#     return minimo, massimo, media
#
# print(statistiche([1, 5, 3, 9, 2]))

# Soluzione esercizio 4.1
# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set1 ^ set2)

# Soluzione esercizio 4.2
# def rimuovi_duplicati(lista):
#     visti = set()
#     nuova = []
#     for elemento in lista:
#         if elemento not in visti:
#             visti.add(elemento)
#             nuova.append(elemento)
#     return nuova
#
# print(rimuovi_duplicati([1, 2, 2, 3, 1, 4, 5, 4]))

# Soluzione esercizio 4.3
# def lettere_comuni(parola1, parola2):
#     return set(parola1) & set(parola2)
#
# print(lettere_comuni("python", "java"))

# Soluzione esercizio 5.1
# print(sorted(nomi))
# print(sorted(nomi, key=len))
# print(sorted(nomi, key=len, reverse=True))

# Soluzione esercizio 5.2
# ordinate = sorted(persone, key=lambda persona: persona['eta'])
# print(ordinate)

# Soluzione esercizio 5.3
# ordinati = sorted(studenti, key=lambda coppia: (-coppia[1], coppia[0]))
# print(ordinati)

# Soluzione esercizio 6.1
# def area_rettangolo_opz(larghezza, altezza=None):
#     if altezza is None:
#         altezza = larghezza
#     return larghezza * altezza
#
# print(area_rettangolo_opz(5))
# print(area_rettangolo_opz(4, 6))

# Soluzione esercizio 6.2
# def media(lista_voti):
#     return sum(lista_voti) / len(lista_voti)
#
# def elabora_voti(dati_studenti):
#     medie = {}
#     studenti_con_almeno_9 = set()
#     tutti_i_voti = []
#
#     for nome, voti in dati_studenti:
#         medie[nome] = media(voti)
#         tutti_i_voti.extend(voti)
#         for voto in voti:
#             if voto >= 9:
#                 studenti_con_almeno_9.add(nome)
#                 break
#
#     classifica = sorted(medie.items(), key=lambda coppia: coppia[1], reverse=True)
#     statistiche_globali = (
#         sum(tutti_i_voti) / len(tutti_i_voti),
#         max(tutti_i_voti),
#         min(tutti_i_voti)
#     )
#
#     return medie, classifica, studenti_con_almeno_9, statistiche_globali
#
# studenti_test = [
#     ("Alice", [8, 7, 9, 6]),
#     ("Bob", [9, 8, 10, 7]),
#     ("Charlie", [6, 5, 7, 8]),
#     ("Diana", [10, 9, 9, 8])
# ]
#
# print(elabora_voti(studenti_test))

# Soluzione esercizio 7
# def accumula(x, lista=[]):
#     lista.append(x)
#     return lista
#
# print(accumula(1))
# print(accumula(2))
# print(accumula(3))

# Soluzione esercizio 8
# def accumula_bene(x, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(x)
#     return lista
#
# print(accumula_bene(1))
# print(accumula_bene(2))
# print(accumula_bene(3))

# Soluzione esercizio 9
# while True:
#     testo = input("Inserisci un intero da 1 a 10: ")
#     try:
#         numero = int(testo)
#     except ValueError:
#         print("Input non valido")
#         continue
#
#     if 1 <= numero <= 10:
#         break
#
#     print("Numero fuori intervallo")
#
# print(numero)

