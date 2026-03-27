# Lezione 4

## Introduzione

In questa lezione riprendiamo il lavoro sui contenitori iniziato nella lezione precedente e approfondiamo alcuni aspetti molto importanti:

- iterazione tramite indice
- uso di `enumerate()`
- problemi causati dalla modifica di una lista durante un ciclo
- uso dei contenitori in contesti booleani
- introduzione agli oggetti e ai metodi
- principali operazioni su liste, tuple, insiemi e dizionari

Questa lezione è importante perché ci porta da un uso elementare dei contenitori a un uso più consapevole e più vicino alla pratica reale della programmazione in Python. La bozza originale insiste proprio su questi punti: scorrere correttamente i dati, capire quando un metodo modifica davvero una struttura dati e distinguere bene i comportamenti dei diversi contenitori. fileciteturn9file0

## Iterare un contenitore attraverso l'indice

Nelle lezioni precedenti abbiamo già visto che un contenitore può essere attraversato con un ciclo `for`. Un passo ulteriore consiste nel percorrere non direttamente gli elementi, ma i loro **indici**.

Esempio:

```python
lista_new = [2, 5, 7, 'fls']

for indice in range(len(lista_new)):
    elemento = lista_new[indice]
    print(indice, elemento)
```

Output:

```python
0 2
1 5
2 7
3 fls
```

Qui:

- `len(lista_new)` restituisce la lunghezza della lista;
- `range(len(lista_new))` genera gli indici validi della lista;
- `lista_new[indice]` permette di leggere l'elemento nella posizione corrente.

Questo approccio è utile quando non basta conoscere il valore di un elemento, ma serve anche sapere **in quale posizione si trova**.

## `enumerate()`

Un modo più comodo per ottenere contemporaneamente indice ed elemento è usare `enumerate()`.

```python
lista_new = [2, 5, 7, 'fls']
print(list(enumerate(lista_new)))
```

Output:

```python
[(0, 2), (1, 5), (2, 7), (3, 'fls')]
```

Nella bozza si dice che `enumerate` genera una lista di coppie indice-elemento. L'idea didattica è giusta, ma tecnicamente è meglio dire che `enumerate()` restituisce un **oggetto iterabile**; se vogliamo vedere tutte le coppie insieme, possiamo convertirlo con `list(...)`. fileciteturn9file0

Forma tipica d'uso:

```python
for indice, elemento in enumerate(lista_new):
    print(indice, elemento)
```

Questo è spesso preferibile a `range(len(...))` quando ci servono sia la posizione sia il valore, perché è più leggibile.

## Attenzione: modificare una lista durante l'iterazione

Uno dei punti più importanti della lezione riguarda il fatto che **non bisogna modificare con leggerezza una lista mentre la si sta scorrendo con un ciclo basato sugli indici**. La bozza fa notare due effetti distinti:

- il ciclo continua a fare riferimento alla lunghezza iniziale della lista;
- eliminando un elemento, gli indici successivi si spostano e alcuni valori possono essere saltati. fileciteturn9file0

Esempio:

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66, 77, 88]

for i in range(len(lista_interi)):
    print(lista_interi[i])
    if i == 3:
        del lista_interi[i]
        print('ho eliminato il 33 dalla lista e ho saltato il 44')
```

Output fino all'errore:

```python
0
11
22
33
ho eliminato il 33 dalla lista e ho saltato il 44
55
66
77
88
IndexError: list index out of range
```

### Perché succede

All'inizio il ciclo viene impostato su una lista di 9 elementi, quindi i valori di `i` andranno da `0` a `8`.

Quando eliminiamo `lista_interi[3]`, la lista diventa:

```python
[0, 11, 22, 44, 55, 66, 77, 88]
```

A questo punto:

- `44` si sposta all'indice `3`;
- però il ciclo passa all'indice `4`;
- quindi `44` viene saltato;
- alla fine il ciclo tenterà comunque di accedere a un indice che non esiste più nella lista accorciata.

### Strategie più sicure

Come suggerisce la bozza, due strategie corrette sono:

- scorrere la lista **al contrario**;
- costruire una **nuova lista** contenente solo gli elementi che vogliamo mantenere. fileciteturn9file0

Esempio con nuova lista:

```python
numeri = [0, 11, 22, 33, 44, 55]
nuova = []

for x in numeri:
    if x != 33:
        nuova.append(x)

print(nuova)
```

Output:

```python
[0, 11, 22, 44, 55]
```

## I contenitori come valori booleani

In Python i contenitori possono essere usati direttamente in un `if`.

Regola generale:

- un contenitore **vuoto** vale `False`;
- un contenitore **non vuoto** vale `True`.

Esempio:

```python
S = [20.3]

if S:
    print(S, 'contiene almeno un elemento')
else:
    print(S, 'non contiene elementi')
```

Questo è equivalente a scrivere:

```python
if len(S) > 0:
```

ma di solito è più naturale scrivere direttamente `if S:`.

### Attenzione a `{}` e `set()`

La bozza richiama giustamente un dettaglio importante: in Python `{}` rappresenta un **dizionario vuoto**, non un insieme vuoto. Per creare un insieme vuoto dobbiamo usare `set()`. fileciteturn9file0

Esempi:

```python
print(bool({}))
print(bool(set()))
```

Output:

```python
False
False
```

Entrambi sono vuoti, ma il primo è un dizionario e il secondo è un insieme.

## Oggetti e metodi

Nella bozza compare poi una prima introduzione al concetto di **oggetto**. In Python un oggetto è un'entità che contiene dati e mette a disposizione certe operazioni. Queste operazioni si chiamano **metodi**. fileciteturn9file0

Forma generale:

```python
oggetto.nome_metodo(argomenti)
```

Questa sintassi indica che il metodo è legato a quel particolare oggetto.

### Esempi con stringhe e contenitori

Per spezzare una stringa in caratteri possiamo usare `list()` oppure `set()`:

```python
print(list('ifjbwie'))
print(set('sdfvigub'))
```

Output possibile:

```python
['i', 'f', 'j', 'b', 'w', 'i', 'e']
{'g', 'f', 'u', 'v', 'i', 'b', 'd', 's'}
```

Con `list()` manteniamo l'ordine e i duplicati. Con `set()` invece:

- l'ordine non è garantito;
- gli eventuali duplicati vengono eliminati.

Altro esempio:

```python
S = 'Prova Dimostrativa'
print(S.islower())
```

Output:

```python
False
```

Il metodo `islower()` controlla se tutti i caratteri alfabetici della stringa sono minuscoli.

Esempio con `find()`:

```python
S = 'Prova Dimostrativa'
print(S.find('Prova'), S.find('gnomo'))
```

Output:

```python
0 -1
```

Quindi:

- `0` è la posizione iniziale della sottostringa `'Prova'`;
- `-1` indica che `'gnomo'` non compare nella stringa.

## Metodi dei contenitori

Dopo l'introduzione ai metodi, la bozza elenca le principali operazioni sui contenitori fondamentali di Python. Le raccogliamo qui in modo più ordinato e con spiegazioni essenziali. fileciteturn9file4turn9file5

---

## Operazioni sulle liste (`list`)

Le liste sono contenitori:

- ordinati;
- modificabili;
- in grado di contenere anche elementi di tipo diverso.

### Operazioni fondamentali

```python
L[indice]              # lettura dell'elemento all'indice
L[indice] = espressione
elemento in L
L1 + L2
L1 * n
```

Significato:

- `L[indice]` legge il valore nella posizione indicata;
- `L[indice] = espressione` sostituisce il valore in quella posizione;
- `elemento in L` verifica la presenza di un elemento;
- `L1 + L2` crea una nuova lista concatenando due liste;
- `L1 * n` crea una nuova lista ripetendo più volte la lista iniziale.

### `append()`

```python
L = [1, 2, 3]
L.append(4)
print(L)
```

Output:

```python
[1, 2, 3, 4]
```

Aggiunge un elemento **alla fine** della lista.

### `pop()`

```python
L = [1, 2, 3, 4, 5]
print(L.pop(2))
print(L)
```

Output:

```python
3
[1, 2, 4, 5]
```

`pop(indice)`:

- rimuove l'elemento nella posizione indicata;
- restituisce il valore rimosso.

Se non si specifica l'indice:

```python
L.pop()
```

viene rimosso e restituito l'ultimo elemento.

### `insert()`

```python
L = [1, 2, 4, 5]

L.insert(2, 4)
print(L)

L.insert(30, 44)
print(L)

L.insert(-30, 444)
print(L)
```

Output:

```python
[1, 2, 4, 4, 5]
[1, 2, 4, 4, 5, 44]
[444, 1, 2, 4, 4, 5, 44]
```

Quindi:

- se l'indice è valido, l'elemento viene inserito in quella posizione;
- se l'indice è troppo grande, viene inserito in fondo;
- se l'indice negativo è troppo piccolo, viene inserito all'inizio.

### Assegnamento tramite slice

Nella bozza si osserva che questo meccanismo è definito sulle liste. In effetti possiamo sostituire una porzione della lista con un altro contenitore compatibile. fileciteturn9file4

Forma generale:

```python
lista[inizio:fine] = contenitore
lista[inizio:fine:incremento] = contenitore
```

Esempio:

```python
XXX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
XXX[2:8:1] = list('abcdef')
print(XXX)
```

Output:

```python
[1, 2, 'a', 'b', 'c', 'd', 'e', 'f', 9, 10]
```

Questo permette anche di eliminare una porzione della lista:

```python
L = [10, 20, 30, 40, 50]
L[1:4] = []
print(L)
```

Output:

```python
[10, 50]
```

### Altri metodi utili delle liste

```python
L.pop()
L.remove(elemento)
L.index(elemento)
L.count(elemento)
L.reverse()
L.sort()
```

Significato:

- `L.pop()` rimuove e restituisce l'ultimo elemento;
- `L.remove(elemento)` rimuove il primo elemento uguale al valore dato;
- `L.index(elemento)` trova il primo indice in cui compare l'elemento;
- `L.count(elemento)` conta quante volte compare;
- `L.reverse()` inverte l'ordine della lista;
- `L.sort()` ordina direttamente la lista.

### Metodi distruttivi

La bozza usa spesso il termine **distruttivo**. In questo contesto significa che il metodo **modifica direttamente la struttura dati originale**. fileciteturn9file4

Esempio:

```python
L = [4, 1, 3, 2]
L.sort()
print(L)
```

Output:

```python
[1, 2, 3, 4]
```

La lista originale è stata cambiata.

---

## Operazioni sulle tuple (`tuple`)

Le tuple sono contenitori:

- ordinati;
- non modificabili.

Operazioni principali:

```python
T[1]
elemento in T
T1 + T2
T * N
T.index(elemento)
T.count(elemento)
```

Significato:

- `T[1]` legge l'elemento nella posizione indicata;
- `elemento in T` controlla la presenza;
- `T1 + T2` crea una nuova tupla concatenata;
- `T * N` crea una nuova tupla con ripetizione;
- `T.index(elemento)` restituisce la posizione del primo elemento uguale;
- `T.count(elemento)` conta quante volte compare.

Esempio:

```python
T = (10, 20, 10, 30)
print(T.index(20))
print(T.count(10))
```

Output:

```python
1
2
```

### Importante: le tuple sono immutabili

Nella bozza è ricordato correttamente che assegnare un nuovo valore in una tupla dà errore. fileciteturn9file4

```python
T = (1, 2, 3)
T[1] = 99
```

Questo produce un errore, perché una tupla non può essere modificata.

Anche lo slicing su una tupla non consente modifiche: restituisce una nuova tupla o una porzione leggibile, ma non assegnabile.

---

## Operazioni sugli insiemi (`set`)

Gli insiemi sono contenitori:

- modificabili;
- non ordinati;
- senza duplicati.

La bozza insiste giustamente sul fatto che negli insiemi non esistono né ordine né doppioni. fileciteturn9file5

### Operazioni insiemistiche

```python
elemento in S
S1 | S2
S1 & S2
S1 - S2
S1 ^ S2
```

Significato:

- `elemento in S` verifica la presenza;
- `S1 | S2` oppure `S1.union(S2)` calcola l'unione;
- `S1 & S2` oppure `S1.intersection(S2)` calcola l'intersezione;
- `S1 - S2` oppure `S1.difference(S2)` prende gli elementi di `S1` non presenti in `S2`;
- `S1 ^ S2` oppure `S1.symmetric_difference(S2)` prende gli elementi non in comune.

Esistono anche gli assegnamenti potenziati:

```python
|=   &=   -=   ^=
```

### Metodi principali degli insiemi

```python
S.pop()
S.add(elemento)
S.remove(elemento)
S1.update(S2)
```

Significato:

- `S.pop()` rimuove e restituisce un elemento arbitrario dell'insieme;
- `S.add(elemento)` aggiunge un elemento;
- `S.remove(elemento)` rimuove un elemento e genera errore se non esiste;
- `S1.update(S2)` modifica `S1` aggiungendo gli elementi di `S2`.

La bozza parla di elemento “a caso” per `pop()`: didatticamente l'idea è chiara, ma la formulazione tecnica migliore è “elemento arbitrario”, perché in un insieme non esiste un ordine da rispettare. fileciteturn9file5

Esempio:

```python
S1 = {1, 2, 3}
S2 = {3, 4, 5}

print(S1 | S2)
print(S1 & S2)
print(S1 - S2)
print(S1 ^ S2)
```

Output possibile:

```python
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}
```

---

## Operazioni sui dizionari (`dict`)

I dizionari associano **chiavi** a **valori**. Come osserva la bozza, si comportano in parte come le liste, ma al posto dell'indice numerico si usano le chiavi. fileciteturn9file5

### Operazioni fondamentali

```python
key in D
D[key]
D.keys()
D.values()
D.items()
D.popitem()
D1 | D2
D1.update(D2)
```

Significato:

- `key in D` verifica se la chiave è presente;
- `D[key]` restituisce il valore associato alla chiave;
- `D.keys()` restituisce una vista iterabile delle chiavi;
- `D.values()` restituisce una vista iterabile dei valori;
- `D.items()` restituisce una vista iterabile delle coppie `(chiave, valore)`;
- `D.popitem()` rimuove e restituisce l'ultima coppia inserita;
- `D1 | D2` crea un nuovo dizionario combinando le coppie dei due dizionari;
- `D1.update(D2)` modifica `D1` aggiungendo o aggiornando le coppie di `D2`.

Nella bozza `keys()`, `values()` e `items()` sono descritti come generatori o elenchi. Per essere più precisi, oggi è meglio parlarne come **viste** del dizionario: si possono iterare e usare molto comodamente nei cicli. fileciteturn9file5

### Metodi utili

```python
D.get(key, default)
D.setdefault(key, default)
D.pop(key, default)
D.fromkeys(keys, value)
```

#### `get()`

```python
D = {'a': 10, 'b': 20}
print(D.get('a', 0))
print(D.get('z', 0))
```

Output:

```python
10
0
```

Se la chiave esiste, restituisce il valore associato. Altrimenti restituisce il valore di default.

#### `setdefault()`

```python
D = {'a': 10}
print(D.setdefault('a', 99))
print(D.setdefault('b', 99))
print(D)
```

Output:

```python
10
99
{'a': 10, 'b': 99}
```

Se la chiave esiste, restituisce il valore già presente. Se non esiste, la inserisce con il valore di default.

#### `pop()`

```python
D = {'x': 1, 'y': 2}
print(D.pop('x', 0))
print(D.pop('z', 0))
print(D)
```

Output:

```python
1
0
{'y': 2}
```

#### `fromkeys()`

```python
chiavi = ['nome', 'cognome', 'eta']
D = dict.fromkeys(chiavi, None)
print(D)
```

Output:

```python
{'nome': None, 'cognome': None, 'eta': None}
```

Crea un nuovo dizionario con le chiavi indicate, tutte inizialmente associate allo stesso valore.

## Riepilogo

In questa lezione abbiamo visto che:

- possiamo iterare un contenitore anche tramite indice;
- `enumerate()` è un modo molto comodo per ottenere insieme indice ed elemento;
- modificare una lista durante l'iterazione può causare salti di elementi ed errori;
- i contenitori vuoti valgono `False`, quelli non vuoti valgono `True`;
- gli oggetti espongono metodi, che si invocano con la sintassi `oggetto.metodo(...)`;
- liste, tuple, insiemi e dizionari hanno operazioni proprie che bisogna distinguere bene.

Questo materiale prepara al lavoro pratico sugli esercizi, dove i contenitori non vengono più trattati solo come esempi teorici, ma come veri strumenti per costruire piccoli programmi. fileciteturn9file0turn9file1
