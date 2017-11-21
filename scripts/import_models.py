# Modell importieren (jeweils neu starten, in absteigender Relevanz sortiert)
# Wildcard import in den aktuellen Namespace: 
from hydpy.models.hland import *
print(Model)
# Gezielter import in den aktuellen Namespace: 
from hydpy.models.hland import Model
print(Model)
# Import in einen getrennten Standard-Namespace:
from hydpy.models import hland
print(hland.Model)
# Import in einen getrennten Individual-Namespace:
from hydpy.models import hland as mynamespace
print(mynamespace .Model)
# Import eines Submoduls:
from hydpy.models.hland import hland_model
print(hland_model.Model)