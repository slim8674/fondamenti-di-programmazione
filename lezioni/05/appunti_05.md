# Lezione 5

## Introduzione

In questa lezione entriamo in uno dei punti più importanti della programmazione: **spezzare un programma in parti riusabili**. Finché gli esempi sono piccoli, si può anche scrivere tutto in sequenza. Appena il codice cresce, però, iniziano i problemi: istruzioni duplicate, correzioni da fare in più punti, ragionamenti confusi e debug più difficile.

Per evitare questo caos si usano soprattutto due strumenti:

- i **moduli**, cioè file separati che contengono codice riutilizzabile;
- le **funzioni**, cioè blocchi di istruzioni che ricevono dati, svolgono un compito preciso e possono restituire un risultato.

Nelle slide della lezione il professore passa poi a un piccolo problema di problem solving: trovare la cifra in una certa posizione nella stringa infinita `12345678910111213...`. Quel problema è utile perché mostra bene il metodo corretto: **dividere un problema grande in sottoproblemi più piccoli**, scrivere funzioni dedicate e confrontare soluzioni diverse, non solo in termini di correttezza ma anche di efficienza.

## Moduli e `import`

Quando un programma cresce, non conviene mettere tutto in un solo file. Python permette di distribuire il codice in più file, chiamati **moduli**.

Importare un modulo significa rendere disponibili nel programma funzioni, variabili e costanti definite altrove.

### Forma 1: importare il modulo intero

```python
import math

print(math.pi)
print(math.sqrt(25))
```

Qui nel namespace globale entra solo il nome `math`. Per usare ciò che contiene, bisogna scrivere `math.qualcosa`.

Questo stile è molto chiaro perché rende evidente da dove arriva un certo nome.

### Forma 2: importare solo alcuni nomi

```python
from math import pi, sqrt

print(pi)
print(sqrt(25))
```

Qui invece i nomi `pi` e `sqrt` entrano direttamente nel namespace corrente.

È una forma più comoda da scrivere, ma richiede più attenzione perché può creare **collisioni di nomi** con funzioni o variabili già esistenti.

### Forma da evitare: `from modulo import *`

```python
from math import *
```

Questa forma importa tutto nel namespace corrente. Nelle slide viene esplicitamente sconsigliata perché rende il codice poco leggibile e aumenta il rischio di conflitti tra nomi. In pratica, dopo un po', non è più chiaro quali nomi siano definiti da noi e quali arrivino dal modulo importato. fileciteturn0file0

### Nota pratica sugli import

Quando un modulo è già stato importato, Python in genere non lo rilegge da zero dal file ogni volta, ma riusa la versione già caricata. Questo evita lavoro inutile e rende gli import efficienti.

## Perché servono le funzioni

Una regola di stile fondamentale è questa:

- **mai** copiare e incollare più volte lo stesso blocco di codice;
- **sempre** trasformare quel blocco in una funzione, se svolge un compito riconoscibile.

Il motivo è semplice. Se il codice è duplicato in tre punti e scopri un errore, devi correggerlo tre volte. Se invece quel comportamento è racchiuso in una funzione, la correzione si fa in un solo punto.

Le funzioni servono quindi a:

- riutilizzare codice;
- separare i compiti;
- rendere il programma più leggibile;
- semplificare test e debug.

## Come si definisce una funzione

La sintassi base è questa:

```python
def nome_funzione(argomenti):
    """Breve descrizione della funzione."""
    istruzioni
    return risultato
```

Gli elementi da capire sono quattro.

### 1. `def`

La parola chiave `def` introduce la definizione della funzione.

### 2. Nome della funzione

Il nome dovrebbe descrivere cosa fa la funzione.

Meglio:

```python
def calcola_media(voti):
```

Peggio:

```python
def pippo(x):
```

Nomi chiari riducono gli errori e rendono il codice leggibile anche dopo giorni o settimane.

### 3. Argomenti

Gli argomenti sono i dati che la funzione deve ricevere per poter lavorare.

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Qui `base` e `altezza` sono i nomi usati **dentro** la funzione per riferirsi ai valori ricevuti.

### 4. Corpo della funzione

Tutto ciò che appartiene alla funzione deve essere **indentato** rispetto alla riga con `def`.

In Python l'indentazione non è decorativa: definisce il blocco di istruzioni.

Per convenzione si usano **4 spazi**. Niente tab.

## La docstring

Subito sotto l'intestazione di una funzione si può inserire una stringa descrittiva, detta **docstring**.

```python
def area_rettangolo(base, altezza):
    """Restituisce l'area di un rettangolo."""
    return base * altezza
```

La docstring non è obbligatoria, ma è fortemente consigliata perché documenta il comportamento della funzione e può essere mostrata dagli strumenti di help.

## `return`: il risultato della funzione

Una funzione può produrre un risultato con `return`.

```python
def quadrato(x):
    return x ** 2
```

Quando scriviamo:

```python
risultato = quadrato(5)
```

succede questo:

1. la funzione viene chiamata con il valore `5`;
2. il parametro `x` assume quel valore;
3. viene calcolato `x ** 2`;
4. il valore `25` viene restituito;
5. `risultato` riceve `25`.

### Una funzione può restituire più valori

In Python possiamo restituire più risultati in una sola volta.

```python
def statistiche(numeri):
    minimo = min(numeri)
    massimo = max(numeri)
    media = sum(numeri) / len(numeri)
    return media, minimo, massimo
```

Uso:

```python
m, mn, mx = statistiche([10, 20, 30])
print(m, mn, mx)
```

## Parametri formali e argomenti attuali

Nella definizione:

```python
def saluta(nome):
    print("Ciao", nome)
```

`nome` è un **parametro formale**: è il nome usato dentro la funzione.

Nella chiamata:

```python
saluta("Luca")
```

`"Luca"` è l'**argomento attuale**: è il valore concreto passato alla funzione in quella chiamata.

Questa distinzione conta perché i nomi usati nella definizione non devono per forza coincidere con quelli usati nel codice principale.

```python
def saluta(nome):
    print("Ciao", nome)

persona = "Luca"
saluta(persona)
```

Qui dentro la funzione si parla di `nome`, fuori si parla di `persona`, ma il valore passato è lo stesso.

## Variabili locali e variabili globali

Uno dei concetti centrali della lezione è il **namespace**, cioè lo spazio dei nomi disponibili in un certo contesto.

### Variabili locali

Le variabili create dentro una funzione sono in genere **locali** a quella funzione.

```python
def esempio():
    x = 10
    print(x)
```

La variabile `x` esiste solo durante l'esecuzione della funzione.

Se proviamo a usarla fuori:

```python
esempio()
print(x)
```

ottieni un errore `NameError`, perché quel nome non esiste nel namespace globale.

### Variabili globali

Le variabili definite nel programma principale appartengono al namespace globale.

```python
messaggio = "ciao"


def stampa_messaggio():
    print(messaggio)
```

In questo caso la funzione può leggere `messaggio` se non esiste un nome locale che lo nasconde. Ma in questa fase conviene seguire una regola semplice: **passa i dati tramite argomenti e restituisci i risultati con `return`**, invece di affidarti troppo a variabili globali.

## Il ciclo di vita delle variabili locali

Ogni volta che una funzione viene chiamata, Python crea un nuovo spazio locale per quella chiamata.

Questo implica tre cose importanti.

### 1. Ogni chiamata ha le sue variabili

```python
def raddoppia(x):
    y = x * 2
    return y
```

Se la chiami due volte, ogni chiamata ha il proprio `x` e il proprio `y`.

### 2. Le variabili locali nascono quando la funzione viene eseguita

Non esistono già al momento della definizione. Vengono create quando la funzione parte davvero.

### 3. Le variabili locali spariscono quando la funzione finisce

Quando la funzione termina, il namespace locale viene rilasciato. Gli oggetti creati dentro la funzione possono però sopravvivere se vengono restituiti o assegnati altrove.

Per esempio:

```python
def concatena(prima, seconda):
    nuovo_testo = prima + " " + seconda
    return nuovo_testo

risultato = concatena("ciao", "mondo")
print(risultato)
```

La variabile locale `nuovo_testo` sparisce alla fine della funzione, ma la stringa costruita sopravvive perché è stata restituita e assegnata a `risultato`.

## Chiamate di funzioni annidate

Una funzione può chiamarne un'altra.

```python
def quadrato(x):
    return x ** 2


def somma_quadrati(a, b):
    qa = quadrato(a)
    qb = quadrato(b)
    return qa + qb
```

Qui `somma_quadrati()` usa `quadrato()` come sottoprocedura.

L'idea importante è questa: **ogni chiamata ha il suo namespace locale separato**. Anche se il flusso è annidato, le variabili locali di una funzione non si mescolano automaticamente con quelle delle altre.

## Buono stile nei nomi

Meglio:

```python
def calcola_altezza_media(altezze):
    somma_altezze = sum(altezze)
    return somma_altezze / len(altezze)
```

Peggio:

```python
def pippo(lista):
    sa = sum(lista)
    return sa / len(lista)
```

La seconda versione funziona uguale, ma è molto meno leggibile.

## Primo problema di problem solving: la stringa infinita dei numeri

Costruire mentalmente o algoritmicamente la sequenza

```python
123456789101112131415...
```

poi chiedersi quale cifra occupa una certa posizione, per esempio la 200ª.

Questo esempio è utile non tanto per il problema in sé, ma per il metodo.

## Metodo corretto: scomporre il problema

Un problema complesso si affronta meglio se viene spezzato in sottoproblemi più semplici.

Per esempio, per trovare la N-esima cifra possiamo:

1. costruire una stringa abbastanza lunga;
2. prendere il carattere in posizione `N - 1`.

Oppure possiamo ragionare in modo più efficiente:

1. trovare **in quale numero** cade la N-esima cifra;
2. trovare **quale cifra** di quel numero ci interessa.

Questa mentalità è centrale in programmazione.

## Prima soluzione: costruire la stringa

Una soluzione semplice da capire è questa:

```python
def costruisci_stringona(n):
    testo = ""
    for i in range(1, n + 1):
        testo += str(i)
    return testo


def cerca_con_stringa(n):
    stringona = costruisci_stringona(n)
    return stringona[n - 1]
```

### Perché funziona

- `costruisci_stringona(n)` concatena i numeri da `1` in poi;
- il risultato contiene sicuramente almeno `n` cifre;
- la cifra cercata è al posto `n - 1`, perché gli indici partono da zero.

### Limite di questa soluzione

È semplice, ma non è efficiente:

- crea stringhe sempre più grandi;
- fa molte concatenazioni;
- usa più memoria del necessario.

Questa soluzione va bene come primo passo di ragionamento, ma non è la migliore dal punto di vista computazionale.

## Variante leggermente migliore: fermarsi appena basta

Invece di concatenare fino a `n`, si può concatenare finché la lunghezza della stringa non raggiunge almeno `n`.

```python
def costruisci_stringona_smart(n):
    testo = ""
    i = 1

    while len(testo) < n:
        testo += str(i)
        i += 1

    return testo
```

Questa versione evita lavoro inutile, ma resta basata sulla costruzione di una stringa lunga.

## Seconda soluzione: evitare la stringa inutile

L'idea più interessante può essere questa:

- scorri i numeri a partire da `1`;
- per ciascuno calcola quante cifre ha;
- sottrai quel numero di cifre da `n` finché non arrivi al numero che contiene la cifra desiderata;
- a quel punto estrai la cifra dal numero trovato.

### Funzione che trova il numero giusto

```python
def numero_e_posizione(n, conta_cifre):
    for numero in range(1, n + 1):
        cifre = conta_cifre(numero)

        if cifre < n:
            n -= cifre
        else:
            return numero, n
```

Qui la funzione restituisce due cose:

- il numero in cui cade la cifra cercata;
- la posizione della cifra dentro quel numero, contando da `1`.

### Estrarre la cifra

```python
def cerca_senza_stringona(n, conta_cifre):
    numero, posizione = numero_e_posizione(n, conta_cifre)
    testo = str(numero)
    return testo[posizione - 1]
```

Notare bene: qui la conversione in stringa avviene solo **una volta**, sul numero finale. Non stiamo più costruendo una stringa enorme di tutte le cifre precedenti.

## Come contare le cifre di un numero

### Opzione 1: convertire in stringa

```python
def num_cifre_str(x):
    return len(str(x))
```

È semplicissima e in pratica spesso va benissimo.

### Opzione 2: usare il logaritmo

```python
from math import log10


def num_cifre_log(x):
    return int(log10(x)) + 1
```

Questa è elegante, ma richiede più attenzione teorica e si applica bene solo per numeri positivi.

### Opzione 3: usare le potenze di 10

```python
def num_cifre_potenze(x):
    cifre = 0
    potenza = 1

    while potenza <= x:
        cifre += 1
        potenza *= 10

    return cifre
```

Questa evita conversioni a stringa e non richiede logaritmi, ma è un po' più lunga.

## Terza idea: ragionare per blocchi di cifre

L'ultima parte delle slide mostra un approccio ancora più furbo: ragionare per **blocchi di numeri con uguale numero di cifre**. fileciteturn0file0

- i numeri da `1` a `9` hanno 1 cifra → in totale 9 cifre;
- i numeri da `10` a `99` hanno 2 cifre → in totale `90 * 2 = 180` cifre;
- i numeri da `100` a `999` hanno 3 cifre → in totale `900 * 3 = 2700` cifre.

Formula generale:

- i numeri con `k` cifre sono `9 * 10**(k - 1)`;
- il blocco delle cifre corrispondenti contiene `k * 9 * 10**(k - 1)` cifre.

Questo approccio è più efficiente perché permette di saltare interi blocchi senza scorrere numero per numero.

## Esempio manuale: 200ª cifra

1. Il blocco da 1 cifra contiene 9 cifre.
2. Il blocco da 2 cifre contiene 180 cifre.
3. Totale dei primi due blocchi: `9 + 180 = 189`.
4. Restano `200 - 189 = 11` cifre da contare dentro il blocco dei numeri a 3 cifre.
5. `11 // 3 = 3`, quindi tre numeri completi da 3 cifre precedono quello giusto.
6. Partendo da `100`, il quarto numero è `103`.
7. `11 % 3 = 2`, quindi ci interessa la seconda cifra di `103`.
8. La seconda cifra di `103` è `'0'`.

Risultato: **la 200ª cifra è `0`**.

## Cosa fissare davvero della lezione

Il dettaglio del problema della stringa infinita è meno importante di questi principi generali:

- un programma lungo va diviso in funzioni;
- ogni funzione dovrebbe fare una cosa chiara;
- gli argomenti servono a passare dati dentro la funzione;
- `return` serve a restituire il risultato;
- le variabili locali esistono solo durante l'esecuzione della funzione;
- una buona soluzione non è solo corretta: deve essere anche leggibile e, quando serve, efficiente;
- per risolvere problemi nuovi bisogna scomporli in sottoproblemi semplici.

## Conclusione

Questa è una delle lezioni più importanti del corso fin qui.

Con moduli e funzioni Python smette di essere solo una sequenza di istruzioni una dopo l'altra e diventa un linguaggio con cui organizzare il ragionamento. La parte davvero decisiva non è ricordare ogni dettaglio sintattico, ma imparare a farsi queste domande:

- questo pezzo di codice sta facendo una cosa ben definita?
- lo sto duplicando inutilmente?
- posso trasformarlo in una funzione?
- quali dati deve ricevere?
- quale risultato deve restituire?
- esiste una soluzione più semplice o più efficiente?

Se questa mentalità si consolida adesso, le lezioni successive diventano molto più gestibili.
