"""
data_superStore.py

He creado unas funciones de limpieza y normalización del dataset Superstore Sales.

Problemas abordados:
1. Códigos postales nulos (lógica geográfica).

2. Normalización de códigos postales a estándar USPS (5 dígitos).

    2.1 He detectado que el estadnar USPS requiere exactamente 5 dígitos, y algunos códigos en el 
    dataset no cumplen esta regla. Hay zonas en EE.UU donde los "Postal code" contienen un 0 o incluso 2 ceros a la izquierda,
    y al convertirlos a números se pierden esos ceros, lo que genera inconsistencias.


3. Inconsistencias en nombres de producto.

Autor: Alexandru Cristian Stinga Micu
"""

import pandas as pd


def solucionar_postal_codes_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Relleno los códigos postales nulos usando información de Ciudad y Estado.

    :param df: DataFrame original.
    :return: DataFrame con los códigos postales actualizados para ser no nulos.
    """
    df = df.copy()

    df['Postal Code'] = df['Postal Code'].fillna(
        df.groupby(['City', 'State'])['Postal Code'].transform('max')
    )

    # El caso específico conocido es "Burlington, Vermont", del cual sabemos que el código postal correcto es 05401, 
    # pero al convertirlo a número se pierde el cero inicial, quedando 5401.0.
    mask_burlington = (df['City'] == 'Burlington') & (df['State'] == 'Vermont')
    df.loc[mask_burlington, 'Postal Code'] = 5401.0

    return df


def normalizacion_postal_codes_usa(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizo los códigos postales de EE. UU. al estándar USPS (Maximo 5 dígitos). 
    Esto asegura que todos los códigos postales tengan: exactamente 5 dígitos, preservando ceros iniciales.

    Lo que hago es convertir los códigos postales a enteros para eliminar cualquier decimal (.0), luego los convierto a texto y
    uso str.zfill(5) para rellenar con ceros a la izquierda hasta que tengan 5 dígitos.

    Ya que hay codigos postales en EEUU que al convertirlos a texto se quedan con 3 o 4 dígitos y asi sabemos que esos son los cuales tienen uno o dos ceros a la izquierda
    y es importante rellenarlos con ceros a la izquierda para cumplir con el formato USPS y evitar inconsistencias en el análisis posterior.

    Ejecutamos esta funcion despues de "solucionar_postal_codes_nulos" ya que al principio hay códigos postales nulos y debemos solucionar los nulos para evitar errores al convertir a enteros.

    :param df: DataFrame original.
    :return: DataFrame con códigos postales normalizados.
    """
    df = df.copy()

    df['Postal Code'] = (
        df['Postal Code']
        .astype(int)      # Elimino decimales (.0) -> Paso a enteros
        .astype(str)      # Convierto de Entero a texto (Int -> Str)
        .str.zfill(5)     # Relleno con ceros a la izquierda hasta llegar 5 dígitos (Standard USPS) 
    )

    return df


def normalizar_nombres_productos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizo el catálogo de productos asegurando que hay un único nombre por Product ID.

    Asigno a cada Product Id un único nombre de producto, tomando el primer nombre encontrado para cada Product ID. 
    Esto asegura que no haya inconsistencias en los nombres de producto asociados a un mismo ID.

    :param df: DataFrame original.
    :return: DataFrame con nombres consistentes.
    """
    df = df.copy()

    mi_catalogo_actualizado = df.groupby('Product ID')['Product Name'].first()
    df['Product Name'] = df['Product ID'].map(mi_catalogo_actualizado)

    return df


def solucion_super_store_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aqui aplico todas las reglas de limpieza del dataset Superstore que he definido.

    :param df: DataFrame original.
    :return: DataFrame limpio y normalizado.
    """
    df = solucionar_postal_codes_nulos(df)
    df = normalizacion_postal_codes_usa(df)
    df = normalizar_nombres_productos(df)

    return df
