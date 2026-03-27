# Lezione 3

## Introduzione

In questa lezione introduciamo alcuni strumenti fondamentali per scrivere programmi più articolati:

- assegnamento potenziato
- assegnamento multiplo
- strutture condizionali
- istruzione `match`
- cicli `for` e `while`
- uso di `range()`
- istruzioni `break` e `continue`
- contenitori principali di Python: liste, tuple, insiemi e dizionari

Questi concetti permettono di controllare il flusso del programma e di organizzare gruppi di dati in modo più efficace.

## Assegnamento potenziato

In Python esistono operatori che permettono di aggiornare una variabile applicando un’operazione e riassegnando subito il risultato.

Esempi:

```python
x = 10
x += 1   # equivalente a x = x + 1
x -= 2   # equivalente a x = x - 2
x *= 3   # equivalente a x = x * 3
x //= 4  # equivalente a x = x // 4
x %= 5   # equivalente a x = x % 5
x **= 2  # equivalente a x = x ** 2
```

Questa forma è utile perché rende il codice più compatto e spesso più leggibile.

### Esempio con numeri

```python
contatore = 0
contatore += 1
print(contatore)
```

Output:

```python
1
```

## Assegnamento potenziato con le stringhe

Gli operatori `+` e `*` possono essere usati anche con le stringhe.

- `+` concatena due stringhe
- `*` ripete una stringa un certo numero di volte

Esempio:

```python
a = 'ciao'
a += ' bello'
print(a)

a *= 3
print(a)
```

Output:

```python
ciao bello
ciao bellociao bellociao bello
```

Anche in questo caso l’assegnamento potenziato crea il nuovo valore e lo riassegna alla variabile.

## Assegnamento multiplo

Python permette di assegnare più valori a più variabili in una sola istruzione.

Esempio:

```python
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
```

È importante che il numero di elementi a destra sia uguale al numero di variabili a sinistra.

Esempio:

```python
parole = 'Paperino e Minnie'.split()
p, congiunzione, m = parole
print(p)
print(congiunzione)
print(m)
```

Output:

```python
Paperino
e
Minnie
```

Se il numero degli elementi non coincide, Python genera un errore.

## Spacchettamento di sequenze

L’assegnamento multiplo è molto utile quando si lavora con sequenze come liste e tuple.

Esempio:

```python
scheda = ['Emiliano', 'Pezzilli', 24, 165]
nome, cognome, eta, altezza = scheda

print(nome)
print(cognome)
print(eta)
print(altezza)
```

Questa tecnica si chiama spesso **spacchettamento** o **unpacking**.

## Scambio di variabili

In Python si possono scambiare due valori senza usare una variabile temporanea.

Esempio:

```python
nome = 'Emiliano'
cognome = 'Pezzilli'

nome, cognome = cognome, nome

print(nome)
print(cognome)
```

Output:

```python
Pezzilli
Emiliano
```

Questo funziona perché Python valuta prima l’espressione a destra dell’uguale e solo dopo assegna i valori alle variabili a sinistra.

## Condizioni e percorsi alternativi

Per eseguire istruzioni diverse a seconda di una condizione si usano `if`, `elif` ed `else`.

Sintassi:

```python
if condizione1:
    istruzioni eseguite se condizione1 è True
elif condizione2:
    istruzioni eseguite se condizione1 è False e condizione2 è True
else:
    istruzioni eseguite se tutte le condizioni precedenti sono False
```

Esempio:

```python
voto = 27

if voto >= 30:
    print('Ottimo')
elif voto >= 18:
    print('Esame superato')
else:
    print('Esame non superato')
```

## L’importanza dell’indentazione

In Python l’indentazione non serve solo a rendere il codice ordinato: serve a definire i blocchi di istruzioni.

Esempio:

```python
x = 10

if x > 5:
    print('x è maggiore di 5')
    print('questa riga fa parte del blocco if')

print('questa riga è fuori dal blocco if')
```

Le righe con la stessa indentazione appartengono allo stesso blocco.

## L’istruzione `match`

A partire da Python 3.10 è disponibile l’istruzione `match`, utile per confrontare un valore con più casi possibili.

La sua idea generale è simile a `switch/case` di altri linguaggi, ma in Python è più flessibile.

Sintassi di base:

```python
match variabile:
    case valore1:
        istruzioni
    case valore2 | valore3:
        istruzioni
    case _:
        istruzioni di default
```

Esempio:

```python
comando = 'start'

match comando:
    case 'start':
        print('Avvio')
    case 'stop' | 'end':
        print('Arresto')
    case _:
        print('Comando non riconosciuto')
```

### Match su strutture

`match` può anche riconoscere la forma di alcuni dati.

Esempio:

```python
punto = [10, 20]

match punto:
    case [x, y]:
        print('Coordinate:', x, y)
    case _:
        print('Formato non valido')
```

In questo caso, se il valore è una lista di due elementi, i due valori vengono spacchettati nelle variabili `x` e `y`.

## Cicli e iterazione

In Python i due principali cicli sono:

- `for`
- `while`

Si usano per ripetere istruzioni.

## Il ciclo `for`

Il ciclo `for` è adatto quando vogliamo attraversare una sequenza oppure quando sappiamo già su quali valori iterare.

Sintassi:

```python
for elemento in sequenza:
    blocco di codice
```

Esempio:

```python
for lettera in 'ciao':
    print(lettera)
```

Output:

```python
c
i
a
o
```

### Clausola `else` nel `for`

Il ciclo `for` può avere una clausola `else` opzionale.

```python
for elemento in sequenza:
    blocco di codice
else:
    blocco eseguito se il ciclo termina normalmente
```

La clausola `else` viene eseguita solo se il ciclo termina senza `break`.

## La funzione `range()`

La funzione `range()` genera una sequenza di interi.

Forme principali:

```python
range(fine)
range(inizio, fine)
range(inizio, fine, passo)
```

Esempi:

```python
for i in range(5):
    print(i)
```

Output:

```python
0
1
2
3
4
```

Con due argomenti:

```python
for i in range(3, 8):
    print(i)
```

Output:

```python
3
4
5
6
7
```

Con tre argomenti:

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```python
2
4
6
8
10
```

Il valore finale non è incluso.

## `break` e `continue`

Nei cicli esistono due istruzioni molto importanti:

- `break` interrompe subito il ciclo
- `continue` salta il resto del blocco corrente e passa all’iterazione successiva

Esempio con `break`:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```python
0
1
2
3
4
```

Esempio con `continue`:

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
```

Output:

```python
1
3
5
```

## Il ciclo `while`

Il ciclo `while` ripete un blocco di codice finché una condizione rimane vera.

Sintassi:

```python
while condizione:
    blocco di codice
```

È particolarmente utile quando non sappiamo in anticipo quante iterazioni saranno necessarie.

Esempio:

```python
x = 0

while x < 5:
    print(x)
    x += 1
```

Output:

```python
0
1
2
3
4
```

Se la condizione non viene aggiornata correttamente, si rischia un ciclo infinito.

### Clausola `else` nel `while`

Anche il ciclo `while` può avere una clausola `else`.

```python
while condizione:
    blocco di codice
else:
    blocco eseguito se il ciclo termina senza break
```

## Esempio completo con `while`, `break` e `continue`

```python
x = 0

while x < 20:
    x += 1

    if x == 12:
        break

    if x % 2 == 0:
        continue

    print(x, end=' ')
else:
    print('\nLi ho stampati tutti')

print('\nInizio del codice seguente')
```

In questo esempio:

- `x` viene aumentato a ogni iterazione
- quando `x` vale `12`, il ciclo termina con `break`
- i numeri pari vengono saltati con `continue`
- la clausola `else` non viene eseguita, perché il ciclo termina con `break`

## I contenitori principali di Python

Python mette a disposizione diversi tipi di contenitori per raggruppare più valori.

| Tipo | Nome | Sintassi tipica | Ordinato/indicizzato | Modificabile |
|---|---|---|---|---|
| lista | `list` | `[1, 2, 3]` | sì | sì |
| tupla | `tuple` | `(1, 2, 3)` | sì | no |
| insieme | `set` | `{1, 2, 3}` | no | sì |
| dizionario | `dict` | `{'a': 1, 'b': 2}` | indicizzato per chiave | sì |

Questi contenitori possono avere comportamenti molto diversi.

## Le liste

Le liste sono sequenze ordinate e modificabili.

Esempio:

```python
lista_prova = [2, 5, 7, 'tre']
print(lista_prova)
print(lista_prova[3])

lista_prova[3] = 'tre modificato'
print(lista_prova)
```

Le liste:

- mantengono l’ordine degli elementi
- permettono duplicati
- si possono modificare
- sono indicizzate a partire da `0`

## Le tuple

Le tuple sono simili alle liste, ma non si possono modificare dopo la creazione.

Esempio:

```python
tupla_prova = (2, 5, 7, 'tre')
print(tupla_prova)
print(tupla_prova[1])
```

Se proviamo a cambiare un elemento, otteniamo errore:

```python
tupla_prova[1] = 10
```

Errore:

```python
TypeError
```

Le tuple sono utili quando vogliamo rappresentare dati che non devono cambiare.

## Gli insiemi

Gli insiemi (`set`) sono contenitori modificabili, non indicizzati e senza duplicati.

Esempio:

```python
insieme_prova = {2, 5, 7, 'tre'}
print(insieme_prova)
```

Gli insiemi:

- non garantiscono un ordine fisso
- non permettono duplicati
- non supportano l’indicizzazione

Per questo motivo, un’istruzione come questa genera errore:

```python
print(insieme_prova[2])
```

Errore:

```python
TypeError: 'set' object is not subscriptable
```

Per modificarli si usano metodi specifici:

```python
insieme_prova.add(666)
insieme_prova.update([2, 'cambiato'])
print(insieme_prova)
```

Alcuni metodi utili sono:

- `add()` aggiunge un elemento
- `update()` aggiunge più elementi
- `remove()` rimuove un elemento, ma dà errore se non esiste
- `discard()` rimuove un elemento senza errore se non esiste
- `pop()` rimuove un elemento arbitrario
- `clear()` svuota l’insieme

## I dizionari

I dizionari memorizzano coppie **chiave: valore**.

Esempio:

```python
dizionario_prova = {
    'a': 1,
    'b': 2,
    'c': 3,
    42: 'cammello',
    (2, 5): 'prova'
}

print(dizionario_prova)
```

Nei dizionari:

- ogni chiave deve essere univoca
- si accede ai valori tramite la chiave
- i valori possono essere modificati

Esempio:

```python
new_diz = {'a': 1, 'b': 2, 'c': 3}

print(new_diz['a'])
new_diz['a'] = 4
new_diz['chiave'] = 'valore'
del new_diz['c']

print(new_diz)
```

Se si prova ad accedere a una chiave inesistente, si ottiene un errore `KeyError`.

```python
print(new_diz[4])
```

Per controllare se una chiave è presente si può usare `in`:

```python
print(4 in new_diz)
print('a' in new_diz)
```

### Metodi utili dei dizionari

```python
print(new_diz.keys())
print(new_diz.values())
print(new_diz.items())
```

- `keys()` restituisce le chiavi
- `values()` restituisce i valori
- `items()` restituisce coppie `(chiave, valore)`

## Iterare sui contenitori

### Iterare su lista, tupla o insieme

```python
for elemento in [10, 20, 30]:
    print(elemento)
```

Lo stesso approccio vale anche per tuple e insiemi.

### Iterare su un dizionario

Se vogliamo scorrere chiavi e valori insieme:

```python
dizionario = {'nome': 'Luca', 'eta': 20}

for chiave, valore in dizionario.items():
    print(chiave, valore)
```

Output:

```python
nome Luca
eta 20
```

## Osservazioni finali

In questa lezione abbiamo introdotto strumenti centrali per costruire programmi reali:

- l’assegnamento potenziato permette aggiornamenti rapidi delle variabili
- l’assegnamento multiplo consente di spacchettare sequenze e scambiare valori
- `if`, `elif` ed `else` permettono di scegliere percorsi alternativi
- `match` è utile per distinguere casi diversi in modo più ordinato
- `for` e `while` permettono la ripetizione di istruzioni
- `break` e `continue` modificano il comportamento dei cicli
- liste, tuple, insiemi e dizionari sono i principali contenitori di Python

## Sintesi

Questa lezione estende in modo deciso gli strumenti base di Python:

- controllo del flusso con condizioni e cicli
- gestione di più valori con i contenitori
- aggiornamento e spacchettamento di variabili
- prime tecniche di scansione di sequenze e dizionari

Questi argomenti saranno fondamentali nelle lezioni successive, soprattutto quando inizieremo a scrivere programmi più lunghi e a gestire strutture dati più complesse.
