import requests
import os
import pandas as pd

def descargar_pdf(desde_enlaces, hacia_carpeta):
    if not os.path.exists(hacia_carpeta):
        os.makedirs(hacia_carpeta)

    for enlace in desde_enlaces:
        nombre_archivo = enlace.split('/')[-1]
        ruta_archivo = os.path.join(hacia_carpeta, nombre_archivo)

        respuesta = requests.get(enlace)
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
            print(f"Archivo '{nombre_archivo}' descargado correctamente.")

# Lee los enlaces desde el archivo Excel
def leer_enlaces_desde_excel(archivo_excel, nombre_columna):
    datos_excel = pd.read_excel(archivo_excel)
    return datos_excel[nombre_columna].tolist()

# Ruta del archivo Excel que contiene los enlaces
ruta_excel = 'Lista_URLS.xlsx'

# Nombre de la columna que contiene los enlaces en el archivo Excel
nombre_columna = 'Enlaces'

# Carpeta donde guardar los archivos descargados
carpeta_destino = 'C:/Users/USUARIO/Desktop/Pdfs Guardados/Administración de Empresas (En Linea)/Contabilidad General'

# Obtener los enlaces desde el archivo Excel
enlaces_pdf = leer_enlaces_desde_excel(ruta_excel, nombre_columna)

# Descargar los archivos PDF
descargar_pdf(enlaces_pdf, carpeta_destino)
