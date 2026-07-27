# src/generar_resultados.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

def cargar_resultados():
    """
    Carga los resultados de los modelos
    """
    with open('outputs/results/resultados_modelos.json', 'r', encoding='utf-8') as f:
        resultados = json.load(f)
    return resultados

def generar_tabla_comparativa(resultados):
    """
    Genera tabla comparativa de modelos
    """
    logit = resultados['logit']
    probit = resultados['probit']
    
    datos = {
        'Métrica': ['AIC', 'BIC', 'Pseudo R²', 'AUC'],
        'Logit': [logit['aic'], logit['bic'], logit['pseudo_r2'], logit['auc']],
        'Probit': [probit['aic'], probit['bic'], probit['pseudo_r2'], probit['auc']]
    }
    
    df_tabla = pd.DataFrame(datos)
    
    print("\n" + "="*60)
    print("📊 TABLA COMPARATIVA DE MODELOS")
    print("="*60)
    print(df_tabla.to_string(index=False))
    
    # Guardar como CSV
    df_tabla.to_csv('outputs/tables/comparacion_modelos.csv', index=False)
    print("\n✅ Tabla guardada en outputs/tables/comparacion_modelos.csv")
    
    return df_tabla

def generar_grafico_efectos(efectos):
    """
    Genera gráfico de efectos marginales
    """
    plt.figure(figsize=(12, 8))
    
    # Crear gráfico de barras para efectos marginales
    variables = list(efectos.keys())
    valores = list(efectos.values())
    
    colors = ['#2ecc71' if v < 0 else '#e74c3c' for v in valores]
    
    plt.barh(variables, valores, color=colors, alpha=0.7)
    plt.xlabel('Efecto Marginal Promedio', fontsize=12)
    plt.title('Efectos Marginales de las Variables en la Probabilidad de Informalidad', fontsize=14)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    
    plt.savefig('outputs/figures/efectos_marginales.png', dpi=300, bbox_inches='tight')
    plt.show()

def generar_informe_ejecutivo(resultados):
    """
    Genera un informe ejecutivo en Markdown
    """
    logit = resultados['logit']
    probit = resultados['probit']
    
    informe = f"""
# INFORME EJECUTIVO - ANÁLISIS DE INFORMALIDAD LABORAL EN ECUADOR

## Resumen Ejecutivo
- **Modelo Logit:** AIC = {logit['aic']:.2f}, Pseudo R² = {logit['pseudo_r2']:.4f}
- **Modelo Probit:** AIC = {probit['aic']:.2f}, Pseudo R² = {probit['pseudo_r2']:.4f}
- **Mejor modelo según AIC:** {resultados['comparacion']['mejor_aic']}

## Principales Hallazgos
1. La educación reduce significativamente la probabilidad de informalidad
2. Las mujeres tienen mayor probabilidad de ser informales
3. La ubicación geográfica influye en la informalidad

## Recomendaciones de Política
1. Fortalecer programas de educación y capacitación laboral
2. Implementar políticas de género para reducir brechas
3. Desarrollar estrategias de formalización en zonas rurales
"""
    
    with open('outputs/results/informe_ejecutivo.md', 'w', encoding='utf-8') as f:
        f.write(informe)
    
    print("\n✅ Informe ejecutivo guardado en outputs/results/informe_ejecutivo.md")

if __name__ == "__main__":
    # Cargar resultados
    resultados = cargar_resultados()
    
    # Generar tabla comparativa
    tabla = generar_tabla_comparativa(resultados)
    
    # Generar gráfico de efectos (si tienes los datos)
    # generar_grafico_efectos(efectos)
    
    # Generar informe ejecutivo
    generar_informe_ejecutivo(resultados)