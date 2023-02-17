# meli-poc-mld-sql-analysis

This repo contains a PoC using SQL linter for sql queries, etls, etc build by a small team.

## Motivación

Con el fin de garantizar un nivel de estandarización suficiente que permita la mantenibilidad de los artefactos, en este caso, consultas que son considerados activos del equipo y facilitar su entendimiento y reutilizar por parte del equipo de Mercado Libre.

Si no se presta atención, es posible que consultas difíciles de entender, mantener o reutilizar pueda llevar al equipo a realizar tareas ya hechas una y otra vez generando un desperdicio general y reduciendo la habilidad del equipo de entregar valor en tiempos adecuados.

Sin embargo, producir reglas de estandarización no es suficiente si el equipo no las adopta y el seguimiento de estas reglas puede ser engorroso por parte de los integrantes quienes están enfocados en producir valor a través de la funcionalidad y la legibilidad pasa a un segundo plano.

Encontrar una forma de garantizar la estandarización sin agregar fricción en el ciclo de desarrollo es de vital importancia para facilitar para un crecimiento sostenido del equipo.

## Método

Para la realización de este análisis se proponen los siguientes pasos:

- Seleccionar una herramienta tipo linter para evaluar automáticamente la calidad de las consultas SQL desarrolladas por el equipo.
  - La herramienta debe ser:
    - Código abierto
    - Capaz de evaluar y sugerir los cambios necesarios para mantener la calidad
    - Integrable en un proceso de pre-commit
- Minar los repositorios del equipo, aislar las consultas SQL.
- Ejecutar el linter seleccionado en el paso 1 e identificar los problemas más frecuentes y si estos son relevantes para garantizar la calidad del código dentro del equipo.
- Realizar una prueba de concepto, integrando el linter seleccionado en el pre-commit de un repositorio.
- Evaluar si es preciso implementar las reglas y definiciones creadas por el equipo.

## Selección del Linter

TODO https://docs.sqlfluff.com/en/stable/gettingstarted.html

## Conjunto de consultas SQL del equipo

TODO https://sourcegraph.furycloud.io/search
Listar todos los repos del equipo

## Problemas más frecuentes

TODO Análisis descriptivo

## PoC Integración Pre-commit

TODO definir pasos para realizar configurar el linter con el precommit e implementación de una regla sencilla.

BigQuery - Nomenclaturas y WoWs

## Conclusión

TODO
