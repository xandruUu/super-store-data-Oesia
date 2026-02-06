# Superstore Data Quality Project

## Descripción
Este proyecto consiste en la resolución de un reto técnico enfocado en la calidad de datos y normalización de un dataset de ventas minoristas (**Superstore Sales Dataset**). 

He implementado un flujo de trabajo profesional que integra **VS Code**, **GitHub** y **Google Colab** para transformar datos inconsistentes en información fiable para el análisis de negocio.

## Estructura del Repositorio
El proyecto está organizado siguiendo una estructura modular para facilitar la reproducibilidad y el mantenimiento:

* **`data/raw/`**: Contiene el dataset original `train.csv` sin procesar.
* **`data/processed/`**: Directorio destinado a los datos tras la aplicación de limpieza.
* **`src/`**: Scripts de Python (`data_superstore.py`) que contienen la lógica de negocio y funciones de normalización.
* **`notebooks/`**: Cuaderno interactivo (`superStoreDataOesia.ipynb`) para el análisis exploratorio y validación.
* **`docs/`**: Documentación complementaria del análisis del problema.
* **`requirements.txt`**: Librerías necesarias para ejecutar el proyecto.

## Problemas de Calidad Identificados
Mediante un análisis exploratorio (EDA), se han detectado tres problemas críticos:

1.  **Códigos Postales Nulos**: Registros vacíos en el campo `Postal Code` correspondientes a la ciudad de **Burlington, Vermont**.

2.  **Estandarización de ZIP Codes**: Los códigos postales almacenados como números pierden sus ceros iniciales (especialmente en el Noreste de EE. UU.), lo que provoca códigos de 3 o 4 dígitos en lugar de los 5 como marca el estandar USPS.

3.  **Inconsistencias en Productos**: Registros donde un mismo `Product ID` está asociado a múltiples nombres.

## Solución Implementada
Se ha desarrollado la función `solucion_super_store_data` que automatiza las siguientes tareas:

* **Imputación Geográfica**: Relleno de códigos postales nulos utilizando la información de Ciudad y Estado como referencia.
* **Normalización de Formato**: Aplicación de *padding* a 5 dígitos para asegurar que todos los códigos postales cumplan con el estándar de 5 caracteres.
* **Unificación de Catálogo**: Asignación de un único nombre por `Product ID` basándose en la primera ocurrencia, garantizando una relación 1:1 y un análisis de ventas limpio.

## Tecnologías
* **Lenguaje**: Python 3.x
* **Librerías**: Pandas (procesamiento de datos), Matplotlib (visualización).
* **Herramientas**: Google Colab (Análisis), VS Code (Desarrollo), GitHub (Control de versiones).

## Guía de Ejecución en Google Colab
Para ejecutar este proyecto en la nube, siga estos pasos:

1.  **Clonar el repositorio**:
    ```python
    !git clone [https://github.com/xandruUu/super-store-data-Oesia.git](https://github.com/xandruUu/super-store-data-Oesia.git)
    %cd super-store-data-Oesia/
    ```

2.  **Configurar el entorno e importar la solución**:
    ```python
    import sys
    sys.path.append('/content/super-store-data-Oesia')
    from src.data_superstore import solucion_super_store_data
    ```

3.  **Procesar los datos**:
    ```python
    import pandas as pd
    df = pd.read_csv('data/raw/train.csv')
    df_clean = solucion_super_store_data(df)
    ```

---
**Autor:** Alexandru Cristian Stinga Micu