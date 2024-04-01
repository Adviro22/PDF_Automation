import os
import pandas as pd
import requests

def descargar_pdf(enlace, nombre_archivo, carpeta_destino):
    # Verificar si la carpeta destino existe, si no, crearla
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Si el archivo ya existe en la carpeta destino, ajustar el nombre
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    nombre_base, extension = os.path.splitext(nombre_archivo)
    contador = 1
    while os.path.exists(ruta_archivo):
        nombre_archivo = f"{nombre_base}_{contador}{extension}"
        ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
        contador += 1

    # Descargar el PDF desde el enlace proporcionado
    respuesta = requests.get(enlace)
    with open(ruta_archivo, 'wb') as archivo:
        archivo.write(respuesta.content)
        print(f"Archivo '{nombre_archivo}' descargado correctamente.")

def organizar_descargas(desde_archivo_excel, carpeta_base):
    # Leer el archivo Excel
    datos_excel = pd.read_excel(desde_archivo_excel)

    # Iterar sobre cada fila del DataFrame
    for indice, fila in datos_excel.iterrows():
        carrera = fila['carrera']
        paralelo = fila['paralelo']
        enlace = fila['link']
        materia = fila['asignatura']
        
        # Crear la carpeta de la carrera si no existe
        carpeta_carrera = os.path.join(carpeta_base, carrera)
        if not os.path.exists(carpeta_carrera):
            os.makedirs(carpeta_carrera)

        # Crear la carpeta del paralelo si no existe
        carpeta_paralelo = os.path.join(carpeta_carrera, paralelo)
        if not os.path.exists(carpeta_paralelo):
            os.makedirs(carpeta_paralelo)

        # Nombre original del archivo
        nombre_archivo = f"{materia}.pdf"

        # Descargar el PDF en la carpeta del paralelo con el nombre de la materia
        descargar_pdf(enlace, nombre_archivo, carpeta_paralelo)

# Definir la ruta del archivo Excel y la carpeta base
archivo_excel = './excel/Listado de PDFS.xlsx'
carpeta_base = './pdf'

# Llamar a la función para organizar las descargas
organizar_descargas(archivo_excel, carpeta_base)
