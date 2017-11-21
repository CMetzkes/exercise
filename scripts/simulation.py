# -*- coding: utf-8 -*-
"""

@author: Christine
""" 
#Modelle vorbereiten zur ersten Simulation
from hydpy import *
hp = HydPy('rheinHBV')
hp.preparenetwork()
pub.controlmanager.controlpath # Wird der Pfad der Control-Dateien automatisch erkannt?
hp.initmodels() # Dann können die Modelle für den gesamten Rhein initialisiert werden!
hp.elements.hland_neckar1.model.parameters.control.fc
pub.conditionmanager.conditionpath # Wird der Pfad der Condition-Dateien automatisch erkannt?
hp.loadconditions() # Dann können die Anfangszustände für den gesamten Rhein geladen werden!
hp.elements.hland_neckar1.model.sequences.states.lz
pub.sequencemanager.inputpath # Wird der Pfad der Modell-Eingabe-Zeitreihen automatisch erkannt?
pub.sequencemanager.inputdirectory = 'SMHI2006' # Dann erst denn gewünschten Ordner auswählen…
pub.sequencemanager.inputpath # …den Pfad noch einmal prüfen,… 
hp.prepare_inputseries() # …und die Eingangsdaten einlesen!
hp.elements.hland_neckar1.model.sequences.inputs.t.series
pub.sequencemanager.outputpath # Wird der Pfad der Modell-Ausgabe-Zeitreihen automatisch erkannt?
hp.prepare_stateseries() # …dann können die Zustands-Zeitreihen der späteren Analyse zugänglich gemacht werden!
hp.elements.hland_neckar1.model.sequences.states.lz.series
pub. sequencemanager.nodepath # Wird der Pfad der Node-Zeitreihen automatisch erkannt?
hp.prepare_nodeseries() # Dann können die gemessenen Ganglinien eingelesen und die zu simulierenden vorbereitet werden!
hp.nodes.neckar1.sequences.obs.series


# Durchführung der ersten Simulation und graphische Ausgabe der Ergebnisse
hp.doit() # Interne Vorbereitungen und Simulation über den gesamten Zeitraum.
pub.timegrids.init # Über welchen Zeitraum wurde eigentlich initialisiert und simuliert?
hp.nodes.lowerrhine4.comparisonplot() # Vergleichsgraphik für den letzten Rheinpegel
hp.nodes.lippe3.comparisonplot() # …und den letzten Zuflusspegel davor.
# Sollen die Graphiken (nicht) zusammengefasst werden? Dann schalten sie den interaktiven Modus von matplotlib…
from matplotlib import pyplot
pyplot.ion() # …ein,…
pyplot.ioff() # …oder aus.
# Vergleich des Verlaufes der oberen und der unteren Grundwasserspeicherung…
hp.elements.land_vierwas.stateplot('uz', 'lz') # …da wo es viele Urlaub machen…
hp.elements.land_emscher.stateplot('uz', 'lz') # …und da wo es wirklich schön ist!
# Vergleich des Wellenablaufes innerhalb zweier streams hinter einem branch für das Haupt- und Nebengerinne mit manuellen Grafikoptionen:
es = hp.elements
es.stream_lowrhine20_lowrhine3.stateplot('qjoints', color='blue', linestyle='--') 
es.stream_lowrhine21_lowrhine3.stateplot('qjoints ', color='red', linestyle=':'))
Speichern der Simulationsergebnisse
hp.saveconditions() # Speichern der finalen Systemzustände (ToDo: Ordnererstellung)
pub.sequencemanager.nodedirectory = ‘test‘ # Damit die gemessenen Werte im Ordner „node“ nicht überschrieben werden
hp.save_nodeseries() # Speichere alle Daten im effizienten numpy-Binärformat
pub.sequencemanager.nodefiletype = ‘txt‘ # Und im txt-Format?
pub.sequencemanager.nodefiletype = ‘asc‘ # Und im lesbaren asc-Format!:
hp.save_nodeseries() 
# Das Ausschreiben aller state sequences kann etwas dauern – insbesondere im asc-Format: bitte selber ausprobieren