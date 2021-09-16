# IntegracionArea

El programa principal ``src/Programa.py`` se compone de dos módulos, uno para integrar sobre un área con inecuaciones, y otro para hacer transformaciones de funciones.

## Sobre el primer módulo

Esta es una forma de integrar sobre un área definida, sin necesidad de analizar las inecuaciones para definir los intervalos de las integrales.

Está probado para funciones de dos variables, pero es generalizable para n variables.

Solo es necesario la función y las inecuaciones sobre los que se aplica.

**Advertencia:** No es aplicable en funciones o intervalos complicados (Coordenadas polares, cilíndricas, esféricas, etc.).

## Sobre el segundo módulo

Es una forma de calcular rápidamente las transformaciones por jacobiano de funciones e intervalos complicados.

**Advertencia:** Es necesario agregar datos, para coordenadas polares es necesario agregar algunos intervalos, se explica en el programa ``src/Ejemplos.py``.
