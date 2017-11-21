1
type(1)
1.
type(1.)
1+1.

x = 1.
x
x == 1.
x < 1.
x + 1.
x += 1. # X wird verändert, Ergebnis x=2
x

# Funktionen definieren
def addiere(x, y):
    return x+y # einrücken
addiere 
addiere(1.,1.)
addiere('a','b')
addiere(1. ,'b')# Fehlermeldung: Lösung: str(1.)

# Klassen: beschreiben, welche Attribute und Methoden Objekte (==Instanzen) der Klasse haben
# Definition der Klasse Zahl1 mit Methoden
# 'self' bezieht sich immer auf die aktuelle Instanz der Klasse
# _init_-Methode dient dem Initialisieren einer automatisch erzeugten Klasse
class Zahl1(object):
    def __init__(self, wert): # Methode 'init' weist das Attribut wert zu
        self.wert = wert
    def addiere(self, wert): # Definition einer Methode 'addiere'
        self.wert += wert # addiere bewirkt, dass zu dem wert nochmals der wert addiert wird
Zahl1
x = Zahl1(1.)# erstellt Instanz x der Klasse Zahl1
x
type(x)
x.wert
x.addiere(1.)
x.wert

class Zahl2(Zahl1):
    def subtrahiere(self, wert):
        self.wert -= wert
