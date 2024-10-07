import os
import time

def generate_index(directory):
    index_content = "# Índice de Documentación\n\n"
    
    for root, dirs, files in os.walk(directory):
        # Obtener la ruta relativa del directorio actual
        relative_root = os.path.relpath(root, directory)
        if relative_root != ".":
            index_content += f"## {relative_root}\n\n"
        
        for file in files:
            if file.endswith(".md"):
                # Obtener la ruta relativa del archivo desde /docs/
                file_path = os.path.relpath(os.path.join(root, file), directory)
                full_path = os.path.join("/docs", file_path)
                # Obtener la fecha y hora de creación del archivo
                creation_time = os.path.getctime(os.path.join(root, file))
                creation_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creation_time))
                # Crear un enlace en markdown con la ruta del archivo y la fecha de creación
                link = f"- {file} - `{full_path}` - Creado el: {creation_time_str}\n"
                # Añadir el enlace al contenido del índice
                index_content += link
        
        if relative_root != ".":
            index_content += "\n"
    
    # Guardar el índice en un archivo markdown
    with open(os.path.join(directory, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)

# Llamar a la función con el directorio 'docs'
generate_index("docs")
