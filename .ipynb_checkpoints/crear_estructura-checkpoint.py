import os

def crear_estructura():
    # Directorios requeridos para el proyecto
    estructura = [
        "mi_proyecto/data/raw",
        "mi_proyecto/data/processed",
        "mi_proyecto/data/external",
        "mi_proyecto/notebooks/exploratorio",
        "mi_proyecto/notebooks/analisis",
        "mi_proyecto/src",
        #"mi_proyecto/output/plots",
        #"mi_proyecto/output/models"
    ]
    
    # Crea las carpetas
    for carpeta in estructura:
        os.makedirs(carpeta, exist_ok=True)

    # Crear archivos vacíos como README.md, .gitignore, etc.
    archivos = [
        "mi_proyecto/README.md",
        "mi_proyecto/.gitignore",
        "mi_proyecto/requirements.txt",
        #"mi_proyecto/environment.yml"
    ]

    for archivo in archivos:
        open(archivo, 'w').close()  # Crea archivos vacíos

    print("Estructura de directorios y archivos creada exitosamente!")

if __name__ == "__main__":
    crear_estructura()
