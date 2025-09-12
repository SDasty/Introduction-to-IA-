# Actividad 2 - Análisis de Dataset de Enfermedades Cardíacas con SVM

## Descripción del Dataset

Este proyecto utiliza el dataset "Heart Disease Dataset 3k Rows" de Kaggle para implementar un modelo de Support Vector Machine (SVM) que predice la presencia de enfermedades cardíacas.

**Fuente del Dataset:** https://www.kaggle.com/datasets/pratyushpuri/heart-disease-dataset-3k-rows-python-code-2025

## Estructura del Dataset

El dataset contiene las siguientes columnas con sus respectivos significados:

### Variables Categóricas (0 y 1):
- **`sex`**: 
  - 0 = Mujer
  - 1 = Hombre

- **`fbs`** (fasting blood sugar - azúcar en sangre en ayunas):
  - 0 = ≤ 120 mg/dl (normal)
  - 1 = > 120 mg/dl (elevado)

- **`smoking`**:
  - 0 = No fuma
  - 1 = Fuma

- **`diabetes`**:
  - 0 = No tiene diabetes
  - 1 = Tiene diabetes

- **`heart_disease`** (variable objetivo):
  - 0 = No tiene enfermedad cardíaca
  - 1 = Tiene enfermedad cardíaca

### Variables Numéricas:
- **`age`**: Edad del paciente
- **`cp`** (chest pain): Tipo de dolor en el pecho (1-4)
- **`trestbps`**: Presión arterial en reposo
- **`chol`**: Colesterol sérico
- **`restecg`**: Resultados del electrocardiograma en reposo (0-2)
- **`thalach`**: Frecuencia cardíaca máxima alcanzada
- **`exang`**: Angina inducida por ejercicio (0-1)
- **`oldpeak`**: Depresión del ST inducida por ejercicio
- **`slope`**: Pendiente del segmento ST (1-3)
- **`ca`**: Número de vasos principales coloreados (0-3)
- **`thal`**: Resultado del test de esfuerzo (3, 6, 7)
- **`bmi`**: Índice de masa corporal

## Implementación

### Librerías Utilizadas:
- `opendatasets`: Para descargar el dataset de Kaggle
- `pandas`: Para manipulación de datos
- `sklearn`: Para implementar el modelo SVM
- `kagglehub`: Para acceso a datasets de Kaggle

### Proceso:
1. Descarga automática del dataset desde Kaggle
2. Carga del archivo CSV principal (`heart_disease_dataset.csv`)
3. Análisis exploratorio de los datos
4. Preparación de los datos para el modelo
5. Implementación del modelo SVM
6. Evaluación del rendimiento

## Archivos del Proyecto:
- `svm.py`: Script principal con la implementación del modelo
- `heart-disease-dataset-3k-rows-python-code-2025/`: Directorio con los datos descargados
  - `heart_disease_dataset.csv`: Dataset principal
  - `heart_disease_dataset.json`: Datos en formato JSON
  - `heart_disease_dataset.xlsx`: Datos en formato Excel

## Objetivo del Modelo:
Predecir la presencia de enfermedades cardíacas (variable `heart_disease`) basándose en las características clínicas y demográficas del paciente, utilizando un algoritmo de Support Vector Machine.

## Resultados Esperados:
El modelo SVM permitirá clasificar a los pacientes en dos categorías:
- **0**: Sin enfermedad cardíaca
- **1**: Con enfermedad cardíaca

Esto puede ser útil para el diagnóstico temprano y la prevención de enfermedades cardiovasculares.
