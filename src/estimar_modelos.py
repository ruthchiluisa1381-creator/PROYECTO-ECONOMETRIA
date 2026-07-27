import json
import os
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def estimar_modelos(ruta_datos='data/processed/enemdu_limpia.csv'):
    print('Cargando datos procesados...')
    df = pd.read_csv(ruta_datos)

    formula = (
        'informal ~ anios_educ + edad + edad_sq + mujer + jefe_hogar + rural'
    )

    print('Estimando Modelo Logit...')
    logit_mod = smf.glm(
        formula=formula,
        data=df,
        family=sm.families.Binomial(),
        freq_weights=df['fexp'],
    ).fit()

    print('Estimando Modelo Probit...')
    probit_mod = smf.glm(
        formula=formula,
        data=df,
        family=sm.families.Binomial(link=sm.families.links.Probit()),
        freq_weights=df['fexp'],
    ).fit()

    # Guardar métricas de comparación en outputs/results/
    os.makedirs('outputs/results', exist_ok=True)
    metricas = {
        'logit': {
            'aic': float(logit_mod.aic),
            'bic': float(logit_mod.bic),
            'deviance': float(logit_mod.deviance),
        },
        'probit': {
            'aic': float(probit_mod.aic),
            'bic': float(probit_mod.bic),
            'deviance': float(probit_mod.deviance),
        },
    }

    with open('outputs/results/metricas_modelos.json', 'w') as f:
        json.dump(metricas, f, indent=4)

    print('\n================ RESUMEN LOGIT ================')
    print(logit_mod.summary())

    print(' Resultados y métricas guardados en outputs/results/metricas_modelos.json')


if __name__ == '__main__':
    estimar_modelos()
    # Al ejecutar el script se cargan los datos y se calculan las métricas
     df = cargar_y_limpiar_datos("data/raw/enemdu_persona_2023_12.csv")
    estimar_modelos(df)

    pass
