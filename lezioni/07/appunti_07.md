# Lezione 7

## Introduzione

Questa lezione consolida e approfondisce tre argomenti che si intrecciano spesso negli esercizi d'esame:

- funzioni lambda e criteri di ordinamento complessi;
- list comprehension e le sue varianti;
- metodologia di analisi top-down dei problemi, con il caso concreto dei k-massimi.

Non è una lezione di nuova sintassi da zero: molti pezzi erano già presenti. Quello che cambia è la capacità di combinarli in modo più efficiente. In particolare, la list comprehension è uno strumento che compare quasi sempre negli esercizi delle prime FUNC all'esame, e la padronanza dei criteri di ordinamento è richiesta esplicitamente nelle FUNC più pesanti.

## Funzioni lambda: funzioni usa e getta

Quando si usa `sorted()` con `key=`, serve una funzione che trasformi ogni elemento in qualcosa di confrontabile. Spesso questa funzione è banale: riceve un argomento, restituisce un'espressione. Non ha senso darle un nome e definirla in cima al file.

Python permette di definire queste funzioni direttamente nel punto in cui servono, con la sintassi **lambda**.

### Sintassi

```python
lambda argomenti: espressione
```

Se l'espressione è una tupla, conviene aggiungere le parentesi per chiarezza:

```python
lambda argomenti: (espressione_1, espressione_2)
```

### Equivalenza tra lambda e funzione normale

Le due scritture sono equivalenti:

```python
# versione con def
def criterio(elemento):
    return (len(elemento), elemento.lower(), elemento)

# versione lambda
criterio = lambda elemento: (len(elemento), elemento.lower(), elemento)
```

### Quando usare lambda e quando usare def

La lambda va bene quando la logica è semplice e usata una volta sola. Se il criterio diventa complesso, o vuoi riutilizzarlo, è meglio una funzione con `def`: è più leggibile, più facile da debuggare e più facile da testare.

Il professore consiglia esplicitamente di preferire `def` con spacchettamento quando gli elementi sono tuple o strutture composite:

```python
def trasforma(terna):
    eta, genere, nome = terna       # spacchetto la terna
    return len(nome), genere, eta   # costruisco il criterio
```

Questo stile è più chiaro di una lambda lunga su una riga.

## Ordinamenti contrapposti

Un problema frequente è ordinare per due criteri che vanno in **direzioni opposte**, ad esempio:

- lunghezza crescente;
- a parità di lunghezza, ordine alfabetico **decrescente** (Z → A).

Il problema è che `sorted()` confronta le tuple in modo uniforme: non puoi dire "questo campo crescente, quell'altro decrescente" passando solo `reverse=True`.

### Soluzione: rovesciare il segno dei numeri

Per i campi numerici si risolve semplicemente invertendo il segno:

```python
sorted(lista, key=lambda el: (-len(el), el), reverse=True)
```

Cambiare segno a un numero inverte il suo ordine naturale. Una parola di 6 caratteri diventa `-6`, che è più piccola di `-4`: quindi viene prima quando si ordina in modo crescente.

### Perché non si può fare lo stesso con le stringhe

Non esiste un modo diretto per "negare" una stringa. Con le stringhe non puoi usare il segno meno. L'unica alternativa è applicare `reverse=True` al campo stringa e rovesciare il campo numerico, oppure usare strutture dati più elaborate.

Nella pratica d'esame, la soluzione più frequente è: **rovescia il campo numerico con il segno meno, lascia le stringhe com'è**.

### Esempio completo con tuple

```python
L = [(27, 'M', 'Paperino'), (31, 'M', 'Topolino'),
     (26, 'F', 'Paperina'), (32, 'F', 'Minnie')]

# ordine: lunghezza nome crescente, genere crescente, età crescente
def trasforma(terna):
    eta, genere, nome = terna
    return len(nome), genere, eta

sorted(L, key=trasforma)
# [(32, 'F', 'Minnie'), (26, 'F', 'Paperina'),
#  (27, 'M', 'Paperino'), (31, 'M', 'Topolino')]
```

### La stessa logica funziona con min e max

La funzione `key=` non vale solo per `sorted()`. Si può usare anche con `min()` e `max()`:

```python
print(min(L, key=trasforma))  # il "più piccolo" secondo il criterio
print(max(L, key=trasforma))  # il "più grande" secondo il criterio
```

Questo è utile quando non vuoi ordinare tutta la lista ma solo estrarne un estremo.

## List comprehension

### Il problema che risolve

Capita spesso di dover costruire una lista trasformando ogni elemento di un'altra lista:

```python
def cubi(numeri):
    risultato = []
    for x in numeri:
        risultato.append(x**3)
    return risultato
```

Questo schema — lista vuota, ciclo, append, return — è così ricorrente che Python offre una sintassi compatta per scriverlo in una riga.

### Sintassi base

```python
[espressione for variabile in contenitore]
```

Esempio:

```python
lista_di_cubi = [x**3 for x in lista_di_interi]
```

Le parentesi determinano il tipo di contenitore prodotto:

```python
[x**3 for x in lista]         # lista
{x**3 for x in lista}         # insieme (set), senza duplicati
{x: x**3 for x in lista}      # dizionario chiave:valore
tuple(x**3 for x in lista)    # tupla (serve la parola tuple, non bastano le parentesi)
```

### Filtro con if

È possibile includere solo gli elementi che soddisfano una condizione:

```python
[espressione for variabile in contenitore if condizione]
```

Esempio — cubi solo dei numeri dispari:

```python
[x**3 for x in lista if x % 2 != 0]
```

### For nidificati

Si possono usare più `for` nella stessa comprehension:

```python
[espressione for var1 in contenitore1 for var2 in contenitore2]
```

Esempio — tutti i prodotti della tabellina del 10 come insieme:

```python
{x * y for x in range(1, 11) for y in range(1, 11)}
```

Il consiglio del professore è di limitarsi a due `for` nidificati per mantenere la leggibilità.

### Contenitori nidificati

Si possono anche costruire liste di liste:

```python
[[x * y for x in range(1, 11)] for y in range(1, 11)]
```

Il risultato è una matrice 10×10 con i prodotti della tabellina.

### Quando usarla e quando evitarla

La list comprehension è uno strumento, non un obbligo. Va bene per trasformazioni semplici. Se la logica diventa complessa — più condizioni, effetti collaterali, funzioni annidate — è meglio tornare al ciclo esplicito: è più leggibile e più facile da debuggare. All'esame, un ciclo `for` corretto vale quanto una comprehension corretta.

## Metodologia top-down: come analizzare un problema

### L'approccio generale

Prima di scrivere una riga di codice, il professore suggerisce di chiedersi:

- quali sono gli **input** e gli **output**?
- ci sono **condizioni di validità** sui dati?
- quali **errori** bisogna gestire?
- ci sono **effetti collaterali**? la funzione modifica distruttivamente l'input?
- ci sono **scelte non specificate** nella consegna?

Poi si divide il problema in sottoproblemi, ognuno implementato in una funzione separata, testata man mano.

### Leggere la consegna

Un trucco pratico: i nomi sono input o output, i verbi sono calcoli da fare. Esempio:

> _calcola la media di un elenco di altezze_

- "elenco di altezze" → input
- "media" → output
- "calcola la media" → operazione da svolgere

### Importanza del debug rapido

All'esame il tempo è limitato. Testare le sottofunzioni man mano permette di individuare gli errori subito, prima che si propaghino. Una funzione piccola e sbagliata è molto più facile da correggere di una funzione grande e sbagliata.

## Caso pratico: k-massimi

### Analisi del problema

> _trovare i k massimi di una lista L di valori numerici_

Applicando la metodologia:

- input: lista `L` di numeri, intero `k`
- output: lista dei `k` valori più grandi
- condizioni di validità: `k` deve essere positivo e non superiore a `len(L)`; la lista non deve essere vuota
- scelte: la lista risultante deve essere ordinata? si modifica distruttivamente `L`?

### Lanciare errori

Per segnalare condizioni non valide si usa `raise`:

```python
raise ValueError("messaggio esplicativo")
```

Oppure si usa `assert`, che è più compatto ma può essere disattivato:

```python
assert condizione, "messaggio se falsa"
```

**Nota importante**: `assert` non va usato per controllare input esterni (utente, file), perché può essere disattivato a runtime. Per quei casi si usa `raise`.

### Versione distruttiva

La strategia: ripetere `k` volte l'operazione di estrarre il massimo dalla lista.

```python
def estrai_massimo(L):
    assert L, "La lista è vuota"
    M = max(L)
    L.remove(M)
    return M

def k_massimi_distruttivo(L, k):
    assert len(L) > 0, "L è vuota"
    assert 0 < k <= len(L), f"K={k} non valido"
    risultato = []
    for _ in range(k):
        M = estrai_massimo(L)
        risultato.append(M)
    return risultato
```

La versione con list comprehension è equivalente:

```python
return [estrai_massimo(L) for _ in range(k)]
```

### Versione non distruttiva

Se non vogliamo modificare `L`, basta lavorare su una copia:

```python
def k_massimi(L, k):
    L1 = L.copy()
    return k_massimi_distruttivo(L1, k)
```

### Costo computazionale

Nel caso peggiore, con `N = len(L)`:

- per `k` volte si scandisce tutta la lista per trovare il massimo: tempo proporzionale a `N`
- poi si rimuove l'elemento trovato: tempo proporzionale a `N`

Il costo totale è proporzionale a `k × N`. All'aumentare di `k`, il tempo cresce linearmente, come si vede dai grafici della lezione.

### Alternativa con sorted

Una soluzione più compatta, vista anche nelle lezioni precedenti:

```python
def k_massimi_veloce(L, k):
    return sorted(L, reverse=True)[:k]
```

Non è distruttiva e ha costo proporzionale a `N log N` per il sorting, indipendentemente da `k`. Per `k` piccolo rispetto a `N`, la versione iterativa può essere più veloce; per `k` grande, il sorting è spesso più conveniente.

## Errori tipici da evitare

### 1. Lambda troppo complessa

Se una lambda supera un criterio o due, smette di essere leggibile. Meglio una funzione con `def`.

### 2. List comprehension con effetti collaterali

La comprehension è pensata per costruire contenitori, non per eseguire azioni. Usarla per chiamare funzioni con effetti collaterali è possibile ma sconsigliato.

### 3. Dimenticare le parentesi della tupla nella lambda

```python
# SBAGLIATO
sorted(lista, key=lambda el: -len(el), el)  # errore di sintassi

# CORRETTO
sorted(lista, key=lambda el: (-len(el), el))
```

### 4. Confondere assert e raise

`assert` è per controlli interni durante lo sviluppo. `raise` è per gestire condizioni di errore reali che devono essere sempre controllate.

## Valutazione ai fini dell'esame

### Utilità complessiva: **alta**

Questa lezione copre strumenti che compaiono quasi in ogni esame.

### Parti ad altissima priorità

- list comprehension con filtro: è la forma più comune nelle FUNC1–3;
- ordinamento con criteri multipli e contrapposti: richiesto esplicitamente nelle FUNC più pesanti;
- k-massimi come esempio di top-down: il pattern "estrai il massimo, rimuovilo, ripeti" compare spesso nelle varianti di esercizio.

### Parti utili ma di priorità media

- for nidificati nella comprehension: utili, ma raramente indispensabili;
- analisi del costo computazionale: utile per capire, non richiesta all'esame scritto;
- `raise` vs `assert`: da conoscere, ma la distinzione precisa non è mai stata centrale negli esercizi visti finora.

### Giudizio finale

Se devi scegliere cosa padroneggiare bene, concentrati su due cose: **list comprehension con condizione** e **ordinamento con criteri multipli contrapposti**. Sono gli strumenti più richiesti nelle prime funzioni dell'esame, quelle che valgono i punti più facili da conquistare. Il resto supporta la comprensione ma non è strettamente indispensabile per superare la soglia del 18.

---

## Esercizi

Il file degli esercizi associati a questa lezione è `esercizi_07.py`.
