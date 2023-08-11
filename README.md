# psse34parser

Este paquete permite obtener rapidamente una representacion de los archivos `.raw` de la version `34` del PSS\\E

# Estructura de datos
Los datos estaran estructurados de acuerdo a la especificacion del manual del PSS\\E. Se utilizara un diccionario anidado con las siguientes llaves principales
* BUS
* LOAD
* FIXED SHUNT
* GENERATOR
* BRANCH
* SYSTEM SWITCHING
* TRANSFORMER
* AREA
* TWO-TERMINAL
* VSC DC
* IMPEDANCE CORRECTION
* MULTI-TERMINAL
* MULTI-SECTION
* ZONE
* INTER-AREA
* OWNER
* FACTS
* SWITCHED SHUNT
* GNE
* INDUCTION MACHINE
* SUBSTATION

Dentro de cada uno de estos diccionarios habra una lista con cada componente, cuyas llaves corresponden al string especificado en el manual (ver PAGV y POM). Estos strings van en MAYUSCULAS.

# Ejemplo minimo de uso
```python
data = psse34parser.read_case("case.raw")
for load in data["LOAD"]:
    print(f"{load["I"]}\t{load["PL"]}")
```

# Cosas para hacer
[ ] Generar tablas con DataFrames de los componentes
[ ] Posibilidad de pasar el diccionario con la estructura a un objeto 

# Desarrollo
Se utiliza `poetry` para configurar el proyecto.
Para correr las pruebas automaticas se corre el siguiente comando desde la raiz del proyecto
```
poetry run pytest
```