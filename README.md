# Validación Experimental de la Ley de Enfriamiento de Newton

Este proyecto consiste en la validación experimental de la Ley de Enfriamiento de Newton, utilizando el enfriamiento controlado de una barra de aluminio. Se analizaron los datos de temperatura en función del tiempo, tanto en simulaciones como en experimentación real, para comprobar el modelo exponencial que describe el enfriamiento de cuerpos.

## 🔬 Objetivo

Verificar experimentalmente la validez de la Ley de Enfriamiento de Newton mediante la monitorización de la temperatura de una barra de aluminio durante su proceso de enfriamiento natural, utilizando sensores, registro de datos y modelado computacional.

## 📊 Metodología

- Se calienta una barra de acero hasta una temperatura inicial conocida.
- Se permite su enfriamiento en condiciones ambientales controladas.
- Se registra la temperatura a intervalos regulares de tiempo mediante sensores.
- Se ajustan los datos a la forma de la Ley de Enfriamiento de Newton:  
  $$ T(t) = T_{\text{amb}} + (T_0 - T_{\text{amb}})e^{-kt} $$
- Se comparan los datos reales con los resultados de simulación y regresión.

## 📁 Estructura del repositorio

    datos/ # Datos experimentales recogidos
    simulaciones/ # Scripts de simulación (Python, etc.)
    figuras/ # Gráficas de resultados
    informes/ # Anteproyecto y reportes intermedios
    README.md # Este archivo
    requirements.txt # Dependencias del proyecto

## 🛠️ Tecnologías y herramientas

- Python (NumPy, Matplotlib, SciPy)
- Arduino o sistema de adquisición de datos para sensores de temperatura
- Software de procesamiento y análisis de datos (Excel, Python, etc.)

## 📈 Resultados esperados

- Validación del modelo exponencial de enfriamiento.
- Estimación de la constante de enfriamiento `k` para el aluminio.
- Análisis del error entre modelo teórico y datos experimentales.

## 👨‍🔬 Autores

- Juan Pablo Arcila Castañeda, Valeria Giraldo Aristizábal, Ana Sofía Giraldo Villada, Fernando 
Gómez Ferrer & Sara Gutierrez Tobón
- Estudiantes de Física — Universidad EIA