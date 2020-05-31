# kellyvector
Kellyvector è un modulo che ti permette di fare calcoli con i vettori.

#### Introduzione
```python
import vector as v
a = v.Vector([0, 5, 2])
```
Questi semplici comandi ti permettono di importare il modulo e creare un oggetto vettore. In questo caso hi creato un vettore tridimensionale le cui componenti sono: 0, 5, 2. Tuttavia è possibile creare vettori aventi tante dimensioni quante se ne desiderano.

#### Rappresentazione
```python
print (a)
print (repr(a))
```
Il primo comando permette di stampare a schermo le componenti di un vettore, mentre il secondo viene utilizzato per stampare a schermo una stringa che descrive l'oggetto specificando sia la classe a cui appartiene sia le sue componenti

#### Operazioni principali
```python
b = v.Vector([1, 3, 9])
c = a + b	# vettore somma
c = -a		# vettore inverso
c = a - b	# vettore differenza
c = |a|		# modulo del vettore
```
Attenzione !!! Per svolgere qualsiasi operazione i vettori devono avere lo stesso numero di componenti e dunque didimesioni. Qualora questa condizione non venga rispettata il modulo presenterà un errore chiamato: NotSameDegreeError.
