# Determinantes Socioeconómicos de la Informalidad Laboral en el Ecuador (ENEMDU 2025)

**Autora:** Abigail Chiluisa  
**Materia:** Econometría Aplicada 
**Institución:** Universidad Tecnica de Cotopaxi
**Año:** julio del 2026  

---

## 🔗 Enlaces del Proyecto
* 📊 **Dashboard Interactivo en Vercel:** [https://tu-proyecto.vercel.app](https://tu-proyecto.vercel.app)
* 📄 **Minipaper Académico (PDF):** [Ver PDF en GitHub](paper/CHILUISA_ABIGAIL_PROYECTO_FINAL_ECONOMETRIA.pdf)

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

## 🗄️ 2. Fuente de Datos y Variables

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