# Lezione 2

## Introduzione

In questa lezione introduciamo alcuni concetti fondamentali di Python:

- espressioni matematiche
- stringhe
- caratteri speciali
- variabili
- conversione di tipo
- input da tastiera
- valori booleani
- confronti logici

Sono strumenti di base che useremo continuamente nelle lezioni successive.  
In particolare, iniziamo a distinguere bene tra dati numerici e dati testuali, tra operazioni sui valori e operazioni sui caratteri, e tra confronto del contenuto e confronto dell’identità di un oggetto.

## Espressioni matematiche

In Python le espressioni matematiche seguono una precisa gerarchia di priorità.

L’ordine principale è:

1. `**` → potenza
2. `*`, `/`, `//`, `%` → moltiplicazione, divisione, divisione intera, resto
3. `+`, `-` → somma e sottrazione

A parità di priorità, le operazioni vengono eseguite da sinistra verso destra.

Per cambiare l’ordine delle operazioni si usano le parentesi tonde.

Esempio:

```python
print('3 + 14 * 5 / 4 =', 3 + 14 * 5 / 4)
```

Output:

```python
3 + 14 * 5 / 4 = 20.5
```

Alcuni operatori meritano attenzione:

- `/` esegue la divisione normale e produce in genere un `float`
- `//` esegue la divisione intera
- `%` restituisce il resto della divisione
- `**` calcola la potenza

Esempio:

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)
```

Output:

```python
3.5
3
1
8
```

## Le stringhe

In Python il testo è rappresentato dal tipo `str`, chiamato stringa.

Una stringa è una sequenza di caratteri e può essere scritta tra apici singoli o doppi.

Esempi:

```python
'ciao'
"ciao"
'Prova prova'
```

Le stringhe sono **immutabili**: non possono essere modificate direttamente.  
Quando sembra che una stringa cambi, in realtà Python ne crea una nuova in memoria.

Questo significa che non si “corregge” una stringa esistente carattere per carattere come se fosse modificabile: si costruisce una nuova stringa a partire da quella precedente.

## Caratteri speciali

Alcuni caratteri hanno un significato particolare e si scrivono con il backslash `\`.

Esempi:

```python
'\n'   # accapo
'\t'   # tabulazione
'\\'   # backslash
'\''   # apice singolo
'\"'   # doppio apice
```

Esempio:

```python
print('Paperino\nandò\tal\tmare')
```

Se una stringa contiene un apostrofo, si può scrivere in due modi:

```python
"Io sono un po' triste"
```

oppure:

```python
'Io sono un po\' triste'
```

In generale, usare apici singoli o doppi è equivalente.  
Si sceglie la forma più comoda in base al contenuto della stringa.

## Indicizzazione delle stringhe

Ogni carattere di una stringa ha una posizione chiamata indice.

Gli indici partono da `0`.

Esempio:

```python
a = 'Paperino'
print(a[5])
```

Output:

```python
i
```

Nel dettaglio:

- `P` ha indice `0`
- `a` ha indice `1`
- `p` ha indice `2`
- `e` ha indice `3`
- `r` ha indice `4`
- `i` ha indice `5`
- `n` ha indice `6`
- `o` ha indice `7`

Questa numerazione parte sempre da sinistra verso destra.

## Indici negativi

Si possono usare anche indici negativi per partire dalla fine della stringa.

Esempio:

```python
a = 'ciao'
print(a[-1])
print(a[-2])
```

Output:

```python
o
a
```

In questo caso:

- `-1` indica l’ultimo carattere
- `-2` il penultimo
- `-3` il terzultimo

Gli indici negativi sono molto utili quando interessa la parte finale di una stringa.

## Operazioni sulle stringhe

Le stringhe supportano alcune operazioni molto utili.

### Concatenazione

L’operatore `+` unisce due o più stringhe.

```python
'Paperino' + ' ' + 'Minnie'
```

Risultato:

```python
'Paperino Minnie'
```

### Ripetizione

L’operatore `*` ripete una stringa un certo numero di volte.

```python
'Minnie' * 5
```

Risultato:

```python
'MinnieMinnieMinnieMinnieMinnie'
```

Queste operazioni sono diverse dalle operazioni numeriche: qui `+` non somma numeri ma unisce testi, mentre `*` non esegue una moltiplicazione matematica ma ripete il contenuto.

## La funzione `len()`

La funzione `len()` restituisce la lunghezza di una sequenza, per esempio una stringa.

Esempio:

```python
nome = 'Paperino'
print(len(nome))
```

Output:

```python
8
```

La lunghezza corrisponde al numero totale di caratteri presenti nella stringa, spazi inclusi.

## Slicing

Lo slicing permette di estrarre una parte di stringa.

La sintassi generale è:

```python
s[start:stop:step]
```

dove:

- `start` è l’indice iniziale incluso
- `stop` è l’indice finale escluso
- `step` è il passo

Esempio:

```python
a = 'ciaosonoio'
print(a[0:4])
```

Output:

```python
ciao
```

Sono stati presi i caratteri di indice `0`, `1`, `2`, `3`.  
Il carattere in posizione `4` non viene incluso.

Altri esempi:

```python
a = 'programmazione'
print(a[:5])
print(a[5:])
print(a[::2])
print(a[::-1])
```

Output possibile:

```python
progr
ammazione
pormzoi
enoizammargorp
```

Lo slicing è uno strumento fondamentale perché permette di selezionare parti di testo in modo molto compatto.

## Il metodo `find()`

Il metodo `find()` cerca una sottostringa dentro una stringa e restituisce la posizione della prima occorrenza.

Esempio:

```python
a = 'ciao'
print(a.find('i'))
```

Output:

```python
1
```

Se il valore cercato non è presente, `find()` restituisce `-1`.

Esempio:

```python
a = 'ciao'
print(a.find('z'))
```

Output:

```python
-1
```

## Il metodo `split()`

Il metodo `split()` divide una stringa in più parti.

Se non si specifica nulla, Python separa usando gli spazi bianchi: spazi, tabulazioni e accapo.

Esempio:

```python
a = 'Paperino   andò al mare    con Pippo e \n Minnie'
print(a.split())
```

Output:

```python
['Paperino', 'andò', 'al', 'mare', 'con', 'Pippo', 'e', 'Minnie']
```

Il risultato di `split()` non è una stringa, ma una lista di stringhe.  
Più avanti studieremo meglio le liste; per ora è sufficiente osservare che Python ha separato il testo in parole.

## I metodi `lower()` e `upper()`

Le stringhe mettono a disposizione metodi utili per trasformare il testo.

Esempio:

```python
a = 'Ciao Sono IO'
print(a.lower())
print(a.upper())
```

Output:

```python
ciao sono io
CIAO SONO IO
```

Anche in questo caso la stringa originale non viene modificata direttamente: il metodo produce una nuova stringa trasformata.

## Variabili

Una variabile è un nome associato a un valore.

Esempio:

```python
nome = 'Paperino'
eta = 20
```

Le variabili servono per salvare dati e riutilizzarli nel programma.

È buona pratica usare nomi chiari e descrittivi.

Esempi:

```python
altezza_cm = 180
nome_studente = 'Luca'
prezzo_totale = 24.90
```

In Python una variabile non va immaginata come una “scatola” che contiene sempre lo stesso oggetto.  
Più correttamente, il nome della variabile è associato a un riferimento verso un oggetto in memoria.

Per questo motivo, quando si assegna un nuovo valore a una variabile, il nome continua a essere lo stesso ma può riferirsi a un oggetto diverso.

Esempio:

```python
x = 10
print(x)

x = 'ciao'
print(x)
```

Output:

```python
10
ciao
```

Python consente quindi di associare lo stesso nome a valori di tipo diverso in momenti diversi dell’esecuzione.

## Confronto tra valori e identità

In Python bisogna distinguere tra `==` e `is`.

- `==` confronta il contenuto
- `is` confronta l’identità dell’oggetto in memoria

Esempio:

```python
a = 1
b = 1

print(a == b)
print(a is b)
```

In molti casi entrambi restituiscono `True`, ma non significano la stessa cosa.

Per confrontare valori si usa normalmente `==`.

L’operatore `is` si usa soprattutto in casi particolari, ad esempio con `None`.

```python
x = None
print(x is None)
```

Questa distinzione è importante:

- due oggetti diversi possono avere lo stesso contenuto
- `==` controlla se i valori sono uguali
- `is` controlla se è lo stesso identico oggetto

## Conversione di tipo

Python permette di convertire un valore da un tipo a un altro.

Esempi:

```python
str(42)
str(17.34)
int('23')
float('23')
```

Risultati:

```python
'42'
'17.34'
23
23.0
```

Bisogna fare attenzione a questa differenza:

```python
int(3.5)
```

restituisce:

```python
3
```

mentre:

```python
int('3.5')
```

genera errore, perché `'3.5'` non rappresenta un intero valido.

Altro esempio utile:

```python
float('3.5')
```

restituisce:

```python
3.5
```

Quindi la conversione dipende sia dal tipo di partenza sia dalla forma del contenuto.

## Input da tastiera

Per leggere dati inseriti dall’utente si usa `input()`.

Esempio:

```python
nome = input("Ciao, come ti chiami? ")
print("Mi chiamo", nome)
```

`input()` restituisce sempre una stringa.

Questa è una delle cose più importanti da ricordare.  
Anche se l’utente digita un numero, Python lo legge inizialmente come testo.

Esempio:

```python
eta = input("Quanti anni hai? ")
print(eta)
print(type(eta))
```

Output possibile:

```python
18
<class 'str'>
```

Se si vuole usare il valore come numero, bisogna convertirlo.

Esempio:

```python
testo = input("Quanto sei alto? ")
altezza = int(testo)
print("Sono alto", altezza, "cm")
```

## Le f-string

Le f-string sono stringhe formattate che permettono di inserire variabili o espressioni direttamente nel testo.

Si scrivono mettendo `f` prima della stringa.

Esempio:

```python
nome = 'Giovanni'
cognome = 'Rossi'
citta = 'Roma'

lettera = f'''
Caro {nome.upper()} {cognome},
la invito a casa mia a {citta}.
'''

print(lettera)
```

Le parentesi graffe `{}` indicano i punti in cui Python deve sostituire il valore di una variabile o il risultato di un’espressione.

Le f-string rendono il codice più leggibile rispetto alla concatenazione manuale di molte stringhe.

## Il tipo `bool`

Il tipo `bool` rappresenta i valori booleani.

I due valori possibili sono:

```python
True
False
```

Questi valori vengono usati nei confronti e nelle condizioni logiche.

È importante scriverli con l’iniziale maiuscola, perché `true` e `false` non sono validi in Python.

## Vero e falso in Python

In Python molti valori possono essere interpretati come veri o falsi.

Sono considerati falsi, per esempio:

```python
False
0
0.0
''
[]
None
```

Molti altri valori sono invece considerati veri.

Esempio:

```python
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('ciao'))
```

Output:

```python
False
True
False
True
```

Quindi:

- una stringa vuota è falsa
- una stringa non vuota è vera
- zero è falso
- un numero diverso da zero è vero

## Operatori di confronto

Python mette a disposizione i principali operatori di confronto:

```python
==
!=
<
>
<=
>=
```

Esempi:

```python
print(3 < 5)
print(10 == 10)
print(7 != 2)
```

Il risultato di un confronto è sempre un valore booleano, cioè `True` o `False`.

## Confronto tra stringhe

Anche le stringhe si possono confrontare.

Python le confronta in ordine lessicografico, cioè carattere per carattere.

Esempio:

```python
print('Paperino' < 'Topolino')
```

Output:

```python
True
```

Questo accade perché `P` viene prima di `T`.

In generale:

- stringa con stringa si può confrontare
- numero con numero si può confrontare
- stringa e numero non si confrontano direttamente in modo sensato in questo contesto elementare

## Operatori logici

Le espressioni booleane possono essere combinate con gli operatori logici:

- `and`
- `or`
- `not`

Esempio:

```python
print(True and True)
print(True and False)
print(True or False)
print(not True)
```

Significato:

- `and` è vero solo se entrambe le condizioni sono vere
- `or` è vero se almeno una condizione è vera
- `not` inverte il valore logico

Questi operatori permettono di costruire condizioni più complesse.

Esempio:

```python
eta = 20
print(eta >= 18 and eta < 30)
```

## Priorità logica

Nelle espressioni logiche la priorità è:

1. `not`
2. `and`
3. `or`

Esempio:

```python
print(True or False and False)
```

viene interpretato come:

```python
print(True or (False and False))
```

quindi il risultato è:

```python
True
```

Quando un’espressione è poco chiara, conviene comunque usare le parentesi per renderla più leggibile.

## Osservazioni finali

In questa lezione abbiamo introdotto alcuni strumenti fondamentali:

- le espressioni matematiche seguono regole di priorità
- le stringhe sono sequenze di caratteri immutabili
- le variabili permettono di salvare e riutilizzare valori
- `input()` restituisce sempre una stringa
- i valori possono essere convertiti da un tipo a un altro
- le stringhe possono essere analizzate con indici, slicing e metodi
- `==` e `is` non hanno lo stesso significato
- i valori booleani sono fondamentali nei confronti e nelle condizioni logiche

Questi concetti costituiscono la base per scrivere programmi più articolati e per comprendere meglio il comportamento del linguaggio.
