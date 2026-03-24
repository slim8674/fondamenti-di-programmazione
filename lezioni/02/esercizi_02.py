# Lezione 02 - Esempi ed esercizi su stringhe, input e booleani
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

# Stringhe
nome = "Paperino"
print(nome)
print(type(nome))

# Concatenazione di stringhe
nome_completo = "Paperino" + " " + "Duck"
print(nome_completo)

# Ripetizione di stringhe
risata = "ha" * 3
print(risata)

# Lunghezza di una stringa
print(len(nome))

# Accesso ai caratteri tramite indice
print(nome[0])   # primo carattere
print(nome[-1])  # ultimo carattere

# Slicing
saluto = "ciaosonoio"
print(saluto[0:4])   # ciao
print(saluto[:4])    # ciao
print(saluto[4:])    # sonoio
print(saluto[::2])   # un carattere ogni 2
print(saluto[::-1])  # stringa al contrario

# Metodi utili delle stringhe
frase = "Ciao Sono IO"
print(frase.lower())
print(frase.upper())
print(frase.find("S"))

# Split di una frase
testo = "Paperino andò al mare con Pippo"
parole = testo.split()
print(parole)

# Conversioni di tipo
numero_testo = "23"
print(int(numero_testo))
print(float(numero_testo))
print(str(42))

# Input da tastiera
# input() restituisce sempre una stringa
nome_utente = input("Come ti chiami? ")
print("Ciao", nome_utente)

# Booleani
print(True)
print(False)
print(type(True))

# Valori interpretati come veri o falsi
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("ciao"))

# Confronti
print(3 < 5)
print(10 == 10)
print("Paperino" < "Topolino")

# Operatori logici
print(True and False)
print(True or False)
print(not True)


# ====================
# ESERCIZI
# ====================

# Esercizio 1
# Crea una variabile chiamata parola e assegnale una stringa a scelta.
# Stampala e stampa il suo tipo.

# Scrivi qui sotto:


# Esercizio 2
# Crea due stringhe con nome e cognome.
# Uniscile in una nuova variabile con uno spazio in mezzo.
# Stampa il risultato.

# Scrivi qui sotto:


# Esercizio 3
# Crea una stringa con il valore "ciao".
# Stampala ripetuta 4 volte.

# Scrivi qui sotto:


# Esercizio 4
# Crea una stringa con il tuo nome.
# Stampa:
# - il primo carattere
# - l'ultimo carattere
# - la lunghezza del nome

# Scrivi qui sotto:


# Esercizio 5
# Crea una stringa con valore "programmazione".
# Stampa:
# - i primi 5 caratteri
# - gli ultimi 4 caratteri
# - la stringa al contrario

# Scrivi qui sotto:


# Esercizio 6
# Crea una stringa con una frase a scelta.
# Stampala tutta in minuscolo e tutta in maiuscolo.

# Scrivi qui sotto:


# Esercizio 7
# Crea una stringa con una frase.
# Usa split() e stampa la lista delle parole.

# Scrivi qui sotto:


# Esercizio 8
# Converti le seguenti stringhe:
# - "15" in int
# - "7.5" in float
# - 42 in stringa
# Poi stampa i risultati.

# Scrivi qui sotto:


# Esercizio 9
# Chiedi all'utente di inserire il proprio nome.
# Stampa un messaggio di saluto.

# Scrivi qui sotto:


# Esercizio 10
# Chiedi all'utente di inserire la propria età.
# Converti il valore in intero e stampalo con il tipo.

# Scrivi qui sotto:


# Esercizio 11
# Usa bool() sui seguenti valori e stampa il risultato:
# 0
# 1
# ""
# "python"

# Scrivi qui sotto:


# Esercizio 12
# Stampa il risultato dei seguenti confronti:
# 7 > 3
# 5 == 2
# 9 != 4
# "ciao" < "zaino"

# Scrivi qui sotto:


# Esercizio 13
# Stampa il risultato delle seguenti espressioni logiche:
# True and True
# True and False
# False or True
# not False

# Scrivi qui sotto:


# Esercizio 14
# Crea due variabili a e b con lo stesso valore numerico.
# Stampa il risultato di:
# - a == b
# - a is b
# Nota:
# == confronta il contenuto
# is confronta l'identità dell'oggetto

# Scrivi qui sotto:


# Esercizio 15
# Chiedi all'utente nome, cognome e città.
# Costruisci una frase con una f-string e stampala.
# Esempio:
# "Ciao Luca Rossi, vivi a Roma."

# Scrivi qui sotto:


# Esercizio 16
# Chiedi all'utente una parola.
# Stampa la posizione della lettera "a" usando find().

# Scrivi qui sotto:


# Esercizio 17
# Chiedi all'utente una parola.
# Stampa:
# - i primi 3 caratteri
# - gli ultimi 2 caratteri
# - un carattere ogni 2

# Scrivi qui sotto:


# Esercizio 18
# Chiedi all'utente una frase.
# Stampa:
# - la lista ottenuta con split()
# - il numero di parole presenti

# Scrivi qui sotto:


# Esercizio 19
# Chiedi due numeri interi.
# Stampa:
# - la loro somma
# - il loro prodotto
# - il tipo dei risultati

# Scrivi qui sotto:


# Esercizio 20
# Chiedi due numeri interi.
# Stampa:
# - la divisione normale
# - la divisione intera
# - il resto

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1
# parola = "Python"
# print(parola)
# print(type(parola))

# Soluzione esercizio 2
# nome = "Mario"
# cognome = "Rossi"
# nome_completo = nome + " " + cognome
# print(nome_completo)

# Soluzione esercizio 3
# saluto = "ciao"
# print(saluto * 4)

# Soluzione esercizio 4
# nome = "Luca"
# print(nome[0])
# print(nome[-1])
# print(len(nome))

# Soluzione esercizio 5
# parola = "programmazione"
# print(parola[:5])
# print(parola[-4:])
# print(parola[::-1])

# Soluzione esercizio 6
# frase = "Ciao Come Stai"
# print(frase.lower())
# print(frase.upper())

# Soluzione esercizio 7
# frase = "oggi studio python"
# print(frase.split())

# Soluzione esercizio 8
# print(int("15"))
# print(float("7.5"))
# print(str(42))

# Soluzione esercizio 9
# nome = input("Come ti chiami? ")
# print("Ciao", nome)

# Soluzione esercizio 10
# eta = int(input("Quanti anni hai? "))
# print(eta)
# print(type(eta))

# Soluzione esercizio 11
# print(bool(0))
# print(bool(1))
# print(bool(""))
# print(bool("python"))

# Soluzione esercizio 12
# print(7 > 3)
# print(5 == 2)
# print(9 != 4)
# print("ciao" < "zaino")

# Soluzione esercizio 13
# print(True and True)
# print(True and False)
# print(False or True)
# print(not False)

# Soluzione esercizio 14
# a = 5
# b = 5
# print(a == b)
# print(a is b)

# Soluzione esercizio 15
# nome = input("Inserisci il nome: ")
# cognome = input("Inserisci il cognome: ")
# citta = input("Inserisci la città: ")
# messaggio = f"Ciao {nome} {cognome}, vivi a {citta}."
# print(messaggio)

# Soluzione esercizio 16
# parola = input("Inserisci una parola: ")
# print(parola.find("a"))

# Soluzione esercizio 17
# parola = input("Inserisci una parola: ")
# print(parola[:3])
# print(parola[-2:])
# print(parola[::2])

# Soluzione esercizio 18
# frase = input("Inserisci una frase: ")
# parole = frase.split()
# print(parole)
# print(len(parole))

# Soluzione esercizio 19
# a = int(input("Inserisci il primo numero intero: "))
# b = int(input("Inserisci il secondo numero intero: "))
# somma = a + b
# prodotto = a * b
# print(somma)
# print(prodotto)
# print(type(somma))
# print(type(prodotto))

# Soluzione esercizio 20
# a = int(input("Inserisci il primo numero intero: "))
# b = int(input("Inserisci il secondo numero intero: "))
# print(a / b)
# print(a // b)
# print(a % b)