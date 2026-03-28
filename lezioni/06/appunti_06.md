# Lezione 6

## Introduzione

Questa lezione mette ordine in diversi concetti che in Python sembrano separati ma in realtà sono collegati:

- come vengono cercati i nomi nel programma;
- differenza tra variabili locali, globali e nomi built-in;
- effetti collaterali delle funzioni;
- argomenti obbligatori e opzionali;
- pericoli dei valori di default mutabili;
- packing e unpacking con `*`;
- input da tastiera e gestione degli errori;
- ordinamento semplice e ordinamento con criteri personalizzati.

È una lezione più concettuale delle precedenti. Non introduce solo nuova sintassi: chiarisce **perché** alcuni programmi si comportano in modo apparentemente strano. Per questo ha un peso reale nella comprensione del linguaggio. In particolare, i temi su namespace, parametri, mutabilità ed errori ricompaiono continuamente negli esercizi e all'esame.

## Identificatori validi in Python

Un **identificatore** è un nome che usiamo per variabili, funzioni, classi o metodi.

Regole essenziali:

- deve iniziare con una lettera oppure con `_`;
- non può contenere spazi;
- dopo il primo carattere può contenere lettere, cifre e `_`.

Esempi validi:

```python
nome
eta2
_totale
media_voti
```

Esempi non validi:

```python
2nome       # inizia con una cifra
nome utente # contiene uno spazio
prezzo-euro # il trattino non è ammesso
```

Essere rigorosi nei nomi non è solo una questione sintattica. Un buon nome aiuta anche a capire in quale parte del programma ha senso usarlo.

## Namespace: dove vivono i nomi

Quando scrivi un nome come `x`, `print`, `sum` o `mia_funzione`, Python deve capire **a cosa si riferisce**.

Per farlo usa dei contenitori logici chiamati **namespace**. Un namespace è, in sostanza, una tabella di associazione tra nomi e oggetti.

In questa lezione compaiono almeno questi livelli:

- **built-in**: contiene nomi già disponibili in Python, come `print`, `len`, `sum`, `int`;
- **globale**: contiene i nomi definiti nel file principale;
- **di modulo**: contiene i nomi interni a un modulo importato;
- **locale**: contiene i nomi interni alla funzione che in quel momento è in esecuzione.

### Esempio intuitivo

```python
x = 10

def mostra():
    y = 20
    print(x)
    print(y)
```

Qui:

- `x` è un nome globale;
- `y` è un nome locale alla funzione `mostra()`;
- `print` è un nome built-in.

Quando `mostra()` termina, il nome locale `y` sparisce. `x` invece continua a esistere nel programma principale.

## Ordine di ricerca dei nomi: LEGB

Python cerca i nomi secondo l'ordine **LEGB**:

1. **L - Local**: namespace locale della funzione in esecuzione;
2. **E - Enclosing**: eventuali funzioni esterne che racchiudono quella corrente;
3. **G - Global**: namespace globale del file principale;
4. **B - Built-in**: namespace interno di Python.

La prima corrispondenza trovata vince.

Questo significa che un nome locale può **nascondere** un nome globale con lo stesso identificatore.

### Esempio

```python
G = 42

def prova(valore):
    G = valore
    print('Dentro la funzione:', G)

print('Prima:', G)
prova(555)
print('Dopo:', G)
```

Output:

```python
Prima: 42
Dentro la funzione: 555
Dopo: 42
```

La `G` interna alla funzione non modifica quella globale: crea un nuovo nome locale con lo stesso identificatore.

## Variabili globali e parola chiave `global`

Se dentro una funzione vuoi modificare davvero una variabile globale, devi dichiararlo esplicitamente con `global`.

```python
G = 42

def cambia(valore):
    global G
    G = valore

print(G)
cambia(666)
print(G)
```

Output:

```python
42
666
```

### Osservazione importante

`global` esiste, ma va usato con prudenza.

Motivo:

- rende il comportamento della funzione meno prevedibile;
- aumenta gli effetti collaterali;
- rende più difficile testare e riusare il codice.

Nella maggior parte dei casi è meglio far restituire un valore con `return` e assegnarlo all'esterno.

## Effetti collaterali

Una funzione ha un **effetto collaterale** quando modifica qualcosa fuori da sé:

- una variabile globale;
- un oggetto mutabile passato come argomento;
- un file;
- ciò che appare a schermo;
- altro stato esterno.

Stampare con `print()` è già, in senso ampio, un effetto collaterale. Ma in questa lezione il punto centrale è un altro: **modificare dati esterni in modo non evidente**.

## Argomenti delle funzioni: cosa si può modificare davvero

Gli argomenti formali di una funzione sono nomi locali. Quando chiami la funzione, quei nomi vengono associati agli oggetti passati nella chiamata.

Questo porta a una distinzione essenziale.

### Caso 1: riassegnare il nome locale

```python
def rimpiazza(lista):
    lista = ['uno', 'due', 'tre']
```

Qui cambi solo l'associazione del nome locale `lista`. Il chiamante non vede nessun cambiamento.

### Caso 2: modificare il contenuto di un oggetto mutabile

```python
def togli_terzo(lista):
    lista.pop(2)
```

Qui non cambi il nome locale: modifichi direttamente il contenuto dell'oggetto ricevuto. Se il chiamante possiede quella stessa lista, vedrà la modifica.

### Esempio completo

```python
nomi = ['Anna', 'Luca', 'Marco', 'Sara']

def togli_terzo(lista):
    lista.pop(2)

print(nomi)
togli_terzo(nomi)
print(nomi)
```

Output:

```python
['Anna', 'Luca', 'Marco', 'Sara']
['Anna', 'Luca', 'Sara']
```

Questo è un vero effetto collaterale.

## Mutabilità e chiarezza del codice

La regola pratica da portarsi dietro è questa:

- se vuoi **restituire un risultato**, usa `return`;
- se vuoi **modificare intenzionalmente** un oggetto esterno, fallo solo quando è davvero il comportamento desiderato;
- se una funzione modifica una lista ricevuta, deve essere molto chiaro dal nome, dai commenti o dal contesto.

### Versione non distruttiva

```python
def senza_modificare(lista):
    nuova = lista.copy()
    nuova.pop(2)
    return nuova
```

### Versione distruttiva

```python
def modifica_in_posto(lista):
    lista.pop(2)
```

Le due funzioni non fanno la stessa cosa, anche se sembrano simili.

## `return` interrompe la funzione

L'istruzione `return`:

- termina immediatamente l'esecuzione della funzione;
- restituisce al chiamante il valore indicato.

```python
def segno(x):
    if x > 0:
        return 'positivo'
    if x < 0:
        return 'negativo'
    return 'zero'
```

Appena viene eseguito un `return`, il resto della funzione non viene più eseguito.

### Se manca `return`

Se una funzione termina senza eseguire `return`, Python restituisce automaticamente `None`.

```python
def saluta(nome):
    print('Ciao', nome)

risultato = saluta('Luca')
print(risultato)
```

Output:

```python
Ciao Luca
None
```

Questo è uno degli errori più frequenti negli esercizi: pensare che una funzione "torni" qualcosa solo perché lo stampa.

## Argomenti obbligatori e opzionali

Nella definizione di una funzione possiamo avere:

- **argomenti obbligatori**: vanno sempre passati;
- **argomenti opzionali**: hanno un valore di default e quindi possono essere omessi.

### Regola sintattica fondamentale

Prima vanno gli obbligatori, poi gli opzionali.

```python
def descrivi(nome, eta, citta='Roma', studente=True):
    print(nome, eta, citta, studente)
```

Questa definizione è valida.

```python
def errore(citta='Roma', nome):
    pass
```

Questa invece è sintatticamente scorretta.

### Chiamata per posizione e per nome

```python
descrivi('Anna', 20)
descrivi('Anna', 20, 'Milano', False)
descrivi('Anna', 20, studente=False)
descrivi(eta=20, nome='Anna', citta='Napoli')
```

Gli argomenti opzionali sono comodi, ma bisogna capire bene come Python assegna i valori ai parametri.

## Valori di default: quando vengono creati

Il punto delicato è questo: il valore di default viene creato **al momento della definizione della funzione**, non a ogni chiamata.

Per tipi immutabili questo in genere non crea problemi:

```python
def potenza(base, esponente=2):
    return base ** esponente
```

Per tipi mutabili invece può diventare un disastro.

## Il problema dei default mutabili

Esempio sbagliato:

```python
def aggiungi_elemento(x, lista=[]):
    lista.append(x)
    return lista

print(aggiungi_elemento(1))
print(aggiungi_elemento(2))
print(aggiungi_elemento(3))
```

Output:

```python
[1]
[1, 2]
[1, 2, 3]
```

Molti si aspetterebbero:

```python
[1]
[2]
[3]
```

ma non succede, perché la stessa lista di default viene riusata in chiamate successive.

### Soluzione corretta

Si usa `None` come sentinella.

```python
def aggiungi_elemento(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista
```

Ora, se non viene passata alcuna lista, ne viene creata una nuova a runtime.

### Regola pratica da ricordare

Non usare mai come default mutabili come:

- `[]`
- `{}`
- `set()`

se poi prevedi di modificarli dentro la funzione.

## Piccola parentesi: perché `is None` e non `== None`

Quando controlli se un valore è `None`, in Python si usa la forma:

```python
if x is None:
```

Non:

```python
if x == None:
```

`None` è un singleton speciale del linguaggio, quindi il confronto di identità è la forma corretta e standard.

## Problem solving: lo stesso problema, più strategie

La lezione propone un quesito logico e lo risolve in più modi:

- con una scansione e un conteggio;
- con gli insiemi;
- con i dizionari.

L'idea didattica importante non è il rompicapo in sé, ma questa:

> uno stesso problema può essere modellato in modi diversi a seconda della struttura dati scelta.

Questo è molto utile all'esame. Spesso non conta solo arrivare alla risposta, ma scegliere una rappresentazione sensata.

### Metodo 1: scansione lineare

Si visitano le domande una per una e si confrontano risposta corretta e risposta data.

### Metodo 2: insiemi

Si rappresentano come insiemi i numeri delle domande che soddisfano certe proprietà e poi si usano intersezioni e unioni.

### Metodo 3: dizionari

Si costruiscono dizionari del tipo `domanda -> risposta` e poi si confrontano le coppie.

Questa tripla soluzione è un ottimo esempio di maturità algoritmica: stesso problema, tre punti di vista.

## Packing negli assegnamenti

Finora avevi visto assegnamenti multipli con stesso numero di variabili ed elementi:

```python
a, b, c = [1, 2, 3]
```

Con l'asterisco `*` puoi raccogliere più valori rimanenti in una sola variabile. Questo si chiama **packing**.

### Esempi

```python
a, b, *c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
```

Output:

```python
1
2
[3, 4, 5]
```

Altro esempio:

```python
*a, b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
```

Output:

```python
[1, 2, 3]
4
5
```

### Regola

In un assegnamento multiplo può esserci al massimo una variabile con `*`.

## Packing negli argomenti delle funzioni

La stessa idea compare nelle funzioni con un numero variabile di argomenti.

```python
def mia_print(*valori):
    print(valori)

mia_print(10, 20, 30)
```

Output:

```python
(10, 20, 30)
```

Dentro la funzione, `valori` è una **tupla** che contiene tutti gli argomenti posizionali ricevuti. La lezione usa questo per spiegare perché `print()` può accettare un numero arbitrario di valori.

### Esempio realistico

```python
def media(*numeri):
    return sum(numeri) / len(numeri)

print(media(10, 20, 30))
```

## Unpacking nelle espressioni

Se il packing raccoglie valori a sinistra di un assegnamento, l'**unpacking** li espande dentro un'altra espressione.

```python
numeri = [3, 4, 5]
nuova = [1, 2, *numeri, 6]
print(nuova)
```

Output:

```python
[1, 2, 3, 4, 5, 6]
```

Altro esempio:

```python
parola = 'ciao'
caratteri = [*parola]
print(caratteri)
```

Output:

```python
['c', 'i', 'a', 'o']
```

### Uso molto comune con le funzioni

```python
def somma(a, b, c):
    return a + b + c

valori = [10, 20, 30]
print(somma(*valori))
```

Qui `*valori` spacchetta la lista nei tre argomenti richiesti.

## Input da tastiera

Per leggere dati da tastiera si usa `input()`.

```python
nome = input('Come ti chiami? ')
print(nome)
```

`input()` restituisce sempre una stringa. Se vuoi un numero, devi convertire.

```python
risposta = input('Inserisci un intero: ')
numero = int(risposta)
```

Questo punto era già comparso in lezioni precedenti, ma qui viene approfondito sul lato degli errori.

## Errori di conversione e `try/except`

Se l'utente scrive qualcosa che non può essere convertito, il programma genera un'eccezione.

```python
risposta = input('Inserisci un intero: ')
numero = int(risposta)
```

Se l'utente inserisce `3.56` oppure `ciao`, ottieni un `ValueError`.

Per gestire questi casi si usa `try/except`.

```python
def e_numero(testo):
    try:
        float(testo)
        return True
    except ValueError:
        return False
```

### Struttura generale

```python
try:
    codice_rischioso
except NomeErrore:
    gestione_dell_errore
finally:
    codice_finale_opzionale
```

### Esempio utile

```python
while True:
    testo = input('Inserisci un numero tra 1 e 100: ')
    try:
        numero = float(testo)
    except ValueError:
        print('Input non valido')
        continue

    if 1 <= numero <= 100:
        break

    print('Numero fuori intervallo')

print(int(numero))
```

Questa struttura è molto più robusta di una semplice conversione diretta.

## Operatore walrus `:=`

La lezione introduce anche il cosiddetto **walrus operator** `:=`, che permette di assegnare un valore dentro un'espressione.

Esempio:

```python
media = (somma := sum([1, 2, 3])) / 3
print(somma)
print(media)
```

È lecito usarlo, ma va dosato. In codice didattico o d'esame, spesso una riga in più ma più chiara è preferibile.

### Versione più leggibile

```python
somma = sum([1, 2, 3])
media = somma / 3
```

## Ordinare gli elementi

Python offre due strade principali per ordinare.

### Metodo `sort()`

Modifica la lista esistente.

```python
numeri = [5, 2, 8, 1]
numeri.sort()
print(numeri)
```

### Funzione `sorted()`

Restituisce una nuova lista ordinata, lasciando intatto l'originale.

```python
numeri = [5, 2, 8, 1]
ordinati = sorted(numeri)
print(numeri)
print(ordinati)
```

La lezione sottolinea proprio questa differenza tra approccio distruttivo e non distruttivo.

### Ordine inverso

```python
parole = ['uno', 'due', 'tre']
print(sorted(parole, reverse=True))
```

## Ordinamenti più sofisticati

Un concetto molto utile è che possiamo ordinare non solo per il valore “naturale”, ma per un **criterio** scelto da noi.

### Esempio: per lunghezza e poi alfabetico

```python
parole = ['uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette']
ordinate = sorted(parole, key=lambda parola: (len(parola), parola))
print(ordinate)
```

La tupla `(len(parola), parola)` dice a Python:

1. confronta prima la lunghezza;
2. se due parole hanno la stessa lunghezza, confrontale alfabeticamente.

Questo è esattamente il principio mostrato nella lezione con la trasformazione in coppie e terne.

## Stabilità dell'ordinamento

L'ordinamento di `sorted()` è **stabile**: se due elementi risultano uguali secondo il criterio scelto, mantengono il loro ordine relativo originale. La lezione lo mostra prima costruendo tuple con posizione e poi osservando che `sorted()` gestisce già questo comportamento in modo affidabile.

### Esempio

```python
parole = ['aa', 'bb', 'cc']
print(sorted(parole, key=len))
```

Tutte hanno la stessa lunghezza, quindi l'ordine resta quello iniziale.

## Trasformazione di Schwartz: idea pratica

La lezione introduce anche la cosiddetta **trasformazione di Schwartz**: trasformare temporaneamente ogni elemento in una struttura più adatta al confronto, ordinarla, poi recuperare l'elemento originale.

In Python spesso questa idea viene espressa in forma più diretta tramite `key=`.

### Esempio equivalente moderno

```python
def criterio(parola):
    return (len(parola), parola.lower(), parola)

parole = ['PaPerino', 'plUTO', 'TopoLINO', 'minniE', 'PLUTO']
print(sorted(parole, key=criterio))
```

Qui ordiniamo:

1. per lunghezza;
2. poi ignorando maiuscole/minuscole;
3. infine usando la stringa originale come spareggio.

## Errori tipici da evitare

Questa lezione è piena di trappole classiche.

### 1. Confondere stampa e ritorno

```python
def doppio(x):
    print(x * 2)
```

Questa funzione **non restituisce** il doppio: lo stampa soltanto.

### 2. Pensare che riassegnare un parametro modifichi il chiamante

```python
def cambia(lista):
    lista = [1, 2, 3]
```

Non modifica la lista esterna.

### 3. Usare default mutabili

```python
def sbagliata(x, lista=[]):
    ...
```

È una delle fonti di bug più insidiose.

### 4. Usare `global` come soluzione automatica

Spesso è sintomo di una struttura poco pulita.

### 5. Convertire input senza gestire eccezioni

```python
numero = int(input('Numero: '))
```

Funziona solo se l'utente inserisce esattamente ciò che ti aspetti.

## Valutazione discrezionale ai fini dell'esame

### Utilità complessiva: **alta**

Questa lezione è effettivamente utile ai fini dell'esame.

### Parti ad altissima priorità

- namespace locale e globale;
- differenza tra modifica di un oggetto mutabile e semplice riassegnazione locale;
- `return` e valore `None` implicito;
- parametri obbligatori e opzionali;
- default mutabili e uso di `None`;
- `try/except` per input e conversioni;
- `sorted()` e `sort()` con differenza tra approccio distruttivo e non distruttivo.

Questi sono argomenti che possono comparire sia in domande teoriche sia in esercizi pratici.

### Parti utili ma di priorità media

- packing e unpacking;
- walrus operator `:=`;
- trasformazione di Schwartz come nome tecnico.

Sono utili per maturità di linguaggio e comprensione, ma non le metterei allo stesso livello dei concetti su mutabilità, parametri e ritorno di funzione.

### Giudizio finale

Se devi selezionare cosa fissare bene per l'esame, questa è una lezione da **studiare sul serio**, non da saltare. Non è tanto importante memorizzare ogni esempio, quanto interiorizzare le differenze concettuali che spiega. In particolare, se capisci davvero:

- come Python cerca i nomi,
- cosa viene modificato quando passi una lista a una funzione,
- quando una funzione restituisce `None`,
- perché i default mutabili sono pericolosi,

allora farai un salto netto nella qualità del tuo ragionamento sugli esercizi.
