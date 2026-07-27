# Diccionario de Variables - ENEMDU (INEC)

| Variable | Nombre ENEMDU | Tipo Econométrico | Descripción |
| :--- | :--- | :--- | :--- |
| `informal` | `secemp` | Dependiente (Binaria) | **1** = Empleo informal, **0** = Empleo formal |
| `anios_educ` | `p10a` / `p10b` | Explicativa (Continua) | Años de escolaridad aprobados |
| `edad` | `p03` | Explicativa (Continua) | Edad en años cumplidos (>= 15) |
| `edad_sq` | Construida | Explicativa (Continua) | Edad al cuadrado (Proxy de experiencia laboral) |
| `mujer` | `p02` | Explicativa (Dicotómica) | **1** = Mujer, **0** = Hombre |
| `jefe_hogar` | `p04` | Explicativa (Dicotómica) | **1** = Jefe/a de hogar, **0** = Otro miembro |
| `rural` | `area` | Explicativa (Dicotómica) | **1** = Área Rural, **0** = Área Urbana |
| `fexp` | `fexp` | Ponderador / Muestral | Factor de expansión oficial del INEC |

# Diccionario de Variables - ENEMDU Diciembre 2025

| Variable | Nombre en Dataset | Descripción | Categorización / Tipo |
| :--- | :--- | :--- | :--- |
| **Informalidad** | `informal` | Condición de ocupación en el sector informal | 1 = Sector Informal (`secemp == 2`), 0 = Sector Formal/Otro |
| **Educación** | `anios_educ` | Años de escolaridad aprobados | Continua (0 a 22 años) derivados de `p10a` |
| **Edad** | `edad` | Edad del encuestado en años cumplidos | Continua (`p03`) |
| **Edad al Cuadrado** | `edad_sq` | Término cuadrático para ciclo de vida | Continua (`edad^2`) |
| **Género** | `mujer` | Sexo del encuestado | 1 = Mujer (`p02 == 2`), 0 = Hombre (`p02 == 1`) |
| **Jefe de Hogar** | `jefe_hogar` | Parentesco en el hogar | 1 = Jefe/a de hogar (`p04 == 1`), 0 = Otro integrante |
| **Zona** | `rural` | Dominio geográfico | 1 = Área Rural (`area == 2`), 0 = Área Urbana (`area == 1`) |
| **Ponderador** | `fexp` | Factor de expansión poblacional | Ponderador de muestreo representativo nacional |