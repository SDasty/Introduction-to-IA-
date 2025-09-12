# Actividad 2 - Análisis de Dataset de Enfermedades Cardíacas con Random Forest (RF), Redes Neuronales y Xgboost

## Descripción del Dataset

Este proyecto utiliza el dataset "Heart Disease Dataset 3k Rows" de Kaggle para implementar un modelo de Random Forest (RF) que predice la presencia de enfermedades cardíacas.

**Fuente del Dataset:** https://www.kaggle.com/datasets/pratyushpuri/heart-disease-dataset-3k-rows-python-code-2025

# 1. Estructura del Dataset

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
- `random_forest.py`: Script principal con la implementación del modelo
- `heart-disease-dataset-3k-rows-python-code-2025/`: Directorio con los datos descargados
  - `heart_disease_dataset.csv`: Dataset principal
  - `heart_disease_dataset.json`: Datos en formato JSON
  - `heart_disease_dataset.xlsx`: Datos en formato Excel

## Objetivo del Modelo:
Predecir la presencia de enfermedades cardíacas (variable `heart_disease`) basándose en las características clínicas y demográficas del paciente, utilizando un algoritmo de Random Forest (RF).

## Resultados Esperados:
El modelo RF permitirá clasificar a los pacientes en dos categorías:
- **0**: Sin enfermedad cardíaca
- **1**: Con enfermedad cardíaca

Esto puede ser útil para el diagnóstico temprano y la prevención de enfermedades cardiovasculares.

# 2. Preprocesamiento realizado

## 2.1. Preprocesamiento Random Forest
### Escalado y División de Train/Test

**Escalado:** La técnica nos gustó y nos pareció interesante por la posibilidad de transformar el valor de X, y al estandarizar los datos vimos que la predicción base un poco más alta que la final.

**División de Train/Test:** Decidimos hacer la división train y test, ya que fue el mejor camino que encontramos para que fuese eficiente el modelo, a la par que vimos que el test_size al cambiarlo nos hacía cambiar un poco la exactitud, y al ver que podía cambiar decidimos implementarlo.

# 3. Entrenamiento de los tres modelos con sus parámetros

### 3.1. Entrenamiento del modelo Random Forest

Incluimos el número de árboles necesarios simulando los estimadores de los datos en la clasificación, ya que entre más árboles, más exactitud se podía encontrar. La profundidad máxima y los demás factores que escogimos nos da mucha más exactitud, a la vez que tener la semilla (random_state) nos da la seguridad que tendremos los mismos resultados cada vez que se ejecute el código, y no tendremos variabilidad ni inconsistencia en la exactitud del modelo. Establecemos un mínimo para que no se sobrepasen los datos y se muestren realmente los datos que están en el csv, y no otros no existentes.

# 4. Evaluación de Resultados

## 4.1. Modelo Random Forest

Usamos para los resultados del modelo las métricas de rendimiento, porque tuvimos mayor detalle de los datos, los datos de importancia según los porcentajes, y mostramos sobre todo la eficiencia base y final después de la optimización que quisimos hacer, y a través de la métrica vimos si pudo optimizarse o no. Analizando la data como archivo csv vimos que es dificil entender sin contexto previo los 0 y 1s que están en la data, sin embargo, al principio de este documento se explica, por lo que la métrica nos hace entender si es mujer u hombre la persona, si tiene o no diabetes, si fuma o no, entre otras.
