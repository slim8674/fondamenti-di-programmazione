# Lezione 07 - Lambda, list comprehension, k-massimi
#
# Contenuto:
# 1. Esempi introduttivi
# 2. Esercizi (dal più semplice allo stile esame)
# 3. Soluzioni commentate in fondo
#
# Argomenti:
# - Funzioni lambda e criteri di ordinamento
# - Ordinamenti con criteri misti (crescente/decrescente)
# - List comprehension: base, con filtro, nidificata
# - Dict comprehension
# - Metodologia top-down: k-massimi distruttivo e non distruttivo


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# ── Esempio 1: lambda equivalente a def ──────────────────────────────────────
# Una lambda è solo una funzione anonima su una riga.
# Le due forme seguenti sono equivalenti.

def criterio_def(parola):
    return (len(parola), parola.lower())

criterio_lambda = lambda parola: (len(parola), parola.lower())

parole = ['banana', 'kiwi', 'Mela', 'FICO', 'arancia']
print(sorted(parole, key=criterio_def))     # con def
print(sorted(parole, key=criterio_lambda))  # con lambda (stesso risultato)

print()

# ── Esempio 2: ordinamenti misti (crescente e decrescente insieme) ────────────
# Problema: ordinare per lunghezza DECRESCENTE;
#            a parità di lunghezza, ordine alfabetico CRESCENTE.
#
# Soluzione: negare il valore numerico inverte quell'asse.
#   key = (-len(el), el)   →   lunghezza decrescente, alfabetico crescente
#
# ATTENZIONE: NON aggiungere reverse=True, altrimenti si inverte tutto
# e il risultato è opposto a quello voluto.

parole = ['mela', 'kiwi', 'fico', 'uva', 'pesca']
print(sorted(parole, key=lambda el: (-len(el), el)))
# Output: ['pesca', 'mela', 'kiwi', 'fico', 'uva']
#          ^^^^^ 5 lettere    ^^^^ 4 lettere (alfa)   ^^^ 3

print()

# ── Esempio 3: list comprehension base ───────────────────────────────────────
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati = [x**2 for x in numeri]
print(quadrati)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print()

# ── Esempio 4: list comprehension con filtro ─────────────────────────────────
pari = [x for x in numeri if x % 2 == 0]
print(pari)  # [2, 4, 6, 8, 10]

print()

# ── Esempio 5: dict comprehension ────────────────────────────────────────────
quadrati_dict = {x: x**2 for x in numeri}
print(quadrati_dict)  # {1: 1, 2: 4, ..., 10: 100}

print()

# ── Esempio 6: k-massimi distruttivo ─────────────────────────────────────────
# "Distruttivo" significa che la lista originale viene modificata.
# La funzione estrai_massimo rimuove e restituisce il massimo.
# k_massimi_distruttivo la chiama k volte con una comprehension.

def estrai_massimo(L):
    """Rimuove e restituisce il valore massimo di L (modifica L)."""
    assert L, "La lista è vuota"
    M = max(L)
    L.remove(M)
    return M

def k_massimi_distruttivo(L, k):
    """Restituisce i k massimi in ordine decrescente. MODIFICA L."""
    assert len(L) > 0,        "L è vuota"
    assert 0 < k <= len(L),   f"k={k} non valido per una lista di {len(L)} elementi"
    return [estrai_massimo(L) for _ in range(k)]

lista_test = [3, 7, 1, 9, 4, 6, 2]
print(k_massimi_distruttivo(lista_test, 3))     # [9, 7, 6]
print("Lista dopo (modificata):", lista_test)   # [3, 1, 4, 2]

print()


# ====================
# ESERCIZI
# ====================

# ── Esercizio 1.1 ─ Lambda semplice ──────────────────────────────────────────
# Ordina la lista di tuple per secondo elemento CRESCENTE;
# a parità di secondo elemento, per primo elemento DECRESCENTE.
#
# dati = [(3, 'banana'), (1, 'mela'), (2, 'banana'), (1, 'kiwi')]
#
# Risultato atteso: [(2, 'banana'), (3, 'banana'), (1, 'kiwi'), (1, 'mela')]
#
# Suggerimento: la tupla-chiave è (t[1], -t[0])

dati = [(3, 'banana'), (1, 'mela'), (2, 'banana'), (1, 'kiwi')]
# Scrivi qui sotto:


# ── Esercizio 1.2 ─ Ordinamento con tre criteri ───────────────────────────────
# Ordina gli studenti (nome, voto, età) per:
#   1. voto DECRESCENTE
#   2. età CRESCENTE (a parità di voto)
#   3. nome CRESCENTE (a parità di voto e età)
#
# studenti = [('Alice', 8, 22), ('Bob', 9, 20), ('Carlo', 8, 20), ('Diana', 9, 22)]
#
# Risultato atteso: [('Bob', 9, 20), ('Diana', 9, 22), ('Carlo', 8, 20), ('Alice', 8, 22)]

studenti = [('Alice', 8, 22), ('Bob', 9, 20), ('Carlo', 8, 20), ('Diana', 9, 22)]
# Scrivi qui sotto:


# ── Esercizio 1.3 ─ min e max con key ─────────────────────────────────────────
# Trova:
# - la parola più corta (a parità: la prima in ordine alfabetico)
# - la parola più lunga (a parità: l'ultima in ordine alfabetico)
#
# parole = ['gatto', 'cane', 'topo', 'elefante', 'gnu']
#
# Risultato atteso: min → 'gnu',  max → 'elefante'
#
# Nota: per min usiamo key=(len, p) → preferisce la più corta e poi la prima alfa.
#       per max usiamo key=(len, p) → preferisce la più lunga e poi l'ultima alfa.

parole = ['gatto', 'cane', 'topo', 'elefante', 'gnu']
# Scrivi qui sotto:


# ── Esercizio 2.1 ─ List comprehension base ───────────────────────────────────
# Restituisci la lista delle lunghezze delle stringhe.
#
# lunghezze(['ciao', 'mondo', 'python'])  →  [4, 5, 6]

def lunghezze(lista):
    pass  # scrivi qui


# ── Esercizio 2.2 ─ List comprehension con filtro ─────────────────────────────
# Restituisci i quadrati degli interi compresi tra m e M (inclusi).
#
# quadrati_in_range([1, 2, 3, 4, 5, 6, 7], 3, 6)  →  [9, 16, 25, 36]

def quadrati_in_range(lista, m, M):
    pass  # scrivi qui


# ── Esercizio 2.3 ─ Dict comprehension ───────────────────────────────────────
# Costruisci un dizionario {parola: lunghezza} solo per le parole
# che iniziano con una vocale.
#
# parole_vocale(['arancia', 'banana', 'uva', 'mela', 'ananas'])
#   →  {'arancia': 7, 'uva': 3, 'ananas': 6}

def parole_vocale(lista):
    pass  # scrivi qui


# ── Esercizio 2.4 ─ For nidificati ────────────────────────────────────────────
# Costruisci tutte le coppie (i, j) con i, j in {1,2,3} e i ≠ j.
#
# Risultato atteso: [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# Scrivi qui sotto:


# ── Esercizio 2.5 ─ Lista di liste ────────────────────────────────────────────
# Costruisci la tabella dei multipli: per ogni i da 1 a 4,
# la lista [i*1, i*2, i*3, i*4, i*5].
#
# Risultato atteso:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20]]

# Scrivi qui sotto:


# ── Esercizio 3.1 ─ K-massimi NON distruttivo ─────────────────────────────────
# Restituisci i k valori più grandi SENZA modificare la lista originale.
# Riusa estrai_massimo e k_massimi_distruttivo definiti sopra.
#
# L = [3, 7, 1, 9, 4, 6, 2]
# k_massimi(L, 3)  →  [9, 7, 6]
# L rimane [3, 7, 1, 9, 4, 6, 2]

def k_massimi(L, k):
    pass  # scrivi qui


# ── Esercizio 3.2 ─ K-minimi ─────────────────────────────────────────────────
# Restituisci i k valori più piccoli senza modificare L.
# Adatta la strategia dei k-massimi.
#
# k_minimi([3, 7, 1, 9, 4, 6, 2], 3)  →  [1, 2, 3]

def k_minimi(L, k):
    pass  # scrivi qui


# ── Esercizio 3.3 ─ Stile esame ───────────────────────────────────────────────
# Implementa func_esame(D):
# - D: dizionario {nome_studente: [voti]}
# - Considera solo gli studenti con almeno 3 voti
# - Restituisce lista di tuple (nome, media) ordinata per:
#     media DECRESCENTE, a parità nome CRESCENTE
#
# D = {
#     'Alice': [8, 9, 7],
#     'Bob': [6, 8],          ← escluso (meno di 3 voti)
#     'Carlo': [9, 9, 9],
#     'Diana': [8, 8, 8],
#     'Eva': [7, 9, 8],
# }
# Output atteso: [('Carlo', 9.0), ('Alice', 8.0), ('Diana', 8.0), ('Eva', 8.0)]

def func_esame(D):
    pass  # scrivi qui


# ── Esercizio 4 ─ Analisi a freddo ────────────────────────────────────────────
# Cosa stampa questo codice? Rispondi SENZA eseguirlo, poi verifica.
#
# parole = ['Python', 'java', 'C', 'ruby', 'Go']
# print(sorted(parole, key=lambda s: (len(s), s.lower())))
# print(sorted(parole, key=lambda s: (-len(s), s.lower())))

# Scrivi qui la tua previsione come commento:
# Prima print:  ...
# Seconda print: ...


# ── Esercizio 5 ─ Da ciclo a comprehension ────────────────────────────────────
# Riscrivi la funzione usando una list comprehension.
#
# def filtra_e_trasforma(parole):
#     risultato = []
#     for p in parole:
#         if len(p) > 3:
#             risultato.append(p.upper())
#     return risultato

def filtra_e_trasforma_v2(parole):
    pass  # scrivi qui


# ====================
#      SOLUZIONI
# ====================
# Rimuovi i commenti solo dopo aver provato da solo.

# ── Soluzione 1.1
# print(sorted(dati, key=lambda t: (t[1], -t[0])))

# ── Soluzione 1.2
# print(sorted(studenti, key=lambda s: (-s[1], s[2], s[0])))

# ── Soluzione 1.3
# print(min(parole, key=lambda p: (len(p), p)))
# print(max(parole, key=lambda p: (len(p), p)))

# ── Soluzione 2.1
# def lunghezze(lista):
#     return [len(s) for s in lista]

# ── Soluzione 2.2
# def quadrati_in_range(lista, m, M):
#     return [x**2 for x in lista if m <= x <= M]

# ── Soluzione 2.3
# def parole_vocale(lista):
#     vocali = set('aeiouAEIOU')
#     return {p: len(p) for p in lista if p[0] in vocali}

# ── Soluzione 2.4
# coppie = [(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
# print(coppie)

# ── Soluzione 2.5
# tabella = [[i * j for j in range(1, 6)] for i in range(1, 5)]
# for riga in tabella:
#     print(riga)

# ── Soluzione 3.1
# def k_massimi(L, k):
#     return k_massimi_distruttivo(L.copy(), k)

# ── Soluzione 3.2
# def estrai_minimo(L):
#     m = min(L)
#     L.remove(m)
#     return m
#
# def k_minimi(L, k):
#     assert len(L) > 0 and 0 < k <= len(L)
#     L1 = L.copy()
#     return [estrai_minimo(L1) for _ in range(k)]

# ── Soluzione 3.3
# def func_esame(D):
#     medie = [(nome, sum(voti) / len(voti))
#              for nome, voti in D.items()
#              if len(voti) >= 3]
#     return sorted(medie, key=lambda t: (-t[1], t[0]))

# ── Soluzione 4
# Prima print:  ['C', 'Go', 'java', 'ruby', 'Python']
#   → lunghezza crescente; a parità, alfabetico crescente (case-insensitive)
# Seconda print: ['Python', 'java', 'ruby', 'go', 'c']
#   → lunghezza decrescente; a parità, alfabetico crescente (case-insensitive)
#   NOTA: NON aggiungere reverse=True, il segno negativo è sufficiente.

# ── Soluzione 5
# def filtra_e_trasforma_v2(parole):
#     return [p.upper() for p in parole if len(p) > 3]