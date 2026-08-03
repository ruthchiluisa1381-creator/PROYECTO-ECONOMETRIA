# Determinantes Socioeconómicos de la Informalidad Laboral en el Ecuador (ENEMDU 2025)

**Autora:** Abigail Chiluisa  
**Materia:** Econometría Aplicada 
**Institución:** Universidad Tecnica de Cotopaxi
**Año:** julio del 2026  

---

## 🔗 Enlaces del Proyecto
*  **Dashboard Interactivo en Vercel:** https://proyecto-econometria-e4opdn3re-ruthchiluisa1381-3651s-projects.vercel.app

*  **Minipaper Académico (PDF):**
 [Ver PDF en GitHub](paper/CHILUISA_ABIGAIL_PROYECTO_FINAL_ECONOMETRIA.pdf)
* **link githup** :
https://github.com/ruthchiluisa1381-creator/PROYECTO-ECONOMETRIA.git

---

## 📌 1. Planteamiento del Problema, Pregunta y Objetivos

### Problema
La informalidad laboral en el Ecuador representa una barrera estructural para el desarrollo económico, afectando el acceso a la seguridad social y la estabilidad de los ingresos.

### Pregunta de Investigación
¿Cuáles son los principales determinantes socioeconómicos que inciden en la probabilidad de que un trabajador se encuentre en el sector informal en el Ecuador durante el periodo 2025?

### Objetivo General
Determinar y comparar el impacto de los factores socioeconómicos (educación, edad, género, área de residencia) sobre la probabilidad de pertenecer al sector informal mediante modelos de respuesta binaria.

### Objetivos Específicos
1. Estimar y comparar un modelo Logit y un modelo Probit.
2. Calcular e interpretar los Efectos Marginales Promedio (AME).
3. Evaluar la capacidad predictiva y ajuste de los modelos mediante el criterio AIC y la matriz de confusión.

---
### 2. RESUMEN EJECUTIVO
El presente estudio analiza los determinantes socioeconómicos e individuales de la informalidad laboral en el Ecuador empleando los microdatos oficiales de la Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU) correspondiente a diciembre de 2025. Mediante la estimación de modelos de respuesta binaria de máxima verosimilitud (Logit y Probit), incorporando el factor de expansión poblacional, se evalúa el impacto de la educación, la edad, el género, el rol en el hogar y la ubicación geográfica sobre la probabilidad de pertenecer al sector informal. Los resultados confirman que la acumulación de capital humano reduce de forma estadísticamente significativa la probabilidad de informalidad, mientras que residir en zonas rurales y pertenecer al género femenino incrementan el riesgo de inserción en el mercado informal. El modelo Logit presenta un ajuste ligeramente superior según el Criterio de Información de Akaike (AIC).
Palabras Clave: Informalidad laboral, Modelo Logit, Modelo Probit, Mercado de Trabajo, Ecuador, ENEMDU, Capital Humano.

## 3.INTRODUCCIÓN

La informalidad laboral constituye uno de los desafíos estructurales más persistentes en las economías en desarrollo de América Latina, y en particular en el Ecuador. La precarización del empleo no solo limita el acceso de la población trabajadora a la seguridad social y a condiciones laborales dignas, sino que también reduce la base tributaria del Estado y distorsiona la productividad agregada del país.
El objetivo principal de esta investigación es identificar y cuantificar los determinantes individuales y socioeconómicos que inciden en la probabilidad de que un individuo ocupado se desempeñe dentro del sector informal en el Ecuador. Para cumplir con este propósito, la pregunta central de investigación plantea: ¿En qué medida el nivel educativo, la edad, la condición de género y la localización geográfica condicionan la probabilidad de caer en la informalidad laboral?
La hipótesis central sostiene que mayores niveles de escolaridad y la jefatura del hogar ejercen un efecto protector contra la informalidad, mientras que la condición de ruralidad y la brecha de género agravan la vulnerabilidad laboral.

## 4.REVISIÓN DE LITERATURA

El marco teórico sobre la informalidad laboral abarca diversas visiones. Según la Organización Internacional del Trabajo (OIT, 2023), la informalidad abarca tanto a trabajadores por cuenta propia en unidades productivas no registradas como a asalariados sin protección social legal ni contratos formales.
Estudios recientes de la Comisión Económica para América Latina y el Caribe (CEPAL, 2024) y del Banco Mundial (2023) destacan que los mercados de trabajo latinoamericanos presentan una alta segmentación dual. La teoría clásica del capital humano de Mincer (1974) establece que los individuos invierten en educación y capacitación para incrementar su productividad marginal, lo que reduce la probabilidad de quedar relegados a empleos de baja productividad e informales.
A nivel nacional, investigaciones publicadas por el Banco Central del Ecuador (BCE, 2022) y el Instituto Nacional de Estadística y Censos (INEC, 2024) señalan que más del 50% de la Población Económicamente Activa (PEA) en Ecuador trabaja en el sector informal, siendo la brecha urbano-rural y la disparidad de género factores determinantes en la distribución de la precariedad laboral.

## 5.DATOS Y METODOLOGÍA

La base de datos utilizada proviene de los microdatos abiertos de la ENEMDU (diciembre 2025) recopilados por el INEC. La muestra abarca la población ocupada a nivel nacional con información completa en las variables sociodemográficas y de empleo.

## 5.1.Nombre en Variable
	Tipo		Descripción y Categorización Código
Informalidad (Dependiente)	
Binaria (0/1)	
informal	1 si labora en el Sector Informal (secemp = 2), 0 en otro caso.
Años de Educación	Continua	anios_educ	Años de escolaridad aprobados derivados de p10a.
Edad	Continua	edad	Edad del encuestado en años cumplidos (p03).

Edad al Cuadrado	
Continua	
edad_sq	Captura rendimientos decrecientes/ciclo de vida (edad²).

Mujer	Dicotómica (0/1)	
mujer	
1 si el sexo es femenino (p02 = 2), 0 si es masculino.

Jefe de Hogar	Dicotómica (0/1)	
jefe_hogar	
1 si es el/la jefe/a de hogar (p04 = 1), 0 en otro caso.

Zona Rural	Dicotómica (0/1)	
rural	
1 si reside en el área rural (area = 2), 0 si es urbana.
Factor de Expansión	Ponderador	fexp	Ponderación muestral asignada por el INEC.
## 5.2.Especificación Econométrica
Dado que la variable dependiente Yi = informal es de naturaleza binaria, se formalizan los modelos probabilísticos Logit y Probit expresados como:
P(informali = 1 | Xi) = F(β0 + β1anios_educi + β2edadi + β3edad_sqi + β4mujeri + β5jefe_hogari + β6rurali)
Donde F(·) representa la función de distribución acumulada logística estándar en el modelo Logit:
F(z) = Λ(z) = ez / (1 + ez)
Y en el modelo Probit, F(·) representa la distribución normal estándar acumulada Φ(z):
F(z) = Φ(z) = ∫-∞ (1 / √(2π)) e	dt

## 6.RESULTADOS E INTERPRETACIÓN ECONOMÉTRICA

La estimación de los modelos se realizó aplicando Máxima Verosimilitud con pesos de ponderación poblacional (fexp). A continuación se presentan las estimaciones paramétricas y las métricas de bondad de ajuste.
Tabla 1: Resultados de la Estimación Econométrica (Logit vs. Probit)

Variable Predictora	Modelo Logit (Coeficiente)	Modelo Probit (Coeficiente)	Efectos Marginales Promedio (AME)	Significancia (p-value)
Años de Educación (anios_educ)	
-0.1425	
-0.0861	
-0.0312	
p < 0.001 ***
Edad (edad)	-0.0482	-0.0291	-0.0105	p < 0.001 ***
Edad al Cuadrado (edad_sq)	
0.0006	
0.0003	
0.0001	
p < 0.001 ***
Mujer (mujer)	0.2841	0.1712	0.0621	p < 0.001 ***
Jefe de Hogar (jefe_hogar)	
-0.3105	
-0.1884	
-0.0680	
p < 0.001 ***
Zona Rural (rural)	0.8124	0.4912	0.1775	p < 0.001 ***
Constante (β0)	1.1250	0.68010	--	p < 0.001 ***
Tabla 1: Resultados de la Estimación Econométrica (Logit vs. Probit)
Nota: *** p<0.01, ** p<0.05, * p<0.10. Ponderado por factor de expansión ENEMDU. Criterios de Selección: Logit AIC = 48,120.4; Probit AIC = 48,155.8.
## 6.1.Interpretación de Coeficientes y Efectos Marginales (AME)
•Educación: Cada año adicional de escolaridad reduce la probabilidad de trabajar en el sector informal en aproximadamente 3.12 puntos porcentuales (AME = -0.0312), manteniendo el resto de variables constantes. Esto confirma el rol protector de la inversión en educación.
•Ruralidad: Residir en el área rural incrementa la probabilidad de ser informal en 17.75 puntos porcentuales (AME = 0.1775) respecto a la zona urbana, reflejando la falta de estructura empresarial formal en el campo.
•Género: Las mujeres presentan una probabilidad 6.21 puntos porcentuales mayor de encontrarse en la informalidad que los hombres, evidenciando barreras de acceso al mercado formal.
•Jefatura de Hogar: Ser jefe de hogar reduce la probabilidad de informalidad en 6.80 puntos porcentuales, lo cual se asocia con una mayor búsqueda de empleos formales con cobertura de seguridad social familiar.
•Ciclo de Vida (Edad y Edad²): La edad presenta una relación cuadrática en U invertida con la formalidad; durante la juventud el riesgo de informalidad disminuye con la experiencia laboral, pero a edades avanzadas vuelve a incrementarse.
## 6.2.Interpretación de Coeficientes y Efectos Marginales (AME)
•Educación: Cada año adicional de escolaridad reduce la probabilidad de trabajar en el sector informal en aproximadamente 3.12 puntos porcentuales (AME = -0.0312), manteniendo el resto de variables constantes. Esto confirma el rol protector de la inversión en educación.
•Ruralidad: Residir en el área rural incrementa la probabilidad de ser informal en 17.75 puntos porcentuales (AME = 0.1775) respecto a la zona urbana, reflejando la falta de estructura empresarial formal en el campo.
•Género: Las mujeres presentan una probabilidad 6.21 puntos porcentuales mayor de encontrarse en la informalidad que los hombres, evidenciando barreras de acceso al mercado formal.
•Jefatura de Hogar: Ser jefe de hogar reduce la probabilidad de informalidad en 6.80 puntos porcentuales, lo cual se asocia con una mayor búsqueda de empleos formales con cobertura de seguridad social familiar.
•Ciclo de Vida (Edad y Edad²): La edad presenta una relación cuadrática en U invertida con la formalidad; durante la juventud el riesgo de informalidad disminuye con la experiencia laboral, pero a edades avanzadas vuelve a incrementarse.
## 7.CONCLUSIONES Y LIMITACIONES

Conclusiones:
1.La educación se erige como la herramienta de política pública más efectiva para mitigar la informalidad en el Ecuador. Por cada nivel educativo culminado, las posibilidades de empleo formal aumentan sustancialmente.

2.Existe una brecha geográfica drástica en Ecuador, donde la ruralidad triplica el riesgo relativo de vulnerabilidad informal, demandando incentivos específicos para el desarrollo del sector agroproductivo formal.
3.El modelo Logit presentó el menor valor de AIC/BIC, demostrando ser el modelo con mejor ajuste empírico para esta estructura de microdatos.
Limitaciones:
El estudio presenta limitaciones derivadas de la naturaleza transversal de la ENEMDU, lo cual impide capturar efectos dinámicos o de causalidad en el tiempo. Asimismo, existen variables no observadas como las habilidades blandas y las redes de contactos informales que podrían generar sesgo de variable omitida.
## 8.DECLARACIÓN DEL USO DE INTELIGENCIA ARTIFICIAL
Transparencia e Integridad Académica: En el desarrollo de este trabajo se utilizaron herramientas de Inteligencia Artificial Generativa (ChatGPT / Gemini) exclusivamente como apoyo en la estructuración de código en Python (librerías pandas y statsmodels), corrección de sintaxis en HTML/CSS para la generación del PDF y asistencia en el formato de tablas. Toda la interpretación econométrica, selección de variables, validación estadística y redacción de conclusiones fueron realizadas íntegramente por el autor.
## 🗄️ . Fuente de Datos y Variables

* **Fuente:** Instituto Nacional de Estadística y Censos (INEC) — Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU), Diciembre 2025.
* **Unidad de Observación:** Personas ocupadas de 15 años o más.
* **Variable Dependiente:**
  * `informal`: Variable dicotómica (1 = Sector informal, 0 = Sector formal).
* **Variables Explicativas:**
  * `anios_educ`: Años de escolaridad aprobados.
  * `edad` / `edad_sq`: Edad en años y su término cuadrático.
  * `mujer`: Variable dummy (1 = Mujer, 0 = Hombre).
  * `rural`: Variable dummy (1 = Zona rural, 0 = Zona urbana).

---

## 📉 3. Metodología Econométrica y Resultados

Se aplicaron modelos de respuesta binaria (**Logit** y **Probit**). Tras evaluar los criterios de información, el modelo **Logit** presentó un menor AIC, indicando un mejor ajuste.

### Resumen de Efectos Marginales Promedio (AME - Logit)
* **Educación:** Cada año adicional de educación reduce la probabilidad de informalidad aproximadamente en **3.1%**.
* **Género:** Ser mujer incrementa la probabilidad de trabajo informal en aproximadamente **4.5%**, ceteris paribus.
* **Área:** Residir en el área rural aumenta la probabilidad de informalidad significativamente.

---

## 🛠️ 4. Estructura del Repositorio

```text
proyecto-econometria/
├── data/
│   ├── raw/                  # Datos originales (excluidos por .gitignore)
│   ├── processed/            # Datos limpios para estimación
│   └── diccionario_variables.md
├── notebooks/                # Exploración y pruebas iniciales (.ipynb)
├── src/                      # Código modular en Python
│   ├── obtener_datos.py
│   ├── limpiar_datos.py
│   ├── estimar_modelos.py
│   └── generar_resultados.py
├── outputs/                  # Gráficos, tablas y resultados generados
├── paper/                    # Minipaper final en PDF
├── prompts/                  # Registro transparente de uso de IA
├── requirements.txt          # Dependencias del proyecto
└── README.md
## REFERENCIAS BIBLIOGRÁFICAS 

Banco Central del Ecuador (BCE). (2022). Reporte de empleo y mercado laboral ecuatoriano. Quito, Ecuador.
Comisión Económica para América Latina y el Caribe (CEPAL). (2024). Panorama Social de América Latina y el Caribe: Desafíos del mercado de trabajo. Santiago de Chile.
Instituto Nacional de Estadística y Censos (INEC). (2025). Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU) - Diciembre 2025: Metodología y Tabulados Oficiales. Quito, Ecuador.
Mincer, J. (1974). Schooling, Experience, and Earnings. National Bureau of Economic Research (NBER), New York.
Organización Internacional del Trabajo (OIT). (2023). La informalidad laboral en América Latina y el Caribe: Diagnósticos y políticas . Ginebra