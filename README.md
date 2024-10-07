# Generador de Índice de Documentación

Este script en Python genera un índice de documentación en formato Markdown para todos los archivos `.md` en un directorio especificado. El índice incluye enlaces a los archivos y la fecha de creación de cada uno.

## Cómo funciona

El script recorre recursivamente el directorio especificado y sus subdirectorios, buscando archivos con la extensión `.md`. Para cada archivo encontrado, se añade una entrada en el índice con un enlace al archivo y la fecha de creación.

### Funciones principales

- `generate_index(directory)`: Esta es la función principal que genera el índice de documentación.
  - `directory`: El directorio raíz desde el cual se generará el índice.

### Pasos del script

1. **Inicialización del contenido del índice**: Se crea una cadena inicial para el contenido del índice con un título.
2. **Recorrido del directorio**: Se utiliza `os.walk` para recorrer recursivamente el directorio especificado.
3. **Procesamiento de archivos**: Para cada archivo `.md` encontrado:
   - Se obtiene la ruta relativa del archivo desde el directorio raíz.
   - Se obtiene la fecha y hora de creación del archivo.
   - Se crea un enlace en formato Markdown con la ruta del archivo y la fecha de creación.
4. **Escritura del índice**: El contenido del índice se guarda en un archivo `index.md` en el directorio especificado.

### Ejemplo de uso

Para generar un índice de documentación para el directorio `docs`, simplemente llama a la función `generate_index` con el nombre del directorio:

```python
generate_index("docs")
```
### Requisitos

Python 3.x
Módulos estándar de Python: os, time

### Notas

El script solo procesa archivos con la extensión .md.
La fecha de creación del archivo se obtiene utilizando os.path.getctime, que puede variar según el sistema operativo.
