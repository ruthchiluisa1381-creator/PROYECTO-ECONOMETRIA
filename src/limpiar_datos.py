import os
import numpy as np
import pandas as pd


def procesar_enemdu(
    ruta_entrada='data/raw/enemdu_persona_2025_12.csv',
    ruta_salida='data/processed/enemdu_limpia.csv',
):
    print(f'Cargando datos desde: {ruta_entrada}...')
    df = pd.read_csv(ruta_entrada, low_memory=False)

    # Identificar nombres de columnas en minúsculas
    df.columns = df.columns.str.lower()

    # Mapeo de variables según ENEMDU
    variables_clave = ['secemp', 'p03', 'p02', 'p04', 'area', 'fexp']
    df = df.dropna(subset=variables_clave).copy()

    # Construcción de variables econométricas
    df['informal'] = np.where(df['secemp'] == 2, 1, 0)
    df['anios_educ'] = (
        pd.to_numeric(df.get('p10a', 0), errors='coerce').fillna(0)
    )
    df['edad'] = pd.to_numeric(df['p03'], errors='coerce')
    df['edad_sq'] = df['edad'] ** 2
    df['mujer'] = np.where(df['p02'] == 2, 1, 0)
    df['jefe_hogar'] = np.where(df['p04'] == 1, 1, 0)
    df['rural'] = np.where(df['area'] == 2, 1, 0)
    df['fexp'] = pd.to_numeric(df['fexp'], errors='coerce')

    # Guardar datos limpios en la carpeta processed
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df.to_csv(ruta_salida, index=False)
    print(f' Datos procesados guardados exitosamente en: {ruta_salida}')


if __name__ == '__main__':
    procesar_enemdu()