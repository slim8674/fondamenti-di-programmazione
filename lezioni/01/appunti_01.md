# Lezione 1

## Introduzione

Questa prima lezione è introduttiva e serve a fissare alcuni concetti di base della programmazione in Python.

In Python, come negli altri linguaggi di programmazione, le informazioni vengono memorizzate nella **memoria** del computer.

Per riferirsi a questi dati si usano le **variabili**, cioè nomi associati a valori salvati in memoria.

## Variabili

Una variabile è un nome associato a un valore.

Esempio:

```python
x = 10
nome = "Luca"
```

In questo caso:

- `x` contiene il valore `10`
- `nome` contiene il valore `"Luca"`

Le variabili permettono di lavorare con i dati in modo semplice, senza gestire direttamente la memoria.

## Istruzioni

Le **istruzioni** sono i comandi che indicano al computer quali operazioni compiere.

Un programma è formato da una sequenza di istruzioni eseguite una dopo l’altra.

## Funzioni e procedure

Le **funzioni** sono blocchi di codice riutilizzabili.

In generale:

- una **funzione** restituisce un risultato
- una **procedura** esegue operazioni senza restituire un risultato utile

In Python questa distinzione è soprattutto teorica, ma il concetto è utile.

Esempio di funzione:

```python
type(5)
```

Qui `type()` riceve un valore e restituisce il suo tipo.

## Tipi di dato

Ogni valore in Python appartiene a un certo **tipo di dato**.

Per sapere il tipo di un valore si usa la funzione `type()`.

Esempio:

```python
type(100)
```

Risultato:

```python
int
```

## Tipo `int`

Il tipo `int` rappresenta i **numeri interi**.

Esempi:

```python
10
-3
0
2500
```

È possibile scrivere numeri grandi usando l’underscore `_` per migliorare la leggibilità:

```python
100_000
```

Python interpreta questo valore come:

```python
100000
```

L’underscore non cambia il numero, serve solo a renderlo più leggibile.

Esempio:

```python
type(100_000)
```

Risultato:

```python
int
```

## Richiamo di una funzione

In Python una funzione si richiama scrivendo:

- il nome della funzione
- parentesi tonde
- eventuali argomenti dentro le parentesi

Esempio:

```python
type(10)
```

## Operazioni matematiche

Python supporta le operazioni aritmetiche principali.

### Operazioni base

```python
+
-
*
/
```

Esempi:

```python
3 + 2
10 - 4
5 * 6
8 / 2
```

## Operazioni particolari

### Divisione normale `/`

La divisione normale produce sempre un valore di tipo `float`.

Esempio:

```python
10 / 2
```

Risultato:

```python
5.0
```

### Divisione intera `//`

L’operatore `//` esegue la divisione intera.

Esempio:

```python
10 // 3
```

Risultato:

```python
3
```

Produce un `int` solo se entrambi gli operandi sono `int`.

### Modulo `%`

L’operatore `%` restituisce il resto della divisione intera.

Esempio:

```python
10 % 3
```

Risultato:

```python
1
```

### Potenza `**`

L’operatore `**` calcola la potenza.

Esempio:

```python
2 ** 3
```

Risultato:

```python
8
```

## Altre funzioni matematiche

Altre funzioni matematiche sono disponibili nella libreria `math`.

Esempio di import:

```python
import math
```

Questo argomento verrà approfondito più avanti.

## Tipo `float`

Il tipo `float` rappresenta i numeri decimali.

In Python i numeri decimali si scrivono con il **punto** e non con la virgola.

Esempi:

```python
3.14
0.5
-7.2
```

Verifica del tipo:

```python
type(3.14)
```

Risultato:

```python
float
```

## Osservazioni finali

In questa prima lezione emergono alcune idee fondamentali:

- i dati vengono memorizzati nella memoria
- le variabili servono per riferirsi ai dati
- le istruzioni dicono al computer quali operazioni eseguire
- le funzioni permettono di riutilizzare operazioni
- ogni valore ha un tipo
- Python distingue tra interi (`int`) e numeri decimali (`float`)
- gli operatori aritmetici permettono di eseguire calcoli direttamente nel codice

## Sintesi

Questa lezione introduce i primi elementi del linguaggio:

- memoria e variabili
- istruzioni
- funzioni
- tipo `int`
- tipo `float`
- operazioni matematiche di base

Sono i concetti minimi da conoscere prima di passare a programmi più completi.
