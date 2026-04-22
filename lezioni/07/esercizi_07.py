# Lezione 07 - Esempi ed esercizi su lambda, list comprehension, k-massimi
#
# Questo file contiene:
# 1. esempi introduttivi coerenti con gli appunti della lezione 7
# 2. esercizi da svolgere, dal più semplice al più vicino allo stile esame
# 3. soluzioni commentate in fondo
#
# In questa lezione lavoriamo soprattutto con:
# - funzioni lambda e criteri di ordinamento complessi
# - ordinamenti contrapposti (cambiare segno per invertire ordine numerico)
# - list comprehension: base, con filtro, for nidificati, contenitori nidificati
# - metodologia top-down: k-massimi distruttivo e non distruttivo


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Esempio 1: lambda equivalente a una funzione def
def criterio_def(parola):
    return (len(parola), parola.lower())

criterio_lambda = lambda parola: (len(parola), parola.lower())

parole = ['banana', 'kiwi', 'Mela', 'FICO', 'arancia']
print(sorted(parole, key=criterio_def))
print(sorted(parole, key=criterio_lambda))

print()

# Esempio 2: ordinamento contrapposto
# lunghezza CRESCENTE, a parità ordine alfabetico DECRESCENTE
# → rovesciamo con reverse=True e neghiamo la lunghezza
parole = ['mela', 'kiwi', 'fico', 'uva', 'pesca']
print(sorted(parole, key=lambda el: (-len(el), el), reverse=True))

print()

# Esempio 3: list comprehension base
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati = [x**2 for x in numeri]
print(quadrati)

print()

# Esempio 4: list comprehension con filtro
pari = [x for x in numeri if x % 2 == 0]
print(pari)

print()

# Esempio 5: dict comprehension
quadrati_dict = {x: x**2 for x in numeri}
print(quadrati_dict)

print()

# Esempio 6: k-massimi distruttivo
def estrai_massimo(L):
    assert L, "La lista è vuota"
    M = max(L)
    L.remove(M)
    return M

def k_massimi_distruttivo(L, k):
    assert len(L) > 0, "L è vuota"
    assert 0 < k <= len(L), f"K={k} non valido"
    return [estrai_massimo(L) for _ in range(k)]

lista_test = [3, 7, 1, 9, 4, 6, 2]
print(k_massimi_distruttivo(lista_test, 3))
print("Lista dopo (modificata):", lista_test)


# ====================
# ESERCIZI DEL DOCENTE
# ====================

# Esercizio 1.1 - Lambda semplice
# Data la lista di tuple sotto, ordinala per il secondo elemento crescente,
# poi per il primo elemento decrescente in caso di parità.
#
# dati = [(3, 'banana'), (1, 'mela'), (2, 'banana'), (1, 'kiwi')]
# Risultato atteso: [(2, 'banana'), (3, 'banana'), (1, 'kiwi'), (1, 'mela')]

# Scrivi qui sotto:
dati = [(3, 'banana'), (1, 'mela'), (2, 'banana'), (1, 'kiwi')]


# Esercizio 1.2 - Ordinamento contrapposto con tuple
# Hai una lista di studenti nel formato (nome, voto, eta).
# Ordinali per: voto DECRESCENTE, a parità età CRESCENTE, a parità nome CRESCENTE.
#
# studenti = [('Alice', 8, 22), ('Bob', 9, 20), ('Carlo', 8, 20), ('Diana', 9, 22)]
# Risultato atteso: [('Bob', 9, 20), ('Diana', 9, 22), ('Carlo', 8, 20), ('Alice', 8, 22)]

# Scrivi qui sotto:
studenti = [('Alice', 8, 22), ('Bob', 9, 20), ('Carlo', 8, 20), ('Diana', 9, 22)]


# Esercizio 1.3 - min e max con key
# Usa min() e max() con key= per trovare:
# - la parola più corta della lista (in caso di parità, quella alfabeticamente prima)
# - la parola più lunga della lista (in caso di parità, quella alfabeticamente ultima)
#
# parole = ['gatto', 'cane', 'topo', 'elefante', 'gnu']
# Risultato atteso: min = 'gnu', max = 'elefante'

# Scrivi qui sotto:
parole = ['gatto', 'cane', 'topo', 'elefante', 'gnu']


# Esercizio 2.1 - List comprehension base
# Scrivi una list comprehension che, data una lista di stringhe,
# restituisca una lista con la lunghezza di ciascuna stringa.
#
# Test:
# print(lunghezze(['ciao', 'mondo', 'python']))
# Output atteso: [4, 5, 6]

# Scrivi qui sotto:
def lunghezze(lista):
    pass


# Esercizio 2.2 - List comprehension con filtro
# Scrivi una funzione che, data una lista di interi,
# restituisca solo quelli compresi tra m e M (inclusi), elevati al quadrato.
#
# Test:
# print(quadrati_in_range([1, 2, 3, 4, 5, 6, 7], 3, 6))
# Output atteso: [9, 16, 25, 36]

# Scrivi qui sotto:
def quadrati_in_range(lista, m, M):
    pass


# Esercizio 2.3 - Dict comprehension
# Data una lista di parole, costruisci un dizionario
# che mappa ogni parola alla sua lunghezza,
# ma solo per le parole che iniziano con una vocale.
#
# Test:
# print(parole_vocale(['arancia', 'banana', 'uva', 'mela', 'ananas']))
# Output atteso: {'arancia': 7, 'uva': 3, 'ananas': 6}

# Scrivi qui sotto:
def parole_vocale(lista):
    pass


# Esercizio 2.4 - For nidificati
# Usa una list comprehension con due for per costruire tutte le coppie (i, j)
# con i da 1 a 3 e j da 1 a 3, escludendo quelle dove i == j.
#
# Risultato atteso: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Scrivi qui sotto:


# Esercizio 2.5 - Contenitore nidificato
# Costruisci una lista di liste: per ogni i da 1 a 4,
# costruisci la lista dei multipli di i da 1 a 5.
#
# Risultato atteso:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20]]

# Scrivi qui sotto:


# Esercizio 3.1 - K-massimi non distruttivo
# Scrivi la funzione k_massimi(L, k) che restituisce i k valori più grandi di L
# SENZA modificare la lista originale.
# Usa la funzione estrai_massimo e k_massimi_distruttivo già definite sopra.
#
# Test:
# L = [3, 7, 1, 9, 4, 6, 2]
# print(k_massimi(L, 3))   -> [9, 7, 6]
# print(L)                 -> [3, 7, 1, 9, 4, 6, 2]  (invariata)

# Scrivi qui sotto:
def k_massimi(L, k):
    pass


# Esercizio 3.2 - K-minimi
# Scrivi la funzione k_minimi(L, k) che restituisce i k valori più piccoli di L
# senza modificarla. Ragiona su come adattare la strategia dei k-massimi.
#
# Test:
# print(k_minimi([3, 7, 1, 9, 4, 6, 2], 3))
# Output atteso: [1, 2, 3]

# Scrivi qui sotto:
def k_minimi(L, k):
    pass


# Esercizio 3.3 - Stile esame (FUNC2)
# Implementa la funzione func_esame(D) che:
# - riceve un dizionario D dove ogni chiave è una stringa (nome studente)
#   e ogni valore è una lista di voti interi
# - restituisce una lista di tuple (nome, media) ordinata per:
#   - media DECRESCENTE
#   - a parità di media, nome CRESCENTE
# - considera solo gli studenti con almeno 3 voti
#
# Test:
# D = {
#     'Alice': [8, 9, 7],
#     'Bob': [6, 8],
#     'Carlo': [9, 9, 9],
#     'Diana': [8, 8, 8],
#     'Eva': [7, 9, 8]
# }
# Output atteso: [('Carlo', 9.0), ('Diana', 8.0), ('Alice', 8.0), ('Eva', 8.0)]
# NOTA: Alice e Diana hanno entrambe media 8.0 → ordine alfabetico

# Scrivi qui sotto:
def func_esame(D):
    pass


# ====================
# INTEGRAZIONI MIRATE
# ====================

# Esercizio 4 - Lambda pericolosa
# Cosa stampa questo codice? Prova a rispondere SENZA eseguirlo,
# poi verifica.
#
# parole = ['Python', 'java', 'C', 'ruby', 'Go']
# print(sorted(parole, key=lambda s: (len(s), s.lower())))
# print(sorted(parole, key=lambda s: (-len(s), s.lower()), reverse=True))

# Scrivi qui la tua previsione come commento prima di eseguire:


# Esercizio 5 - Comprehension o ciclo?
# Riscrivi questa funzione usando una list comprehension.
# Se non riesci a farlo in modo leggibile, spiega perché nel commento.
#
# def filtra_e_trasforma(parole):
#     risultato = []
#     for p in parole:
#         if len(p) > 3:
#             risultato.append(p.upper())
#     return risultato

# Scrivi qui sotto:
def filtra_e_trasforma_v2(parole):
    pass


# ====================
#      SOLUZIONI
# ====================

# Togli i commenti alle righe sotto solo dopo aver provato da solo.

# Soluzione esercizio 1.1
# print(sorted(dati, key=lambda t: (t[1], -t[0])))

# Soluzione esercizio 1.2
# print(sorted(studenti, key=lambda s: (-s[1], s[2], s[0])))

# Soluzione esercizio 1.3
# print(min(parole, key=lambda p: (len(p), p)))
# print(max(parole, key=lambda p: (len(p), p)))

# Soluzione esercizio 2.1
# def lunghezze(lista):
#     return [len(s) for s in lista]

# Soluzione esercizio 2.2
# def quadrati_in_range(lista, m, M):
#     return [x**2 for x in lista if m <= x <= M]

# Soluzione esercizio 2.3
# def parole_vocale(lista):
#     vocali = set('aeiouAEIOU')
#     return {p: len(p) for p in lista if p[0] in vocali}

# Soluzione esercizio 2.4
# coppie = [(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
# print(coppie)

# Soluzione esercizio 2.5
# tabella = [[i * j for j in range(1, 6)] for i in range(1, 5)]
# for riga in tabella:
#     print(riga)

# Soluzione esercizio 3.1
# def k_massimi(L, k):
#     L1 = L.copy()
#     return k_massimi_distruttivo(L1, k)

# Soluzione esercizio 3.2
# def estrai_minimo(L):
#     m = min(L)
#     L.remove(m)
#     return m
#
# def k_minimi(L, k):
#     assert len(L) > 0 and 0 < k <= len(L)
#     L1 = L.copy()
#     return [estrai_minimo(L1) for _ in range(k)]

# Soluzione esercizio 3.3
# def func_esame(D):
#     medie = [(nome, sum(voti) / len(voti))
#              for nome, voti in D.items()
#              if len(voti) >= 3]
#     return sorted(medie, key=lambda t: (-t[1], t[0]))

# Soluzione esercizio 5
# def filtra_e_trasforma_v2(parole):
#     return [p.upper() for p in parole if len(p) > 3]
