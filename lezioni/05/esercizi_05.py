# Lezione 05 - Esempi ed esercizi su import, funzioni e problem solving
#
# Questo file contiene:
# 1. alcuni esempi in linea con gli appunti della lezione 5
# 2. esercizi da svolgere
# 3. possibili soluzioni commentate in fondo
#
# In questa lezione lavoriamo soprattutto con:
# - moduli e import
# - definizione di funzioni
# - parametri e return
# - variabili locali
# - chiamate di funzioni
# - scomposizione di problemi in sottoproblemi


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Import di un modulo intero
import math
print(math.pi)
print(math.sqrt(16))

print()

# Import di un solo nome
from math import factorial
print(factorial(5))

print()

# Funzione semplice con return

def quadrato(x):
    return x ** 2


print(quadrato(6))

print()

# Funzione con più risultati

def statistiche(numeri):
    minimo = min(numeri)
    massimo = max(numeri)
    media = sum(numeri) / len(numeri)
    return media, minimo, massimo


media, mn, mx = statistiche([10, 20, 30, 40])
print(media)
print(mn)
print(mx)

print()

# Variabili locali

def concatena(prima, seconda):
    nuovo_testo = prima + " " + seconda
    return nuovo_testo


risultato = concatena("ciao", "mondo")
print(risultato)

print()

# Funzioni che chiamano altre funzioni

def doppio(x):
    return x * 2



def somma_doppi(a, b):
    return doppio(a) + doppio(b)


print(somma_doppi(3, 5))

print()

# Piccolo esempio sul conteggio delle cifre

def num_cifre(x):
    return len(str(x))


print(num_cifre(7))
print(num_cifre(42))
print(num_cifre(1000))

print()

# Ricerca della N-esima cifra costruendo la stringa

def costruisci_stringa_numeri(n):
    testo = ""
    i = 1
    while len(testo) < n:
        testo += str(i)
        i += 1
    return testo



def cerca_cifra_con_stringa(n):
    testo = costruisci_stringa_numeri(n)
    return testo[n - 1]


print(cerca_cifra_con_stringa(12))


# ====================
# ESERCIZI
# ====================

# Esercizio 1
# Import e costanti
# Importa il modulo math.
# Stampa il valore di pi greco e la radice quadrata di 81.

# Scrivi qui sotto:


# Esercizio 2
# Import selettivo
# Usa from math import ... per importare solo pow.
# Calcola 2 alla 5 e stampalo.

# Scrivi qui sotto:


# Esercizio 3
# Prima funzione
# Definisci una funzione saluta(nome) che stampi "Ciao <nome>".
# Chiamala con un nome a scelta.

# Scrivi qui sotto:


# Esercizio 4
# Funzione con return
# Definisci una funzione cubo(x) che restituisca x ** 3.
# Chiamala con 4 e stampa il risultato.

# Scrivi qui sotto:


# Esercizio 5
# Area del rettangolo
# Definisci una funzione area_rettangolo(base, altezza)
# che restituisca l'area.
# Chiamala con 5 e 8.

# Scrivi qui sotto:


# Esercizio 6
# Più valori di ritorno
# Definisci una funzione min_max_somma(valori)
# che restituisca minimo, massimo e somma di una lista.
# Provala con [4, 8, 1, 9].

# Scrivi qui sotto:


# Esercizio 7
# Variabili locali
# Definisci una funzione moltiplica(a, b) che dentro crei una variabile locale prodotto
# e poi la restituisca.
# Salva il risultato in una variabile esterna e stampalo.

# Scrivi qui sotto:


# Esercizio 8
# Funzioni annidate
# Definisci una funzione triplo(x) e una funzione somma_tripli(a, b)
# che usi triplo() due volte e restituisca la somma.
# Provala con 2 e 7.

# Scrivi qui sotto:


# Esercizio 9
# Docstring
# Definisci una funzione sottrai(a, b) con una docstring breve.
# La funzione deve restituire a - b.
# Chiamala e stampa il risultato.

# Scrivi qui sotto:


# Esercizio 10
# Numero di cifre - versione stringa
# Definisci una funzione num_cifre_stringa(x)
# che restituisca quante cifre ha un intero positivo usando str() e len().
# Provala con 9, 42 e 12345.

# Scrivi qui sotto:


# Esercizio 11
# Costruzione della stringa infinita
# Definisci una funzione costruisci_fino_a_n_cifre(n)
# che costruisca la stringa "123456789101112..." finché non contiene almeno n caratteri.
# Stampa la lunghezza della stringa ottenuta per n = 20.

# Scrivi qui sotto:


# Esercizio 12
# N-esima cifra con la stringa
# Definisci una funzione cifra_n_con_stringa(n)
# che usi la funzione precedente e restituisca la N-esima cifra.
# Provala con n = 15.

# Scrivi qui sotto:


# Esercizio 13
# Cercare il numero che contiene la cifra
# Definisci una funzione numero_e_posizione(n)
# che scorra i numeri da 1 in poi, sottragga le loro cifre da n
# e restituisca il numero in cui cade la N-esima cifra e la posizione dentro quel numero.
# Per contare le cifre puoi usare len(str(numero)).
# Provala con n = 15.

# Scrivi qui sotto:


# Esercizio 14
# N-esima cifra senza costruire tutta la stringa
# Definisci una funzione cifra_n_senza_stringona(n)
# che usi numero_e_posizione(n) e restituisca la cifra giusta.
# Provala con n = 15.

# Scrivi qui sotto:


# Esercizio 15
# Verifica del risultato
# Usa le due funzioni cifra_n_con_stringa(n) e cifra_n_senza_stringona(n)
# per confrontare il risultato con n = 200.
# Stampa i due risultati.

# Scrivi qui sotto:


# Esercizio 16
# Blocchi di cifre
# Scrivi un commento oppure alcune print che mostrino quante cifre totali ci sono:
# - nei numeri da 1 a 9
# - nei numeri da 10 a 99
# - nei numeri da 100 a 999

# Scrivi qui sotto:


# Esercizio 17
# Funzione ben nominata
# Definisci una funzione media_voti(voti) che restituisca la media.
# Provala con [18, 24, 30, 27].

# Scrivi qui sotto:


# Esercizio 18
# Funzione con input dell'utente
# Definisci una funzione saluta_utente() che chieda il nome con input()
# e stampi un saluto.
# Poi chiamala.

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1
# import math
# print(math.pi)
# print(math.sqrt(81))

# Soluzione esercizio 2
# from math import pow
# print(pow(2, 5))

# Soluzione esercizio 3
# def saluta(nome):
#     print("Ciao", nome)
#
# saluta("Luca")

# Soluzione esercizio 4
# def cubo(x):
#     return x ** 3
#
# print(cubo(4))

# Soluzione esercizio 5
# def area_rettangolo(base, altezza):
#     return base * altezza
#
# print(area_rettangolo(5, 8))

# Soluzione esercizio 6
# def min_max_somma(valori):
#     minimo = min(valori)
#     massimo = max(valori)
#     totale = sum(valori)
#     return minimo, massimo, totale
#
# print(min_max_somma([4, 8, 1, 9]))

# Soluzione esercizio 7
# def moltiplica(a, b):
#     prodotto = a * b
#     return prodotto
#
# risultato = moltiplica(6, 7)
# print(risultato)

# Soluzione esercizio 8
# def triplo(x):
#     return x * 3
#
# def somma_tripli(a, b):
#     return triplo(a) + triplo(b)
#
# print(somma_tripli(2, 7))

# Soluzione esercizio 9
# def sottrai(a, b):
#     """Restituisce la differenza tra a e b."""
#     return a - b
#
# print(sottrai(10, 3))

# Soluzione esercizio 10
# def num_cifre_stringa(x):
#     return len(str(x))
#
# print(num_cifre_stringa(9))
# print(num_cifre_stringa(42))
# print(num_cifre_stringa(12345))

# Soluzione esercizio 11
# def costruisci_fino_a_n_cifre(n):
#     testo = ""
#     i = 1
#     while len(testo) < n:
#         testo += str(i)
#         i += 1
#     return testo
#
# s = costruisci_fino_a_n_cifre(20)
# print(len(s))
# print(s)

# Soluzione esercizio 12
# def costruisci_fino_a_n_cifre(n):
#     testo = ""
#     i = 1
#     while len(testo) < n:
#         testo += str(i)
#         i += 1
#     return testo
#
# def cifra_n_con_stringa(n):
#     testo = costruisci_fino_a_n_cifre(n)
#     return testo[n - 1]
#
# print(cifra_n_con_stringa(15))

# Soluzione esercizio 13
# def numero_e_posizione(n):
#     numero = 1
#     while True:
#         cifre = len(str(numero))
#         if cifre < n:
#             n -= cifre
#             numero += 1
#         else:
#             return numero, n
#
# print(numero_e_posizione(15))

# Soluzione esercizio 14
# def numero_e_posizione(n):
#     numero = 1
#     while True:
#         cifre = len(str(numero))
#         if cifre < n:
#             n -= cifre
#             numero += 1
#         else:
#             return numero, n
#
# def cifra_n_senza_stringona(n):
#     numero, posizione = numero_e_posizione(n)
#     return str(numero)[posizione - 1]
#
# print(cifra_n_senza_stringona(15))

# Soluzione esercizio 15
# def costruisci_fino_a_n_cifre(n):
#     testo = ""
#     i = 1
#     while len(testo) < n:
#         testo += str(i)
#         i += 1
#     return testo
#
# def cifra_n_con_stringa(n):
#     testo = costruisci_fino_a_n_cifre(n)
#     return testo[n - 1]
#
# def numero_e_posizione(n):
#     numero = 1
#     while True:
#         cifre = len(str(numero))
#         if cifre < n:
#             n -= cifre
#             numero += 1
#         else:
#             return numero, n
#
# def cifra_n_senza_stringona(n):
#     numero, posizione = numero_e_posizione(n)
#     return str(numero)[posizione - 1]
#
# print(cifra_n_con_stringa(200))
# print(cifra_n_senza_stringona(200))

# Soluzione esercizio 16
# print("Da 1 a 9:", 9 * 1)
# print("Da 10 a 99:", 90 * 2)
# print("Da 100 a 999:", 900 * 3)

# Soluzione esercizio 17
# def media_voti(voti):
#     return sum(voti) / len(voti)
#
# print(media_voti([18, 24, 30, 27]))

# Soluzione esercizio 18
# def saluta_utente():
#     nome = input("Come ti chiami? ")
#     print("Ciao", nome)
#
# saluta_utente()

