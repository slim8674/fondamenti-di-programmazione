# Lezione 03 - Esempi ed esercizi su assegnamenti, condizioni, cicli e contenitori
#
# Questo file contiene:
# 1. alcuni esempi visti negli appunti
# 2. piccoli esercizi da svolgere
# 3. possibili soluzioni commentate in fondo
#
# Per usare bene questo file:
# - prova prima a leggere gli esempi
# - poi svolgi gli esercizi da solo
# - infine confronta con le soluzioni


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Assegnamento potenziato
x = 10
x += 5
print(x)

x *= 2
print(x)

# Assegnamento potenziato con stringhe
saluto = "ciao"
saluto += " bello"
print(saluto)

saluto *= 2
print(saluto)

# Assegnamento multiplo
nome, cognome, eta = "Luca", "Rossi", 20
print(nome)
print(cognome)
print(eta)

# Scambio di variabili
nome, cognome = cognome, nome
print(nome, cognome)

# Condizioni
numero = 7
if numero > 10:
    print("maggiore di 10")
elif numero > 5:
    print("maggiore di 5")
else:
    print("minore o uguale a 5")

# Match-case
comando = "start"
match comando:
    case "start":
        print("Avvio")
    case "stop" | "end":
        print("Arresto")
    case _:
        print("Comando sconosciuto")

# Ciclo for
for i in range(5):
    print(i)

# Ciclo while
contatore = 0
while contatore < 3:
    print("contatore =", contatore)
    contatore += 1

# Liste
numeri = [10, 20, 30]
print(numeri)
print(numeri[1])
numeri[1] = 99
print(numeri)

# Tuple
coordinate = (4, 7)
print(coordinate)
print(coordinate[0])

# Set
insieme = {1, 2, 2, 3}
print(insieme)
insieme.add(4)
print(insieme)

# Dizionari
studente = {"nome": "Anna", "eta": 21}
print(studente)
print(studente["nome"])
studente["eta"] = 22
studente["corso"] = "Informatica"
print(studente)

# Iterazione su dizionario
for chiave, valore in studente.items():
    print(chiave, valore)


# ====================
# ESERCIZI
# ====================

# Esercizio 1
# Crea una variabile n con valore 8.
# Usa un assegnamento potenziato per aumentarla di 3.
# Stampala.

# Scrivi qui sotto:


# Esercizio 2
# Crea una variabile testo con valore "Py".
# Usa *= per ripeterla 4 volte.
# Stampa il risultato.

# Scrivi qui sotto:


# Esercizio 3
# Assegna in una sola istruzione tre valori a tre variabili a, b e c.
# Poi stampale.

# Scrivi qui sotto:


# Esercizio 4
# Crea due variabili nome e cognome.
# Scambia i loro valori senza usare una variabile temporanea.
# Poi stampali.

# Scrivi qui sotto:


# Esercizio 5
# Crea una variabile voto.
# Se voto è almeno 18 stampa "promosso".
# Altrimenti stampa "bocciato".

# Scrivi qui sotto:


# Esercizio 6
# Crea una variabile numero.
# Se è positivo stampa "positivo".
# Se è negativo stampa "negativo".
# Altrimenti stampa "zero".

# Scrivi qui sotto:


# Esercizio 7
# Crea una variabile giorno con un valore a scelta.
# Usa match per stampare:
# - "lezione" se vale "lunedi"
# - "pausa" se vale "domenica"
# - "altro giorno" in tutti gli altri casi

# Scrivi qui sotto:


# Esercizio 8
# Usa un ciclo for per stampare i numeri da 0 a 9.

# Scrivi qui sotto:


# Esercizio 9
# Usa range(3, 11, 2) e stampa i valori prodotti.

# Scrivi qui sotto:


# Esercizio 10
# Usa un ciclo while per stampare i numeri da 1 a 5.

# Scrivi qui sotto:


# Esercizio 11
# Usa un ciclo for e break per fermarti quando incontri il numero 4.
# Stampa i numeri prima del break.

# Scrivi qui sotto:


# Esercizio 12
# Usa un ciclo for e continue per stampare solo i numeri dispari tra 0 e 9.

# Scrivi qui sotto:


# Esercizio 13
# Crea una lista con quattro elementi a scelta.
# Stampa il primo elemento e l'ultimo elemento.

# Scrivi qui sotto:


# Esercizio 14
# Crea una lista numeri = [1, 2, 3].
# Cambia il valore centrale in 99 e stampa la lista.

# Scrivi qui sotto:


# Esercizio 15
# Crea una tupla con tre valori.
# Stampa il secondo elemento.

# Scrivi qui sotto:


# Esercizio 16
# Crea un set a partire dalla lista [1, 2, 2, 3, 3, 3].
# Stampalo e osserva che i duplicati spariscono.

# Scrivi qui sotto:


# Esercizio 17
# Crea un set con alcuni numeri.
# Aggiungi un nuovo numero con add() e stampalo.

# Scrivi qui sotto:


# Esercizio 18
# Crea un dizionario con le chiavi "nome" e "eta".
# Stampa il valore associato alla chiave "nome".

# Scrivi qui sotto:


# Esercizio 19
# Crea un dizionario vuoto.
# Aggiungi poi le coppie chiave-valore:
# "corso": "Python"
# "lezione": 3
# Stampa il dizionario.

# Scrivi qui sotto:


# Esercizio 20
# Crea un dizionario con almeno due coppie chiave-valore.
# Usa un ciclo for con items() per stampare chiave e valore.

# Scrivi qui sotto:


# Esercizio 21
# Crea la lista ["Luca", "Rossi", 20].
# Usa lo spacchettamento per assegnare i tre valori a nome, cognome ed eta.
# Poi stampali.

# Scrivi qui sotto:


# Esercizio 22
# Chiedi all'utente un numero intero.
# Stampa se il numero è pari o dispari.

# Scrivi qui sotto:


# Esercizio 23
# Chiedi all'utente una parola.
# Conta quante lettere contiene usando len() e stampane la lunghezza.

# Scrivi qui sotto:


# Esercizio 24
# Chiedi all'utente tre numeri interi.
# Mettili in una lista e stampa la somma dei tre numeri.

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1
# n = 8
# n += 3
# print(n)

# Soluzione esercizio 2
# testo = "Py"
# testo *= 4
# print(testo)

# Soluzione esercizio 3
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

# Soluzione esercizio 4
# nome = "Mario"
# cognome = "Rossi"
# nome, cognome = cognome, nome
# print(nome, cognome)

# Soluzione esercizio 5
# voto = 24
# if voto >= 18:
#     print("promosso")
# else:
#     print("bocciato")

# Soluzione esercizio 6
# numero = -5
# if numero > 0:
#     print("positivo")
# elif numero < 0:
#     print("negativo")
# else:
#     print("zero")

# Soluzione esercizio 7
# giorno = "lunedi"
# match giorno:
#     case "lunedi":
#         print("lezione")
#     case "domenica":
#         print("pausa")
#     case _:
#         print("altro giorno")

# Soluzione esercizio 8
# for i in range(10):
#     print(i)

# Soluzione esercizio 9
# for i in range(3, 11, 2):
#     print(i)

# Soluzione esercizio 10
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# Soluzione esercizio 11
# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# Soluzione esercizio 12
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# Soluzione esercizio 13
# valori = [10, 20, 30, 40]
# print(valori[0])
# print(valori[-1])

# Soluzione esercizio 14
# numeri = [1, 2, 3]
# numeri[1] = 99
# print(numeri)

# Soluzione esercizio 15
# dati = (5, 10, 15)
# print(dati[1])

# Soluzione esercizio 16
# insieme = set([1, 2, 2, 3, 3, 3])
# print(insieme)

# Soluzione esercizio 17
# insieme = {1, 2, 3}
# insieme.add(4)
# print(insieme)

# Soluzione esercizio 18
# persona = {"nome": "Luca", "eta": 20}
# print(persona["nome"])

# Soluzione esercizio 19
# dati = {}
# dati["corso"] = "Python"
# dati["lezione"] = 3
# print(dati)

# Soluzione esercizio 20
# persona = {"nome": "Anna", "eta": 21}
# for chiave, valore in persona.items():
#     print(chiave, valore)

# Soluzione esercizio 21
# dati = ["Luca", "Rossi", 20]
# nome, cognome, eta = dati
# print(nome)
# print(cognome)
# print(eta)

# Soluzione esercizio 22
# numero = int(input("Inserisci un numero intero: "))
# if numero % 2 == 0:
#     print("pari")
# else:
#     print("dispari")

# Soluzione esercizio 23
# parola = input("Inserisci una parola: ")
# print(len(parola))

# Soluzione esercizio 24
# a = int(input("Inserisci il primo numero: "))
# b = int(input("Inserisci il secondo numero: "))
# c = int(input("Inserisci il terzo numero: "))
# numeri = [a, b, c]
# print(sum(numeri))
