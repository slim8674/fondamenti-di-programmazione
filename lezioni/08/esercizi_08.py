# Lezione 08 - Esempi ed esercizi su complessità, ricerca binaria, k-massimi
#
# Questo file contiene:
# 1. esempi introduttivi coerenti con gli appunti della lezione 8
# 2. esercizi dalla simulazione ufficiale del prof. Masi (base → medio → difficile)
# 3. esercizi originali su ricerca binaria e k-massimi (stile lezione 8)
# 4. esercizio stile esame (FUNC2/FUNC3)
# 5. soluzioni commentate in fondo
#
# Argomenti coperti:
# - assert e raise per validare input
# - manipolazione stringhe e liste (ripasso da simulazione)
# - ordinamento con criteri multipli e contrapposti (ripasso + approfondimento)
# - k-massimi con sorted() e slicing
# - ricerca binaria su lista ordinata


# ====================
# ESEMPI INTRODUTTIVI
# ====================

# Esempio 1: assert vs raise
# assert → per controlli interni durante sviluppo (disattivabile con -O)
# raise  → per errori che devono sempre essere gestiti

def dividi(a, b):
    if b == 0:
        raise ValueError("Il divisore non può essere zero")
    return a / b

def somma_lista(L):
    assert isinstance(L, list), "L deve essere una lista"
    return sum(L)

print(dividi(10, 2))        # 5.0
# print(dividi(10, 0))      # ValueError

print()

# Esempio 2: k-massimi con sorted (pattern esame)
def k_massimi_sorted(L, k):
    assert 0 < k <= len(L), f"K={k} non valido"
    return sorted(L, reverse=True)[:k]

lista = [3, 7, 1, 9, 4, 6, 2, 8, 5]
print(k_massimi_sorted(lista, 3))   # [9, 8, 7]
print("Lista invariata:", lista)    # non distruttiva

print()

# Esempio 3: ricerca binaria su lista decrescente
# Restituisce la posizione dell'elemento o la posizione di inserimento
def ricerca_binaria(Lista, Valore):
    inizio = 0
    fine = len(Lista) - 1
    while inizio <= fine:
        centrale = (inizio + fine) // 2
        valore_centrale = Lista[centrale]
        if Valore == valore_centrale:
            return centrale
        elif Valore < valore_centrale:
            inizio = centrale + 1   # su lista decrescente i piccoli stanno a destra
        else:
            fine = centrale - 1
    return inizio

ordinata = [100, 80, 60, 40, 20, 0]
print(ricerca_binaria(ordinata, 60))    # 2 — trovato
print(ricerca_binaria(ordinata, 50))    # 3 — posizione di inserimento
print(ricerca_binaria(ordinata, 110))   # 0 — va in testa


# ================================
# SIMULAZIONE PROF. MASI — RIPASSO
# ================================
# Esercizi selezionati dalla simulazione ufficiale.
# Coprono stringhe, liste, dizionari e ordinamento.
# Difficoltà crescente: Facile → Medio → Difficile.

# --- SM.1 - Facile ---
# Data una stringa S (di soli numeri) e una stringa T (numeri + caratteri),
# restituisci una lista con il conteggio di ogni SINGOLA cifra di S in T.
#
# Esempi attesi:
# check_S_in_T('1234', 'p1p2p335o')  → [1, 1, 2, 0]
# check_S_in_T('13', 'p1p2p335o')    → [1, 2]

def check_S_in_T(S, T):
    pass


# --- SM.2 - Medio ---
# Data una stringa "query" e una stringa "corpo", conta quante volte
# "query" è contenuta in "corpo".
# NB: NON usare il metodo .count() delle stringhe.
#
# Esempi attesi:
# count_sub_string('pippo', 'pipppippopipipipipippppppippo')  → 2
# count_sub_string('aba', 'abababababababa')                  → 7

def count_sub_string(query, corpo):
    pass


# --- SM.3 - Medio ---
# Data una lista L di interi, rimuovi in-place il minimo e il massimo
# (unici per ipotesi) e restituisci la coppia (minimo, massimo).
# La lista NON può essere vuota.
#
# Esempi attesi:
# L = [0, 5, 42, -1, 5, 3, 23]
# get_list_except_min_max(L) → (-1, 42)  e  L = [0, 5, 5, 3, 23]
#
# L = [0, 4]
# get_list_except_min_max(L) → (0, 4)    e  L = []

def get_list_except_min_max(L):
    pass


# --- SM.4 - Medio/Difficile ---
# Data una lista L di interi, rimuovi in-place TUTTI i valori uguali
# al minimo e TUTTI i valori uguali al massimo.
# La lista può essere vuota. Minimo e massimo possono coincidere.
# Restituisci il numero totale di elementi eliminati.
#
# Esempi attesi:
# L = [5, 5, 5, 5, 5]         → restituisce 5,  L = []
# L = [-11, 13, -11, 13, -11] → restituisce 5,  L = []
# L = [-5, 2, -5, 10, -11, -11, 10, 0, -11, 2]
#                              → restituisce 5,  L = [-5, 2, -5, 0, 2]
# L = []                       → restituisce 0,  L = []

def get_list_except_min_max_general(L):
    pass


# --- SM.5 - Medio/Difficile ---
# Data una tupla T di stringhe, restituisci una tupla S ordinata per:
# - lunghezza CRESCENTE
# - a parità di lunghezza, ordine lessicografico DECRESCENTE
#
# Esempi attesi:
# sort_by_str(('aaaaa', 'aaa', 'zzzzz', 'zzz'))  → ('zzz', 'aaa', 'zzzzz', 'aaaaa')

def sort_by_str(T):
    pass


# --- SM.6 - Difficile ---
# Data una lista di interi L, genera una stringa che rappresenta
# un istogramma a caratteri.
# Formato di ogni riga: "valore\t" + "*" × frequenza + "\n"
# L'istogramma va dal valore minimo al massimo (inclusi), anche se la
# frequenza è 0.
#
# Esempi attesi:
# L = [1, 1, 1, 1, 4, 4, 4, 5, 5, 10, 10]
# int_to_hist(L) == '1\t****\n2\t\n3\t\n4\t***\n5\t**\n6\t\n7\t\n8\t\n9\t\n10\t**\n'

def int_to_hist(L):
    pass


# ===================================================
# ESERCIZI ORIGINALI — LEZIONE 8
# ===================================================

# --- OR.1 - assert e raise ---
# Scrivi media(L) che:
# - lancia TypeError se L non è una lista
# - lancia ValueError se L è vuota
# - restituisce la media aritmetica
#
# Esempi attesi:
# media([4, 8, 6])  → 6.0
# media([])         → ValueError
# media("ciao")     → TypeError

def media(L):
    pass


# --- OR.2 - k-massimi con gestione errori ---
# Scrivi k_massimi(L, k) che:
# - lancia ValueError se L è vuota o k non è valido
# - restituisce i k valori più grandi in ordine decrescente
# - NON modifica L
#
# Esempi attesi:
# k_massimi([5, 2, 8, 1, 9, 3], 3)  → [9, 8, 5]
# k_massimi([], 1)                   → ValueError
# k_massimi([1, 2, 3], 0)            → ValueError

def k_massimi(L, k):
    pass


# --- OR.3 - Ricerca binaria su lista CRESCENTE ---
# La versione negli esempi lavora su lista DECRESCENTE.
# Riscrivi ricerca_binaria_crescente(Lista, Valore) per lista CRESCENTE.
# La logica si inverte: attenzione alla direzione!
#
# Esempi attesi:
# lista = [0, 10, 20, 30, 40, 50]
# ricerca_binaria_crescente(lista, 30)  → 3   (trovato)
# ricerca_binaria_crescente(lista, 25)  → 3   (posizione di inserimento)
# ricerca_binaria_crescente(lista, 60)  → 6   (da inserire in fondo)

def ricerca_binaria_crescente(Lista, Valore):
    pass


# --- OR.4 - Inserimento in lista ordinata decrescente ---
# Scrivi inserisci_ordinato(Lista, Valore) che inserisce Valore
# nella posizione corretta di Lista (già decrescente), mantenendo l'ordine.
# Usa ricerca_binaria() definita negli esempi.
#
# Esempi attesi:
# L = [90, 70, 50, 30, 10]
# inserisci_ordinato(L, 60)  → L diventa [90, 70, 60, 50, 30, 10]
# inserisci_ordinato(L, 100) → L diventa [100, 90, 70, 60, 50, 30, 10]

def inserisci_ordinato(Lista, Valore):
    pass


# ====================
# INTEGRAZIONI MIRATE
# ====================

# Integrazione 1 — Riflessione sulla complessità
# Stima il costo nel caso peggiore con la notazione O.
# Verifica le risposte nelle soluzioni in fondo.
#
# a) sorted(L, reverse=True)[:k]                  → O(?)
# b) [estrai_massimo(L) for _ in range(k)]        → O(?)
# c) ricerca_binaria(Lista, Valore)                → O(?)
# d) L.copy()                                      → O(?)


# Integrazione 2 — Riscrittura top-down
# La funzione sotto funziona ma è monolitica.
# Riscrivila in due funzioni: una che valida, una che calcola.

def k_min_monolitico(L, k):
    if k < 1 or k > len(L):
        return None
    return sorted(L)[:k]

# Scrivi la versione top-down qui sotto:


# ======================
# ESERCIZIO STILE ESAME
# ======================

# FUNC3 — top_k_giocatori
# Data una lista di dizionari con campi 'nome' (str) e 'punteggio' (int),
# restituisci i k giocatori con punteggio più alto, ordinati per:
# - punteggio DECRESCENTE
# - a parità di punteggio, nome CRESCENTE (alfabetico)
# Lancia ValueError se k < 1 o k > len(giocatori).
#
# Esempi attesi:
# giocatori = [
#     {'nome': 'Alice', 'punteggio': 90},
#     {'nome': 'Bob',   'punteggio': 85},
#     {'nome': 'Carlo', 'punteggio': 90},
#     {'nome': 'Diana', 'punteggio': 75},
# ]
# top_k_giocatori(giocatori, 2)
# → [{'nome': 'Alice', 'punteggio': 90}, {'nome': 'Carlo', 'punteggio': 90}]
# top_k_giocatori(giocatori, 3)
# → [{'nome': 'Alice', 'punteggio': 90}, {'nome': 'Carlo', 'punteggio': 90},
#    {'nome': 'Bob', 'punteggio': 85}]

def top_k_giocatori(giocatori, k):
    pass


# ====================
# SOLUZIONI
# ====================
# Decommentare un blocco alla volta, solo dopo aver provato.

# --- Soluzione SM.1 ---
# def check_S_in_T(S, T):
#     return [T.count(C) for C in S]


# --- Soluzione SM.2 ---
# def count_sub_string(query, corpo):
#     conteggio = 0
#     for pos in range(len(corpo)):
#         if corpo[pos:pos+len(query)] == query:
#             conteggio += 1
#     return conteggio


# --- Soluzione SM.3 ---
# def get_list_except_min_max(L):
#     m = min(L)
#     M = max(L)
#     L.remove(m)
#     L.remove(M)
#     return m, M


# --- Soluzione SM.4 ---
# def get_list_except_min_max_general(L):
#     if not L:
#         return 0
#     conteggio = 0
#     m = min(L)
#     M = max(L)
#     while m in L:
#         L.remove(m)
#         conteggio += 1
#     while M in L:
#         L.remove(M)
#         conteggio += 1
#     return conteggio


# --- Soluzione SM.5 ---
# def sort_by_str(T):
#     # criterio: lunghezza crescente, a parità lessicografico decrescente
#     # con reverse=True: (-len) crescente → len decrescente... non funziona diretto
#     # soluzione corretta: chiave (len, parola) con reverse=True inverte entrambi
#     # → len decrescente ✗, parola decrescente ✗
#     # Soluzione con negazione manuale: non si può negare una stringa.
#     # Il prof usa la chiave (-len, parola) con reverse=True nella simulazione:
#     return tuple(sorted(T, key=lambda p: (-len(p), p), reverse=True))
#
# NOTA critica: questa soluzione del prof produce lunghezza DECRESCENTE
# (perché reverse=True e la chiave è -len → doppia negazione → decrescente).
# Se la consegna dice CRESCENTE, la chiave corretta è (len, p) senza reverse.
# Leggi sempre con attenzione cosa chiede la consegna.


# --- Soluzione SM.6 ---
# def int_to_hist(L):
#     frequenze = {}
#     for x in L:
#         frequenze[x] = frequenze.get(x, 0) + 1
#     risultato = ''
#     for i in range(min(frequenze), max(frequenze) + 1):
#         risultato += f"{i}\t{'*' * frequenze.get(i, 0)}\n"
#     return risultato


# --- Soluzione OR.1 ---
# def media(L):
#     if not isinstance(L, list):
#         raise TypeError("L deve essere una lista")
#     if not L:
#         raise ValueError("L è vuota")
#     return sum(L) / len(L)


# --- Soluzione OR.2 ---
# def k_massimi(L, k):
#     if not L:
#         raise ValueError("L è vuota")
#     if not (1 <= k <= len(L)):
#         raise ValueError(f"K={k} non valido")
#     return sorted(L, reverse=True)[:k]


# --- Soluzione OR.3 ---
# def ricerca_binaria_crescente(Lista, Valore):
#     inizio = 0
#     fine = len(Lista) - 1
#     while inizio <= fine:
#         centrale = (inizio + fine) // 2
#         valore_centrale = Lista[centrale]
#         if Valore == valore_centrale:
#             return centrale
#         elif Valore > valore_centrale:
#             inizio = centrale + 1   # su lista crescente i grandi stanno a destra
#         else:
#             fine = centrale - 1
#     return inizio


# --- Soluzione OR.4 ---
# def inserisci_ordinato(Lista, Valore):
#     pos = ricerca_binaria(Lista, Valore)
#     Lista.insert(pos, Valore)


# --- Soluzione Integrazione 1 ---
# a) O(N log N) — dominato dall'ordinamento
# b) O(K × N)  — K estrazioni, ciascuna O(N) per max() e remove()
# c) O(log N)  — dimezza la zona di ricerca a ogni passo
# d) O(N)      — deve copiare ogni elemento


# --- Soluzione Integrazione 2 ---
# def valida_k_min(L, k):
#     if not L:
#         raise ValueError("L è vuota")
#     if not (1 <= k <= len(L)):
#         raise ValueError(f"K={k} non valido")
#
# def k_min(L, k):
#     valida_k_min(L, k)
#     return sorted(L)[:k]


# --- Soluzione FUNC3 ---
# def top_k_giocatori(giocatori, k):
#     if not (1 <= k <= len(giocatori)):
#         raise ValueError(f"K={k} non valido")
#     ordinati = sorted(giocatori, key=lambda g: (-g['punteggio'], g['nome']))
#     return ordinati[:k]
