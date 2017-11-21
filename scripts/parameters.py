# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:08:46 2017

@author: user1
"""

from hydpy.models.hland import *
parameterstep('1d')
alpha(2.0)
alpha # Der Parameter wird veranschaulicht
alpha.value # Der simulationsrelevante Wert wird ausgegeben
type(alpha) # Die Parameterklasse wird ausgegeben
alpha(-1.0) # Abgesicherte Änderung
alpha
alpha.value = -1.0 # Nicht abgesicherte Änderung
alpha
alpha.trim() # Nachträgliche Wertekorrektur
alpha
alpha = -1.0 # ACHTUNG: Die Alpha-Instanz wird durch eine Zahl ersetzt
alpha
type(alpha)

# Zeitschrittabhängigkeit (nach Neustart testen)
from hydpy.models.hland import *
parameterstep('1d')
simulationstep('12h')
percmax(2.0)
percmax # Auf die „Parameterschrittweite“ bezogener Wert
percmax.value # Auf die „Simulationsschrittweite“ bezogener Wert
percmax.value = 2.0
percmax
percmax.value
