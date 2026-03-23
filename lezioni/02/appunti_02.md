Le espressioni matematiche seguono la classica gerarchia di priorità, prima ** poi * e \ e poi + e -, andando da sinistra verso destra. Non utilizzeremo altre parentesi poichè in Python hanno significati diversi, utilizzeremo solo parentesti tonde duplicandole alla necessità.

Un esempio potrebbe essere:
print('3 + 14 *5 \ 4 =', 3 + 14 *5 \ 4 )

3 + 14 *5 \ 4 = 20.5

In Python il testo viene chiamato stringa (tipo str)

I testi sono immutabili, non modificabili, possiamo solo crearne nuovi in memoria, il testo va racchiuso tra apici singoli o doppi.
Garbage collection è un processo interno a Python per il riciclo della mempria e la gestione della stessa.

ES di testo:
'Prova prova'
Stamperà sempre in singolo apice, la sintassi è equivalente.

E se dovessimo utilizzare un apostrofo? Scriveremo così 'Io sono un po\' triste' utilizzando il backslash Python riconoscerà il nostro carattere.

Data una stringa possiamo estrarre un suo carattere poiché essi sono tutti numerati secondo un posizionamento che parte da 0 e avanza di 1 per ogni carattere nella stringa.

Per estrarre un carattere dalla nostra stringa faremo così
A = 'Paperino'
A[5]
'i'

Possiamo utilizzare anche due operatori matematici per le nostre stringhe.
ES:
'Paperino' + ' ' + "Minnie"
Ovviamente lo spazio in mezzo è quello che ci servirà per separare le due stringhe.

Possiamo anche ripetere le stringhe moltiplicandole.
ES:
'Minnie' * 5
'MinnieMinnieMinnieMinnieMinnie'

Possiamo spezzare la stringa con un separatore (di default gli spazi) usando il metodo split
A = 'Paperino   andò al mare    con Pippo e \n Minnie'
A.split()
['Paperino', 'andò', 'l', 'mare', 'con', 'Pippo', 'e', 'Minnie']

Passiamo ora ai caratteri particolari
accapo = '\n' #newline
tab = '\t' 
backslash = '\\'
doppio_apice = '\"'
apice = '\''
print('Paperino\nando\'\tal\tmare')

Abbiamo usato un paio di volte le variabili, ad ogni nome dato ad una variabile corrisponderà un pezzo di memoria, nello specifico la posizione in memoria del dato salvato nella variabile. Si chiama variabile poichè il suo contenuto può variare durante l'esecuzione del programma. Quindi alla variabile è associato solo il riferimento all'oggetto, ci sono in pratica due salti.

Una variabile può essere modificata con l'operando di assegnazione '=', la variabile A è unica è il riferimento e l'oggetto che cambia.

Per fare un confronto tra due variabili e capire se sono uguali possiamo utilizzare l'operatore di confronti 'is', ma questo confronto avverrà solo a livello di id, non di contenuto. Con il doppio operatore == invece capiamo similità sul contenuto della variabile.

a =1
b = 1
a is b
true

è consigliato utilizzare sempre nomi di variabili parlanti, esplicative del dato e quello per cui ci serve. 

conversione tra tipi diversi di dati
str(42), str(17.34)
come posso tramutare da stringa ad intero
int('23'), float('23')
(23, 23.0)

mentre se provassi a trasformare in intero 3.5 mi darebbe errore

come leggere un input da tastiera
testo = input("Messaggio che chiede di inserire il dato (prompt)")
nome = input("Ciao come ti chiami?")
print("Mi chiamo", nome)

Come ti chiami? Emiliano
Mi chiamo Emiliano

testo = input("Quanto sei alto?")
altezza = int(testo)
print("Sono alto", altezza, "cm")

Come ottenere la lunghezza di una sequenza di caratteri, utilizziamo la funzione len(nome), quindi come sempre specificando l'oggetto tra parentesi.

Possiamo anche fare slicing della stringa, ci dobbiamo ricordare però che il primo indice è incluso mentre l'ultimo escluso, useremo l'operatore :. E che nello slicing s[start:stop:step], il secondo valore stop non è un carattere da prendere. È il limite di arresto escluso.

ES
a='ciaosonoio'
a[0:4]
ciao

Se invece volessimo sapere la posizione di un carattere possiamo utilizzare find:

ES
a=ciao
a.find('i')
1

In generale possiamo utilizzare anche indici inversi quindi negativi
ES
a=ciao
a[-1]
o
quindi andrà a ritroso partendo dalla fine

Possiamo anche prendere un carattere ogni 2 per esempio, scrivendo così
a = 'ciao sono di Roma'
'ca ood oa'

sempre nell'ambito della gestione delle stringhe possiamo trasformare i caratteri di una stringa in tutti minuscoli attraverso la funzione lower oppure upper
ES
>>> a = 'Ciao Sono IO'
>>> a.lower()
'ciao sono io'

Parliamo ora di String Interpolation

Quando creiamo una nuova variabile prima del cuntenuto scriviamo la lettera f, in questo modo Python riuscirà a capire che è una stringa formattata, e al suo interno potrà avere altre variabili da stampare.

ES
nome = 'Giovanni'
cognome = 'Rossi'
citta = 'Roma'

lettera = f'''
Caro {nome.upper()} {cognome}
La invito a casa mia a {citta}
'''

La funzione print ci resatituirà la lettera completata

Riprendere a videolezione 2 1:56