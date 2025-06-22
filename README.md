# psse34parser

Este paquete permite obtener rapidamente una representacion de los archivos `.raw` y `.seq` de la version `34` del PSS\\E

# Estructura de datos RAW
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

Dentro de cada uno de estos diccionarios habra una lista con cada componente, cuyas llaves corresponden al string especificado en el manual (data format). Estos strings van en MAYUSCULAS.

# Estructura de datos SEQ
Los datos estaran estructurados de acuerdo a la especificacion del manual del PSS\\E. Se utilizara un diccionario anidado con las siguientes llaves principales
* GENERATOR
* LOAD
* ZERO SEQ. MUTUAL
* ZERO SEQ. NON-TRANSFORMER BRANCH
* ZERO SEQ. TRANSFORMER
* ZERO SEQ. SWITCHED SHUNT
* ZERO SEQ. FIXED SHUNT
* INDUCTION MACHINE
* NON CONVENTIONAL SOURCE FAULT CONTRIBUTION

# Ejemplo minimo de uso
La lectura de los datos se puede hacer con:

```python
data = psse34parser.read_case("case.raw")
for load in data["LOAD"]:
    print(f"{load["I"]}\t{load["PL"]}")
```

Tambien se puede generar un `DataFrame` de la siguiente manera
```python
data = psse34parser.read_case("case.raw")
generate_dataframe_model(data)
print(data["BUS"].head())
```

# Desarrollo
Dentro del Makefile estan las recetas de `install` y `test` para instalar y correr las pruebas del paquete.
