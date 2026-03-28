# Lezione 4

## Introduzione

Nelle lezioni precedenti abbiamo visto come lavorare con stringhe, condizioni, cicli e contenitori principali di Python. In questa lezione facciamo un passo avanti: non ci limitiamo più a scorrere i dati, ma iniziamo a manipolarli in modo più consapevole.

L'obiettivo è duplice. Da un lato impariamo a visitare un contenitore conoscendo non solo il valore degli elementi, ma anche la loro posizione. Dall'altro iniziamo a usare in modo sistematico i **metodi** messi a disposizione dai diversi tipi di dato, soprattutto liste, tuple, insiemi e dizionari.

Questa lezione è importante perché segna il passaggio da un uso “elementare” dei contenitori a un uso più maturo: non ci interessa più soltanto memorizzare dati, ma anche scegliere l'operazione giusta in base al tipo di struttura che abbiamo davanti.

## Scorrere un contenitore tramite indice

Finora abbiamo spesso usato un ciclo `for` per leggere gli elementi di una sequenza uno dopo l'altro. In molti casi questo basta. A volte, però, serve anche sapere **in quale posizione** si trova ciascun elemento.

In queste situazioni possiamo usare gli indici con `range(len(...))`.

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

Qui sta succedendo questo:

- `len(lista_new)` restituisce la lunghezza della lista;
- `range(len(lista_new))` produce gli indici validi della lista;
- `lista_new[indice]` permette di accedere all'elemento in quella posizione.

Questo approccio è utile quando dobbiamo lavorare contemporaneamente con **posizione** e **valore**.

## `enumerate()`

In Python esiste una soluzione più comoda e leggibile per ottenere indice ed elemento insieme: `enumerate()`.

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

Il vantaggio di `enumerate()` è che evita di dover scrivere ogni volta `range(len(...))` e rende più chiaro il significato del ciclo.

Se vogliamo vedere esplicitamente cosa produce, possiamo trasformarne il risultato in lista:

```python
lista_new = [2, 5, 7, 'fls']
print(list(enumerate(lista_new)))
```

Output:

```python
[(0, 2), (1, 5), (2, 7), (3, 'fls')]
```

Quindi `enumerate()` associa a ogni elemento la sua posizione e produce coppie del tipo `(indice, elemento)`.

## Attenzione quando si modifica una lista durante un ciclo

Una delle situazioni più delicate riguarda le liste modificate mentre vengono percorse. L'errore tipico è cancellare un elemento durante un ciclo basato sugli indici, pensando che il resto del ciclo continui a funzionare normalmente.

Vediamo un esempio:

```python
lista_interi = [0, 11, 22, 33, 44, 55, 66, 77, 88]

for i in range(len(lista_interi)):
    print(lista_interi[i])
    if i == 3:
        del lista_interi[i]
        print('ho eliminato il 33 dalla lista e ho saltato il 44')
```

L'idea sembra innocua, ma in realtà succedono due cose:

- eliminando un elemento, tutti quelli successivi si spostano a sinistra;
- il ciclo però continua a usare gli indici costruiti sulla lunghezza iniziale.

Dopo l'eliminazione di `33`, il `44` prende il suo posto. Quando il ciclo passa all'indice successivo, il `44` viene saltato. Inoltre il ciclo tenterà comunque di arrivare fino all'ultimo indice della lista originale, ma nel frattempo la lista si è accorciata: questo può produrre un `IndexError`.

Questo problema insegna una regola importante: **modificare una lista mentre la si sta attraversando richiede cautela**.

### Strategie più sicure

Le strategie più comuni sono due:

- costruire una nuova lista con gli elementi che vogliamo tenere;
- scorrere la lista in ordine inverso quando dobbiamo eliminare elementi.

Esempio con una nuova lista:

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

In questo modo non tocchiamo la lista che stiamo leggendo e il comportamento resta prevedibile.

## Contenitori e valori booleani

In Python non solo i numeri e le espressioni logiche possono essere interpretati come veri o falsi. Anche i contenitori hanno un valore booleano.

La regola generale è semplice:

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

Output:

```python
[20.3] contiene almeno un elemento
```

Questo permette di scrivere controlli molto naturali, senza dover usare ogni volta `len(...) > 0`.

```python
if lista:
    print('La lista non è vuota')
```

è spesso più leggibile di:

```python
if len(lista) > 0:
    print('La lista non è vuota')
```

### Dizionario vuoto e insieme vuoto

C'è però una distinzione da ricordare bene. In Python:

```python
{}
```

indica un **dizionario vuoto**, non un insieme vuoto.

Per creare un insieme vuoto bisogna usare:

```python
set()
```

Esempio:

```python
print(bool({}))
print(bool(set()))
```

Output:

```python
False
False
```

Entrambi sono vuoti e quindi falsi, ma rappresentano due strutture diverse.

## Oggetti e metodi

Per capire bene il resto della lezione serve chiarire il concetto di **metodo**.

In Python quasi tutto è un oggetto. Un oggetto contiene dati e mette a disposizione certe operazioni che hanno senso per quel tipo di dato. Queste operazioni si chiamano **metodi**.

La sintassi generale è:

```python
oggetto.metodo(argomenti)
```

Questa forma indica che il metodo appartiene a quel particolare oggetto o, più in generale, a quel tipo di dato.

Per esempio una stringa ha metodi specifici per cercare sottostringhe, cambiare maiuscole e minuscole, verificare certe proprietà del testo. Una lista ha metodi per aggiungere, togliere o riordinare elementi. Un dizionario ha metodi per lavorare con chiavi e valori.

### Alcuni esempi

```python
S = 'Prova Dimostrativa'
print(S.islower())
```

Output:

```python
False
```

Il metodo `islower()` controlla se i caratteri alfabetici della stringa sono tutti minuscoli.

```python
S = 'Prova Dimostrativa'
print(S.find('Prova'))
print(S.find('gnomo'))
```

Output:

```python
0
-1
```

Qui `find()` restituisce:

- la posizione iniziale della sottostringa, se la trova;
- `-1`, se la sottostringa non è presente.

Un altro esempio utile è questo:

```python
print(list('ifjbwie'))
print(set('sdfvigub'))
```

Output possibile:

```python
['i', 'f', 'j', 'b', 'w', 'i', 'e']
{'g', 'f', 'u', 'v', 'i', 'b', 'd', 's'}
```

Con `list()` trasformiamo la stringa in una lista di caratteri, mantenendo ordine e duplicati. Con `set()` otteniamo invece un insieme, quindi:

- i duplicati vengono eliminati;
- l'ordine non è garantito.

## Le liste

Le liste sono tra i contenitori più usati in Python. Sono:

- **ordinate**;
- **modificabili**;
- capaci di contenere elementi anche di tipo diverso.

Proprio perché sono modificabili, offrono molti metodi utili.

### Accesso, modifica e operazioni di base

```python
L[indice]
L[indice] = espressione
elemento in L
L1 + L2
L1 * n
```

Queste operazioni permettono di:

- leggere un elemento in una certa posizione;
- sostituire un elemento;
- controllare se un valore è presente;
- concatenare due liste;
- ripetere una lista più volte.

### `append()`

Il metodo `append()` aggiunge un elemento in fondo alla lista.

```python
L = [1, 2, 3]
L.append(4)
print(L)
```

Output:

```python
[1, 2, 3, 4]
```

### `pop()`

Il metodo `pop()` rimuove un elemento e lo restituisce.

```python
L = [1, 2, 3, 4, 5]
x = L.pop(2)

print(x)
print(L)
```

Output:

```python
3
[1, 2, 4, 5]
```

Questo è importante: `pop()` non si limita a cancellare, ma ci consegna anche il valore estratto.

Se non passiamo alcun indice, viene rimosso l'ultimo elemento:

```python
L = [10, 20, 30]
print(L.pop())
print(L)
```

Output:

```python
30
[10, 20]
```

### `insert()`

Il metodo `insert(posizione, valore)` inserisce un nuovo elemento nella posizione indicata.

```python
L = [1, 2, 4, 5]
L.insert(2, 3)
print(L)
```

Output:

```python
[1, 2, 3, 4, 5]
```

### Altri metodi utili delle liste

Tra i metodi più comuni troviamo anche:

```python
L.remove(elemento)
L.index(elemento)
L.count(elemento)
L.reverse()
L.sort()
```

- `remove(elemento)` elimina il primo elemento uguale al valore indicato;
- `index(elemento)` restituisce l'indice della prima occorrenza;
- `count(elemento)` conta quante volte compare il valore;
- `reverse()` inverte l'ordine della lista;
- `sort()` ordina la lista.

### Metodi distruttivi

Quando diciamo che un metodo è **distruttivo**, intendiamo che modifica direttamente l'oggetto su cui è applicato.

Per esempio:

```python
L = [4, 1, 3, 2]
L.sort()
print(L)
```

Output:

```python
[1, 2, 3, 4]
```

La lista originale è stata cambiata. Questo è diverso da operazioni che producono un nuovo risultato lasciando intatto il contenitore di partenza.

### Assegnamento tramite slice

Le liste supportano anche una forma molto potente di modifica: l'assegnamento su slice.

```python
XXX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
XXX[2:8] = list('abcdef')
print(XXX)
```

Output:

```python
[1, 2, 'a', 'b', 'c', 'd', 'e', 'f', 9, 10]
```

In pratica selezioniamo una porzione della lista e la sostituiamo con altri valori.

Lo slice può anche essere usato per eliminare elementi:

```python
L = [10, 20, 30, 40, 50]
L[1:4] = []
print(L)
```

Output:

```python
[10, 50]
```

## Le tuple

Le tuple assomigliano alle liste perché sono contenitori ordinati, ma hanno una differenza decisiva: sono **immutabili**.

Questo significa che una volta create non possiamo modificarne direttamente gli elementi.

Operazioni tipiche:

```python
T[1]
elemento in T
T1 + T2
T * n
T.index(elemento)
T.count(elemento)
```

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

Se invece proviamo a cambiare un elemento otteniamo un errore:

```python
T = (1, 2, 3)
T[1] = 99
```

Questo fallisce proprio perché le tuple non sono modificabili.

## Gli insiemi

Gli insiemi (`set`) sono contenitori molto diversi da liste e tuple. Sono:

- **non ordinati**;
- **modificabili**;
- privi di duplicati.

Sono particolarmente utili quando interessa la presenza o assenza di valori, oppure quando dobbiamo fare operazioni insiemistiche.

### Operazioni fondamentali

```python
elemento in S
S1 | S2
S1 & S2
S1 - S2
S1 ^ S2
```

Significato:

- `S1 | S2` → unione;
- `S1 & S2` → intersezione;
- `S1 - S2` → differenza;
- `S1 ^ S2` → differenza simmetrica.

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

### Metodi principali degli insiemi

```python
S.add(elemento)
S.remove(elemento)
S.pop()
S1.update(S2)
```

- `add()` aggiunge un elemento;
- `remove()` elimina un elemento;
- `pop()` rimuove e restituisce un elemento arbitrario;
- `update()` aggiunge a un insieme gli elementi di un altro.

Esempio:

```python
S = {1, 2, 3}
S.add(4)
print(S)
```

Output possibile:

```python
{1, 2, 3, 4}
```

## I dizionari

I dizionari (`dict`) permettono di associare una **chiave** a un **valore**. Sono molto utili quando vogliamo accedere ai dati non per posizione numerica, ma tramite un nome o un identificatore.

Esempio semplice:

```python
studente = {
    'nome': 'Anna',
    'voto': 28
}
```

Qui `'nome'` e `'voto'` sono le chiavi, mentre `'Anna'` e `28` sono i valori associati.

### Operazioni e metodi fondamentali

```python
key in D
D[key]
D.keys()
D.values()
D.items()
D.get(key, default)
D.setdefault(key, default)
D.pop(key, default)
D1.update(D2)
```

Queste operazioni permettono di:

- verificare se una chiave è presente;
- leggere il valore associato a una chiave;
- ottenere viste delle chiavi, dei valori o delle coppie chiave-valore;
- leggere un valore con un default in caso di assenza;
- inserire una chiave con un valore iniziale se manca;
- eliminare una chiave restituendo il valore;
- aggiornare un dizionario con un altro.

### `get()`

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

`get()` è utile perché evita errori quando una chiave potrebbe non essere presente.

### `setdefault()`

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

Se la chiave c'è, viene restituito il suo valore. Se non c'è, viene inserita con il valore di default.

### `items()`

Quando vogliamo scorrere insieme chiavi e valori, `items()` è particolarmente comodo.

```python
rubrica = {
    'Luca': '12345',
    'Anna': '67890'
}

for nome, numero in rubrica.items():
    print(nome, numero)
```

Output:

```python
Luca 12345
Anna 67890
```

Questa forma sarà molto utile negli esercizi.

## Conclusione

In questa lezione abbiamo consolidato l'uso dei contenitori da un punto di vista più operativo.

Abbiamo visto che:

- una sequenza può essere percorsa anche tramite indice;
- `enumerate()` rende più elegante il lavoro con indice ed elemento;
- modificare una lista durante il ciclo può causare errori e salti inattesi;
- i contenitori vuoti valgono `False`, quelli non vuoti valgono `True`;
- gli oggetti mettono a disposizione metodi specifici;
- liste, tuple, insiemi e dizionari hanno caratteristiche diverse e quindi richiedono operazioni diverse.

La parte davvero importante non è memorizzare a memoria tutti i metodi, ma iniziare a riconoscere **quale struttura usare** e **quale operazione è più adatta** in un certo contesto. È qui che Python comincia a diventare uno strumento davvero espressivo.
