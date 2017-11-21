# -*- coding: utf-8 -*-

@author: Christine


# Handhabung von Vernetzungen
# Manuelle Erstellung mit Node- und Element-Objekten
from hydpy import Node, Element, Nodes, Elements
gauge1 = Node('gauge1', variable='Q') # Jedem Node eine Variable zuordnen
gauge1
catch1 = Element('catch1 ', outlets=gauge1) # Vernetzung durch Element-Konstruktor
catch1
catch2 = Element('catch2', outlets='gauge2') # Abkürzungen sind erlaubt
catch2
stream = Element('stream', inlets=gauge1, outlets='gauge2') #  Zu- und Abfluss
stream
branch = Element('branch', inlets='gauge2', outlets=Nodes('gauge30', 'gauge31'))
branch # Verzweigung
branch.inlets.gauge2.entries.stream.inlets.gauge1.entries.catch1 # „network-walk“

# Laden von Vernetzungen aus network-Dateien
#1. Öffnen Sie die Netzwerk-Datei examples\network\rheinHBV\rhein.py
#2. Drücken Sie F5

#Laden, Erstellen und Speichern von Netzwerk-Selections
from hydpy import HydPy, pub
hp = HydPy('rheinHBV') # Vorbereitung des operationellen HBV-Modells
hp.preparenetwork() # Laden der Netzwerk-Datei
hp.elements # die „aktiven“ Elemente
hp.nodes # die „aktiven“ Nodes
hp.network_properties # Einen ersten Überblick gewinnen
pub.selections.rhein.elements # aktuell identisch mit den „aktiven“ Elementen
pub.selections.rhein.nodes # aktuell identisch mit den „aktiven“ Nodes
anyname = pub.selections.rhein.copy('neckar') # flache Kopie von selection anlegen
pub.selections += anyname  # selection zu selections hinzufügen
anyname.select_upstream(hp.elements.stream_neckar5_uprhine2) # Neckar-Auswahl
pub.selections.neckar.nodes += hp.nodes.neckar50 # Der Neckar-Endnode hinzufügen
pub.selections.neckar.nodes += hp.nodes.uprhine4 # Die Rhein-Mündung hinzufügen
anyname.copy('neckar_land').select_elementnames('land') # Nur „Land-Elemente“
pub.networkmanager.save(pub.selections) # Selection sichern
pub.networkmanager.dirpath # Hier werden Network-Dateien aktuell gespeichert
pub.networkmanager.filenames # So heißen die aktuellen Network-Dateien
hp.updatedevices(pub.selections.neckar) # Die Neckar-Auswahl aktivieren
hp.networkproperties # Ist die Neckar-Auswahl plausibel?
hp.updatedevices(pub.selections.rhein) # Auswahl zurücksetzen
#Dritte Iterationsübung (für alle Elemente anzeigen, in welche(n) Node(s) diese entwässern)
for (name1, element) in hp.elements:
    for (name2, node) in element.outlets:
        print(name1, ‚: ‚ name2,)
    print(‘ ‘)