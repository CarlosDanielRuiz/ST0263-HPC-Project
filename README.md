# ST0263-HPC-Project

HPC Project for ST0263 - Special Topics in Telematics

## Integrantes

- Mateo Marulanda Cifuentes - mmarulandc@eafit.edu.co (032)
- Carlos Daniel Ruiz Gomez - cruizgo1@eafit.edu.co (031)
- Esteban Sierra Múnera - esierra5@eafit.edu.co (032)

## Documentacion

El documento principal del proyecto se encuentra en [GDrive](https://docs.google.com/document/d/1fPNx0y-jmvhG9NYCfLXodjK0_UfVxWObjdfGKUp8pnE/edit?usp=sharing) y en este [Repositorio](docs/presentacion_proyecto.md)

## Prerequisitos

Para la ejecución del proyecto se debe contar con los siguientes paquetes.

```sh
[Paquetes Python]
biopython
click
```

## Ejecución

1. Clonar el repositorio.
```sh
git clone https://github.com/CarlosDanielRuiz/STO0263-HPC-Project.git
```
2. Creación de un ambiente virtual. Este paso es recomendado 
```sh
python -m venv ambiente_proyecto
```
3. Activación del ambiente virtual.
```sh
source ambiente_proyecto/bin/activate
```
4. Instalar requisitos del programa
```sh
pip install -r requirements.txt
```
5. Descomprimir los archivos FASTA que desee usar
6. Ejecutar bajo el comando
```sh
python paralelo.py -np <cores> -f <archivo.fasta>
```

> Los archivos Fasta se encuentran en el directorio `genomas`. Para más ejemplos, usar los links en el documento de GDrive

## Sustentación en Video
- Mateo Marulanda Cifuentes - [Video](https://www.youtube.com/watch?v=ZNSFG_qY81s&feature=youtu.be)
- Carlos Daniel Ruiz Gomez - [Video](https://www.youtube.com/watch?v=6U8pt2Z7yiY&feature=youtu.be)
- Esteban Sierra Múnera - [Video](https://www.youtube.com/watch?v=gACGts_PtSw)
