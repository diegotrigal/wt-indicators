import os

# Lista de carpetas a excluir (especifica aquí los nombres de las carpetas a excluir)
excluir_carpetas = ["lib", "migrations", "__pycache__", ".git"]


def list_directory(path, file, indent=0):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            # Salta las carpetas especificadas en la lista de exclusión
            if os.path.isdir(item_path) and item in excluir_carpetas:
                continue

            # Guarda los directorios y archivos con una estructura de sangría en el archivo
            file.write("    " * indent + "|-- " + item + "\n")

            if os.path.isdir(item_path):
                list_directory(item_path, file, indent + 1)
    except PermissionError:
        # Omite carpetas a las que no se tiene permiso de acceso
        file.write("    " * (indent + 1) + "|-- [Acceso Denegado]\n")


if __name__ == "__main__":
    # Define el nombre del archivo de salida
    output_file = "estructura_directorio.txt"

    with open(output_file, "w") as file:
        # Escribe el directorio raíz en el archivo
        file.write("|-- " + os.path.basename(os.getcwd()) + "\n")
        # Llama a la función para listar el contenido y guardarlo en el archivo
        list_directory(os.getcwd(), file)

    print(f"Estructura del directorio guardada en {output_file}")
