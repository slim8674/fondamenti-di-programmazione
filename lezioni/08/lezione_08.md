# Lezione 8

## Introduzione

Questa lezione parte da dove si era fermata la lezione 7 — il problema dei k-massimi — e lo usa come pretesto per introdurre due argomenti nuovi: la **complessità temporale** (notazione O) e la **ricerca binaria**.

Il filo conduttore è semplice: ogni volta che si riscrive una funzione in modo più furbo, ci si chiede quanto tempo impiega nel caso peggiore. Alla fine della lezione si ha una visione chiara del perché alcune soluzioni scalano meglio di altre, e si ha in mano un algoritmo nuovo — la ricerca binaria — che tornerà utile in molti contesti.

Questa lezione è più orientata alla comprensione che alla produzione di codice da esame. Fa eccezione la ricerca binaria, che può comparire come esercizio, e il pattern `sorted(L, reverse=True)[:k]`, che è già stato visto ma qui viene consolidato.

## raise e assert: validare l'input

Prima di affrontare i k-massimi, la lezione riprende due strumenti per segnalare errori.

### raise

Lancia un errore esplicitamente, con un messaggio utile:

```python
raise ValueError("K non può essere negativo")
raise TypeError("L deve essere una lista")
```

Questo errore viene sempre eseguito, indipendentemente da qualsiasi flag.

### assert

Sintassi compatta per controllare che una condizione sia vera:

```python
assert condizione, "messaggio se la condizione è falsa"
```

Esempio pratico:

```python
assert 0 < k <= len(L), f"K={k} non è compreso tra 1 e len(L)={len(L)}"
```

**Nota importante**: `assert` può essere disattivato avviando Python con il flag `-O`. Per questo motivo non va usato per controllare input che arrivano dall'esterno (utente, file). Per quei casi si usa `raise`. Nel corso e all'esame, il professore usa spesso `assert` per semplicità — va bene farlo.

## K-massimi: tre strategie a confronto

### Strategia 1 — Versione distruttiva (già vista in lezione 7)

Si estrae il massimo dalla lista `k` volte, rimuovendolo ogni volta:

```python
def estrai_massimo(L):
    assert L, "La lista è vuota"
    M = max(L)
    L.remove(M)
    return M

def k_massimi_distruttivo(L, k):
    assert len(L) > 0, "L è vuota"
    assert 0 < k <= len(L), f"K={k} non valido"
    return [estrai_massimo(L) for _ in range(k)]
```

Costo: per ogni estrazione si scansiona tutta la lista (`O(N)`), ripetuto `k` volte → **O(k × N)**.

### Strategia 2 — Con sorted (non distruttiva, più compatta)

```python
def k_massimi_sorted(L, k):
    assert 0 < k <= len(L)
    return sorted(L, reverse=True)[:k]
```

Costo: ordinare l'intera lista richiede **O(N log N)**. Prendere i primi `k` elementi è O(k), trascurabile. Il tempo totale è **O(N log N)**, indipendente da `k`.

Quando conviene? Quando `k` è grande, perché il costo non cresce con `k`.

### Strategia 3 — Low memory (streaming)

Invece di tenere tutta la lista in memoria, si scorre la sequenza una volta e si aggiorna una lista di soli `k` massimi correnti:

```python
def k_massimi_lowmem(K, L):
    massimi = []
    for X in L:
        update_massimi(massimi, K, X)
    return massimi
```

La funzione `update_massimi` gestisce tre casi:

1. se ho meno di `K` valori → aggiungo `X`
2. se `X` è minore o uguale al minimo dei massimi → ignoro
3. altrimenti → rimuovo il minimo e aggiungo `X`

Versione semplice (senza mantenere l'ordine):

```python
def update_massimi(massimi, k, X):
    if k > len(massimi):
        massimi.append(X)
        return
    minimo = min(massimi)         # O(K)
    if X <= minimo:
        return
    massimi.remove(minimo)        # O(K)
    massimi.append(X)
```

Costo: O(K) per ogni elemento → **O(N × K)** totale. Usa solo O(K) di memoria.

Versione migliorata: mantenere i `k` massimi ordinati permette di trovare e rimuovere il minimo in O(1) (è sempre in fondo):

```python
def update_massimi(massimi, K, X):
    massimi.append(X)
    massimi.sort(reverse=True)    # O(K log K)
    massimi[K:] = []              # elimina oltre posizione K
```

Costo per aggiornamento: **O(K log K)**. Ma l'inserimento fisico in una lista ordinata rimane O(K) anche con la ricerca binaria, perché spostare gli elementi costa comunque O(K).

La soluzione ottimale usa `SortedList` da `sortedcontainers`:

```python
from sortedcontainers import SortedList

def aggiorna_k_massimi_SC(massimi, X, k):
    if len(massimi) < k:
        massimi.add(X)            # O(log K)
    elif massimi[0] < X:
        del massimi[0]            # O(log K)
        massimi.add(X)            # O(log K)
```

Costo: **O(N log K)** — il migliore possibile per questo problema.

### Riepilogo costi

| Strategia                 | Tempo      | Memoria |
| ------------------------- | ---------- | ------- |
| Distruttiva (estrai max)  | O(K × N)   | O(N)    |
| sorted() + slicing        | O(N log N) | O(N)    |
| Low memory (non ordinata) | O(K × N)   | O(K)    |
| Low memory (SortedList)   | O(N log K) | O(K)    |

Quale scegliere? Dipende da `K` e `N`. Se `K` è molto piccolo rispetto a `log(N)`, la versione low memory con SortedList è nettamente migliore. Se `K` è grande, il sorted() diventa competitivo.

## Ricerca binaria

### Il problema

Cercare un elemento in una lista **ordinata**. La ricerca lineare scansiona tutto: O(N). Si può fare molto meglio.

### L'idea

A ogni passo si guarda l'elemento centrale. Se è quello cercato, trovato. Se il valore cercato è più piccolo, si cerca nella metà giusta. Se è più grande, nell'altra. A ogni passo si dimezza la zona di ricerca → **O(log N)**.

### Implementazione su lista ordinata decrescente

```python
def ricerca_binaria(Lista, Valore):
    inizio = 0
    fine = len(Lista) - 1
    while inizio <= fine:
        centrale = (inizio + fine) // 2
        valore_centrale = Lista[centrale]
        if Valore == valore_centrale:
            return centrale           # trovato
        elif Valore < valore_centrale:
            inizio = centrale + 1     # cerca a destra (lista decrescente)
        else:
            fine = centrale - 1       # cerca a sinistra
    return inizio                     # posizione di inserimento
```

**Attenzione**: su lista **decrescente** la logica si inverte rispetto alla versione classica su lista crescente. Se il valore cercato è minore del centrale, va cercato a destra (i valori piccoli stanno in fondo).

La funzione non solo trova un elemento, ma restituisce anche la **posizione in cui andrebbe inserito** se non trovato. Questo la rende utile per mantenere liste ordinate con inserimenti efficienti.

### In Python esiste già: bisect

Il modulo `bisect` della libreria standard implementa la ricerca binaria su liste ordinate crescenti. Per le liste decrescenti, l'implementazione manuale come sopra è più diretta.

## Notazione O — complessità temporale

### Cos'è

Descrive come cresce il tempo di esecuzione di una funzione al crescere della dimensione dell'input, nel caso peggiore. Si ignorano le costanti moltiplicative.

### Le classi principali

| Notazione  | Nome           | Cosa succede se N raddoppia        |
| ---------- | -------------- | ---------------------------------- |
| O(1)       | costante       | niente, il tempo non cambia        |
| O(log N)   | logaritmica    | aumenta di pochissimo              |
| O(N)       | lineare        | il tempo raddoppia                 |
| O(N log N) | pseudo-lineare | poco più del doppio                |
| O(N²)      | quadratica     | il tempo quadruplica               |
| O(2^N)     | esponenziale   | il tempo raddoppia per ogni +1 a N |

### Regole di semplificazione

- I fattori costanti si ignorano: `O(5 × N)` diventa `O(N)`.
- Somma: si prende il termine dominante: `O(N) + O(log N)` = `O(N)`.
- Prodotto: si moltiplicano: `O(N) × O(K)` = `O(N × K)`.

### Perché importa all'esame

La notazione O non viene chiesta direttamente all'esame scritto. Ma capirla aiuta a scegliere la strategia giusta quando la consegna dice "funzione efficiente" o quando si ragiona su quale approccio usare per un problema di ordinamento o ricerca.

## Errori tipici da evitare

### 1. Confondere assert e raise

`assert` per controlli interni durante sviluppo. `raise` per errori che devono sempre essere gestiti (input esterni, precondizioni critiche).

### 2. Ricerca binaria su lista non ordinata

La ricerca binaria funziona **solo** su liste ordinate. Applicarla a una lista casuale produce risultati errati senza errori espliciti.

### 3. Invertire la direzione nella ricerca binaria decrescente

Su lista decrescente, valori piccoli stanno a destra. Se X < centrale, si cerca a destra (inizio = centrale + 1), non a sinistra. È facile invertire per abitudine con la versione crescente.

### 4. L.copy() si dimentica nella versione non distruttiva

Se vuoi i k-massimi senza modificare la lista originale, devi copiare prima di passarla alla versione distruttiva. Dimenticarlo è un bug silenzioso.

### 5. sorted() con reverse=True non inverte le stringhe "al contrario"

`reverse=True` inverte l'intera lista, non il singolo campo. Se hai criteri misti (numeri decrescenti, stringhe crescenti), devi usare il trucco del segno meno sui numeri.

## Valutazione ai fini dell'esame

### Utilità complessiva: **media**

Questa lezione è più concettuale delle precedenti. Gli strumenti direttamente spendibili all'esame sono pochi ma importanti.

### Parti ad alta priorità

- `sorted(L, reverse=True)[:k]` — pattern consolidato, richiesto spesso nelle FUNC;
- `assert` e `raise` per validare input — buona pratica attesa nelle soluzioni;
- ricerca binaria — può comparire come esercizio nelle FUNC più avanzate.

### Parti utili ma di priorità media

- notazione O e analisi della complessità: utile per capire, raramente richiesta esplicitamente;
- `SortedList` da `sortedcontainers`: non è nella libreria standard, difficilmente richiesta all'esame scritto;
- versione low memory dei k-massimi: interessante concettualmente, ma il pattern `sorted()[:k]` è più pratico e quasi sempre sufficiente.

### Giudizio finale

Consolida il pattern `sorted(L, reverse=True)[:k]` e impara a riconoscere quando una funzione ha costo O(N²) vs O(N log N). Studia la ricerca binaria come algoritmo: il ragionamento "dimezza la zona di ricerca ad ogni passo" è un pattern che torna anche altrove (ricorsione su alberi, sottoinsiemi).

---

## Esercizi

Il file degli esercizi associati a questa lezione è `esercizi_08.py`.
