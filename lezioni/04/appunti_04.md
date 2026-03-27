# Lezione 4

## Introduzione

In questa lezione approfondiamo alcuni aspetti molto importanti del lavoro con i contenitori e con gli oggetti in Python:

- iterazione tramite indice
- uso di `len()` e `range()` insieme
- funzione `enumerate()`
- modifica di una lista durante un ciclo
- verità e falsità dei contenitori
- oggetti e metodi
- distinzione tra funzioni generali e metodi degli oggetti

Questi concetti servono a scrivere codice più corretto e più leggibile. In particolare, aiutano a capire meglio come scorrere i dati, come evitare errori frequenti e come usare correttamente le operazioni messe a disposizione dai vari tipi di oggetto.

## Iterare su un contenitore

Nelle lezioni precedenti abbiamo visto che un contenitore può essere percorso con un ciclo `for`.

Esempio:

```python
lista_new = [2, 5, 7, 'fls']

for elemento in lista_new:
    print(elemento)
```

Output:

```python
2
5
7
fls
```

Questo approccio è molto comodo quando interessa il valore degli elementi.

## Iterare tramite indice

A volte però non basta conoscere il valore dell’elemento: può essere utile conoscere anche la sua posizione.

In quel caso possiamo generare gli indici con `range(len(contenitore))`.

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

Qui succedono due cose:

- `len(lista_new)` restituisce il numero di elementi della lista
- `range(len(lista_new))` genera gli indici validi: `0`, `1`, `2`, `3`

Questo schema è utile quando:

- serve leggere la posizione di un elemento
- serve accedere a più contenitori in parallelo tramite lo stesso indice
- serve modificare elementi in una certa posizione

## Quando usare l’indice e quando no

In generale:

- se ti serve solo il valore, è meglio scrivere `for elemento in contenitore`
- se ti servono posizione e valore, puoi usare `enumerate()`
- se devi lavorare proprio con le posizioni numeriche, puoi usare `range(len(...))`

Usare l’indice senza necessità rende spesso il codice meno leggibile.

## La funzione `enumerate()`

Python offre una funzione molto comoda per ottenere insieme indice ed elemento: `enumerate()`.

Esempio:

```python
lista_new = [2, 5, 7, 'fls']

for indice, elemento in enumerate(lista_new):
    print(indice, elemento)
```

Output:

```python
0 2
1 5
2 7
3 fls
```

Possiamo anche osservare il risultato trasformandolo in lista:

```python
lista_new = [2, 5, 7, 'fls']
print(list(enumerate(lista_new)))
```

Output:

```python
[(0, 2), (1, 5), (2, 7), (3, 'fls')]
```

Questa funzione produce coppie della forma:

```python
(indice, elemento)
```

Per questo `enumerate()` è spesso preferibile a `range(len(...))` quando vogliamo sia la posizione sia il valore corrente.

## Esempio di confronto tra due stili

### Stile con indice

```python
nomi = ['Anna', 'Luca', 'Marco']

for i in range(len(nomi)):
    print(i, nomi[i])
```

### Stile con `enumerate()`

```python
nomi = ['Anna', 'Luca', 'Marco']

for i, nome in enumerate(nomi):
    print(i, nome)
```

I due codici producono lo stesso effetto, ma il secondo è spesso più chiaro.

## Modificare una lista durante un ciclo

Un errore molto frequente consiste nel modificare una lista mentre la si sta scorrendo.

Esempio problematico:

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66, 77, 88]

for i in range(len(lista_interi)):
    print(lista_interi[i])
    if i == 3:
        del lista_interi[i]
        print('ho eliminato il 33 dalla lista e ho saltato il 44')
```

Questo codice è pericoloso perché:

- `range(len(lista_interi))` è stato costruito usando la lunghezza iniziale della lista
- dopo `del lista_interi[i]` la lista diventa più corta
- gli indici successivi cambiano
- l’ultimo indice prodotto dal ciclo può non essere più valido

Il risultato tipico è un errore del tipo:

```python
IndexError: list index out of range
```

Inoltre, eliminando un elemento, gli elementi successivi scorrono verso sinistra e si rischia di saltarne qualcuno.

## Perché si salta un elemento

Supponiamo di partire da:

```python
[0, 11, 22, 33, 44, 55]
```

Se eliminiamo `33`, la lista diventa:

```python
[0, 11, 22, 44, 55]
```

L’elemento `44` prende il posto che prima era di `33`.
Se il ciclo passa subito all’indice successivo, `44` può non essere elaborato nel modo previsto.

## Strategie più sicure

Quando bisogna eliminare elementi durante una scansione, conviene usare strategie più sicure.

### 1. Creare una nuova lista

È spesso la soluzione più semplice e leggibile.

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66]
nuova_lista = []

for elemento in lista_interi:
    if elemento != 33:
        nuova_lista.append(elemento)

print(nuova_lista)
```

Output:

```python
[0, 11, 22, 44, 55, 66]
```

### 2. Iterare al contrario

Se si elimina per indice, può essere utile scorrere la lista dalla fine verso l’inizio.

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66]

for i in range(len(lista_interi) - 1, -1, -1):
    if lista_interi[i] == 33:
        del lista_interi[i]

print(lista_interi)
```

Output:

```python
[0, 11, 22, 44, 55, 66]
```

Questo approccio è più sicuro perché eliminando un elemento in una posizione avanzata non si altera la parte ancora da visitare a sinistra.

### 3. Usare una list comprehension

Più avanti vedremo meglio questo strumento, ma già ora si può osservare questa forma:

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66]
lista_filtrata = [x for x in lista_interi if x != 33]
print(lista_filtrata)
```

## Contenitori vuoti e valori booleani

In Python molti valori possono essere interpretati come `True` o `False`.

Per i contenitori vale una regola molto importante:

- un contenitore vuoto è considerato `False`
- un contenitore non vuoto è considerato `True`

Esempi:

```python
print(bool([]))
print(bool([1, 2]))
print(bool(()))
print(bool((3, 4)))
print(bool({}))
print(bool({'a': 1}))
print(bool(set()))
print(bool({1, 2}))
```

Output:

```python
False
True
False
True
False
True
False
True
```

## Attenzione a `{}` e `set()`

Bisogna ricordare un dettaglio importante:

```python
{}
```

in Python rappresenta un **dizionario vuoto**, non un insieme vuoto.

Per creare un insieme vuoto bisogna scrivere:

```python
set()
```

Quindi:

```python
bool({})
```

controlla un dizionario vuoto, mentre:

```python
bool(set())
```

controlla un insieme vuoto.

## Controllare se un contenitore è vuoto

È possibile controllare se un contenitore contiene almeno un elemento in due modi.

### Forma esplicita con `len()`

```python
S = [20.3]

if len(S) > 0:
    print(S, 'contiene almeno un elemento')
else:
    print(S, 'non contiene elementi')
```

### Forma più pythonica

```python
S = [20.3]

if S:
    print(S, 'contiene almeno un elemento')
else:
    print(S, 'non contiene elementi')
```

La seconda forma è generalmente preferita perché più breve e più naturale in Python.

## Esempi con contenitori diversi

```python
parole = []
if parole:
    print('la lista non è vuota')
else:
    print('la lista è vuota')
```

```python
dati = {}
if dati:
    print('il dizionario contiene almeno una coppia chiave-valore')
else:
    print('il dizionario è vuoto')
```

```python
insieme = set()
if not insieme:
    print('l\'insieme è vuoto')
```

## Oggetti in Python

In Python tutto è basato su oggetti.

Un **oggetto** può essere visto come un’entità che possiede:

- dati
- comportamento

Per esempio:

- una stringa è un oggetto
- una lista è un oggetto
- un numero è un oggetto
- un dizionario è un oggetto

Ogni oggetto appartiene a un certo tipo e mette a disposizione certe operazioni.

## Metodi degli oggetti

Le operazioni specifiche associate a un oggetto si chiamano **metodi**.

La sintassi generale è:

```python
oggetto.nome_del_metodo(argomenti)
```

Esempi:

```python
parola = 'ciao'
print(parola.upper())
```

```python
numeri = [10, 20]
numeri.append(30)
print(numeri)
```

```python
dati = {'nome': 'Luca'}
print(dati.keys())
```

In tutti questi casi il metodo dipende dal tipo dell’oggetto.

## Funzioni e metodi

È importante distinguere tra:

- **funzioni generali**, scritte come `nome_funzione(argomenti)`
- **metodi**, scritti come `oggetto.metodo(argomenti)`

Esempi di funzioni:

```python
len('ciao')
type([1, 2, 3])
print('salve')
```

Esempi di metodi:

```python
'ciao'.upper()
'ciao'.find('a')
[1, 2].append(3)
```

### Differenza concettuale

Una funzione è chiamata dall’esterno e riceve l’oggetto come argomento.
Un metodo, invece, è un’operazione messa a disposizione direttamente da quel tipo di oggetto.

Per esempio:

```python
testo = 'Oggi sono Un po StaNco'
print(testo.lower())
```

Qui `lower()` è un metodo delle stringhe, quindi si richiama sull’oggetto stringa stesso.

## Alcuni metodi comuni

### Metodi delle stringhe

```python
testo = 'Ciao Mondo'
print(testo.lower())
print(testo.upper())
print(testo.find('M'))
print(testo.split())
```

### Metodi delle liste

```python
numeri = [1, 2, 3]
numeri.append(4)
print(numeri)

numeri.remove(2)
print(numeri)
```

### Metodi dei dizionari

```python
persona = {'nome': 'Anna', 'eta': 21}
print(persona.keys())
print(persona.values())
print(persona.items())
```

### Metodi degli insiemi

```python
insieme = {1, 2}
insieme.add(3)
print(insieme)
```

## Osservazioni finali

In questa lezione abbiamo consolidato alcune idee molto utili per programmare meglio:

- un contenitore può essere percorso direttamente oppure tramite indice
- `enumerate()` è spesso il modo più comodo per ottenere posizione ed elemento insieme
- modificare una lista mentre la si sta scorrendo può produrre errori o comportamenti inattesi
- i contenitori vuoti valgono `False`, quelli non vuoti valgono `True`
- `{}` è un dizionario vuoto, mentre un insieme vuoto si scrive `set()`
- in Python gli oggetti mettono a disposizione metodi specifici
- una funzione e un metodo non si richiamano con la stessa sintassi

## Sintesi

Questa lezione rafforza il modo in cui leggiamo e manipoliamo i dati in Python:

- accesso con indice e scansione controllata
- uso corretto di `enumerate()`
- attenzione alle modifiche in-place durante i cicli
- uso dei contenitori come valori booleani
- comprensione del modello a oggetti e dei metodi

Sono concetti fondamentali, perché ricompaiono continuamente in esercizi, programmi reali e librerie del linguaggio.
