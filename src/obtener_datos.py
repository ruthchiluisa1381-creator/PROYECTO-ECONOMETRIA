# src/obtener_datos.py
import pandas as pd
import os
import zipfile

def cargar_datos_enemdu():
    """
    Carga los datos de la ENEMDU desde el archivo ZIP
    """
    zip_path = 'data/raw/2_BDD_DATOS_ABIERTOS_ENEMDU_2025_12_CSV.zip'
    
    # Verificar que el archivo existe
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"No se encuentra el archivo: {zip_path}")
    
    print("📂 Cargando datos de la ENEMDU 2025...")
    
    try:
        # Leer el archivo CSV dentro del ZIP
        df = pd.read_csv(
            zip_path,
            compression='zip',
            encoding='latin-1',
            low_memory=False
        )
        
        print(f"✅ Datos cargados exitosamente")
        print(f"   - Registros: {df.shape[0]:,}")
        print(f"   - Variables: {df.shape[1]}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")
        return None

def explorar_estructura(df):
    """
    Explora la estructura de los datos
    """
    print("\n" + "="*60)
    print("📊 EXPLORACIÓN INICIAL DE DATOS")
    print("="*60)
    
    # Ver primeras filas
    print("\n📋 Primeras 5 filas:")
    print(df.head())
    
    # Ver nombres de columnas
    print(f"\n📋 Total de columnas: {len(df.columns)}")
    print("Primeras 10 columnas:")
    for i, col in enumerate(df.columns[:10], 1):
        print(f"   {i}. {col}")
    
    # Ver tipos de datos
    print("\n📊 Tipos de datos:")
    print(df.dtypes.value_counts())
    
    # Buscar variables de interés
    print("\n🔍 Variables relacionadas con empleo e informalidad:")
    keywords = ['p69', 'afili', 'seguro', 'ess', 'empleo', 'trabajo', 
                'ocup', 'condic', 'ingreso', 'educ', 'sexo', 'edad']
    
    found = []
    for col in df.columns:
        col_lower = col.lower()
        if any(keyword in col_lower for keyword in keywords):
            found.append(col)
            print(f"   - {col}")
    
    return found

def guardar_muestra(df, n=5000):
    """
    Guarda una muestra para trabajar más rápido
    """
    muestra = df.sample(n=min(n, len(df)), random_state=42)
    muestra.to_csv('data/processed/muestra_enemdu_2025.csv', index=False)
    print(f"\n✅ Muestra de {len(muestra):,} registros guardada en data/processed/")

if __name__ == "__main__":
    # Cargar datos
    df = cargar_datos_enemdu()
    
    if df is not None:
        # Explorar estructura
        variables_interes = explorar_estructura(df)
        
        # Guardar muestra para análisis rápido
        guardar_muestra(df)
        
        # Guardar información de variables en archivo
        with open('data/diccionario_variables.md', 'w', encoding='utf-8') as f:
            f.write("# Diccionario de Variables - ENEMDU 2025\n\n")
            f.write("## Variables de interés para el análisis de informalidad\n\n")
            f.write("| Variable | Descripción | Tipo |\n")
            f.write("|----------|-------------|------|\n")
            
            # Aquí deberás completar con la información del diccionario
            for var in variables_interes[:10]:
                f.write(f"| {var} | Por determinar | Por determinar |\n")
        
        print("\n✅ Diccionario de variables creado en data/diccionario_variables.md")