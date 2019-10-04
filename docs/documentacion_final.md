# Documento Final

## Problema

El problema a realizar es: [Conteo de Nucleótidos de ADN](./propuesta.md)

## Objetivos y Alcances

Una cadena es simplemente una colección ordenada de símbolos seleccionados de algún alfabeto y formados en una palabra; la longitud de una cadena es el número de símbolos que contiene.

Un ejemplo de una cadena de ADN de longitud 21 (cuyo alfabeto contiene los símbolos *A*, *C*, *G* y *T*) es "ATGCTTCAGAAAGGTTCTTACG".

**Dada:** Una cadena de ADN de una longitud máxima de 1000 nt.

**Regresar:** Cuatro números enteros (separados por espacios) contando el número respectivo de veces que los símbolos 'A', 'C', 'G', y 'T' aparecen en s.

### Ejemplo

**Input:**
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

**Output:**
20 12 17 21

## Requerimientos Técnicos

1. Acceso al DCA de la universidad
2. Tener disponibilidad de las máquinas del DCA
    - 192.168.10.40
    - 192.168.10.41
    - 192.168.10.42

## Plan de Trabajo

- Asesoría con estudiantes de maestría de biología e ingeniería de procesos, y diferentes personas de APOLO (incluyendo coordinador, docentes y administradores)

- Utilizar la metodología PCAM para el diseño e implementación del algoritmo serial (el algoritmo serial es de orden O( n ) con n = Longitud de la cadena) y paralelo (utilizando OpenMP y MPI) con ayuda de la biblioteca Biopython por sus facilidades para trabajar problemas de biología computacional.

- Realizar la medición del SpeedUp y Eficiencia con escenarios en serie y paralelo modificando la cantidad de recursos y la longitud de la cadena de ADN (según el microorganismo).

- Realizar la medición del SpeedUp y Eficiencia con cadenas de ADN con similitudes o patrones sobre las cuales se puedan plantear hipótesis de comportamiento y desempeño de los algoritmos.

- Realizar el análisis de las comparaciones y concluir de las ventajas o desventajas de la intervención del paralelismo en los resultado de ejecución.

## Referencias

- http://rosalind.info/problems/dna/
- https://www.ncbi.nlm.nih.gov/nuccore/NC_001416.1?report=fasta
- http://www.plantgdb.org/prj/GenomeBrowser/
