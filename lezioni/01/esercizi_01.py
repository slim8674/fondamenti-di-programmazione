# Lezione 1 - Esempi ed esercizi base
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

# Un valore intero
numero_intero = 10
print(numero_intero)

# Un valore decimale
numero_decimale = 3.14
print(numero_decimale)

# Controllo del tipo di dato
print(type(numero_intero))
print(type(numero_decimale))

# Un numero intero scritto con underscore per leggibilità
grande_numero = 100_000
print(grande_numero)
print(type(grande_numero))

# Operazioni matematiche di base
print(3 + 2)    # somma
print(10 - 4)   # sottrazione
print(5 * 6)    # moltiplicazione
print(8 / 2)    # divisione normale -> float

# Operazioni particolari
print(10 // 3)  # divisione intera
print(10 % 3)   # resto della divisione
print(2 ** 3)   # potenza


# ====================
# ESERCIZI
# ====================

# Esercizio 1
# Crea una variabile chiamata a e assegnale il valore 25.
# Stampala.

# Scrivi qui sotto:


# Esercizio 2
# Crea una variabile chiamata b e assegnale il valore 7.5.
# Stampa il valore e il suo tipo.

# Scrivi qui sotto:


# Esercizio 3
# Scrivi un numero grande usando l'underscore, ad esempio un milione.
# Stampalo e controlla il tipo.

# Scrivi qui sotto:


# Esercizio 4
# Calcola e stampa il risultato delle seguenti operazioni:
# 12 + 8
# 20 - 5
# 4 * 6
# 15 / 2

# Scrivi qui sotto:


# Esercizio 5
# Calcola e stampa:
# la divisione intera tra 17 e 5
# il resto della divisione tra 17 e 5
# 3 elevato alla 4

# Scrivi qui sotto:


# Esercizio 6
# Osserva la differenza tra / e //.
# Calcola:
# 10 / 3
# 10 // 3

# Scrivi qui sotto:


# Esercizio 7
# Usa la funzione type() sui seguenti valori:
# 42
# 2.5
# 50_000

# Scrivi qui sotto:


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1
# a = 25
# print(a)

# Soluzione esercizio 2
b = 7.5
print(b)
print(type(b))

# Soluzione esercizio 3
grande = 1_000_000
print(grande)
print(type(grande))

# Soluzione esercizio 4
print(12 + 8)
print(20 - 5)
print(4 * 6)
print(15 / 2)

# Soluzione esercizio 5
print(17 // 5)
print(17 % 5)
print(3 ** 4)

# Soluzione esercizio 6
print(10 / 3)
print(10 // 3)

# Soluzione esercizio 7
print(type(42))
print(type(2.5))
print(type(50_000))