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

## 2.2. Preprocesamiento red neuronal
### a. Limpieza de datos faltantes
Se cargó el dataset y se verificó la ausencia de valores nulos. No se realizaron imputaciones adicionales en este ejemplo.

### b. Codificación de variables categóricas
Se aplicó `OneHotEncoder` a las variables categóricas para convertirlas en representaciones numéricas.

### c. Escalado/normalización
Se aplicó `StandardScaler` a las variables numéricas para normalizar la media y desviación estándar.

### d. División en train/test
Se dividió el dataset en conjuntos de entrenamiento (80%) y prueba (20%) usando `train_test_split`, estratificando por la variable objetivo para mantener la proporción de clases.

# 3. Entrenamiento de los tres modelos con sus parámetros

### 3.1. Entrenamiento del modelo Random Forest

Incluimos el número de árboles necesarios simulando los estimadores de los datos en la clasificación, ya que entre más árboles, más exactitud se podía encontrar. La profundidad máxima y los demás factores que escogimos nos da mucha más exactitud, a la vez que tener la semilla (random_state) nos da la seguridad que tendremos los mismos resultados cada vez que se ejecute el código, y no tendremos variabilidad ni inconsistencia en la exactitud del modelo. Establecemos un mínimo para que no se sobrepasen los datos y se muestren realmente los datos que están en el csv, y no otros no existentes.

### 3.2 Entrenamiento del modelo de red neuronal
Se entrenó un modelo de red neuronal (`MLPClassifier`) usando un pipeline que incluye preprocesamiento:

- **Arquitectura:** Capas ocultas de 128 y 64 neuronas.  
- **Función de activación:** ReLU  
- **Solver:** Adam  
- **Regularización:** `alpha=0.0005`  
- **Tasa de aprendizaje:** Adaptativa  
- **Máximo de iteraciones:** 1000  
- **Detención temprana:** Activada  
- **Pesos de clase:** Balanceados según la distribución de `heart_disease`.

# 4. Evaluación de Resultados

## 4.1. Modelo Random Forest

Usamos para los resultados del modelo las métricas de rendimiento, porque tuvimos mayor detalle de los datos, los datos de importancia según los porcentajes, y mostramos sobre todo la eficiencia base y final después de la optimización que quisimos hacer, y a través de la métrica vimos si pudo optimizarse o no. Analizando la data como archivo csv vimos que es dificil entender sin contexto previo los 0 y 1s que están en la data, sin embargo, al principio de este documento se explica, por lo que la métrica nos hace entender si es mujer u hombre la persona, si tiene o no diabetes, si fuma o no, entre otras.

## 4.2 Modelo Red Neuronal

### a. Métricas de rendimiento
- **Accuracy:** Se imprime el valor de precisión sobre el conjunto de prueba.  
- **Reporte de clasificación:** Incluye precisión, recall y F1-score para cada clase.  

### b. Curvas o visualizaciones
Se generó una matriz de confusión visualizada con `seaborn`:

<img width="600" height="400" alt="Figure_1" src="https://github.com/user-attachments/assets/1637aeea-81f0-4463-8bef-80539f7b7e48" /> 


(Esta visualización muestra la cantidad de predicciones correctas e incorrectas para cada clase.)
## 5. Análisis Comparativo

### Desempeño de los Modelos

#### **MLP (Red Neuronal)**
- **Ventajas:**  
  - Capacidad de aprender patrones complejos y no lineales en los datos.  
  - Maneja bien datasets con interacciones entre múltiples variables.  
  - Permite ajuste fino mediante hiperparámetros y regularización.  
- **Desventajas:**  
  - Requiere mayor tiempo de entrenamiento.  
  - Sensible a la selección de hiperparámetros y al escalado de datos.  
  - Menor interpretabilidad; difícil explicar por qué se toma una decisión específica.  
- **Escenarios de aplicación:**  
  - Predicciones médicas donde se necesitan identificar patrones complejos.  
  - Situaciones donde la exactitud es prioritaria sobre la interpretabilidad.

#### **Random Forest (RF)**
- **Ventajas:**  
  - Robusto ante ruido y outliers en los datos.  
  - Fácil de interpretar mediante la importancia de las características.  
  - Generalmente menos sensible a sobreajuste gracias al promedio de múltiples árboles.  
  - Entrenamiento más rápido que redes neuronales complejas.  
- **Desventajas:**  
  - Puede requerir más memoria para conjuntos de datos muy grandes.  
  - Predicciones menos precisas que una red neuronal si los patrones son muy complejos.  
- **Escenarios de aplicación:**  
  - Diagnóstico médico con énfasis en interpretabilidad y explicación de decisiones.  
  - Problemas donde se necesita una solución confiable sin optimización extensa de hiperparámetros.

#### **Comparación General**
| Modelo | Precisión | Interpretabilidad | Tiempo de Entrenamiento | Robustez |
|--------|-----------|-----------------|------------------------|----------|
| MLP    | Alta      | Baja            | Alto                   | Media    |
| RF     | Media-Alta| Alta            | Medio                  | Alta     |


## 6. Conclusiones
- La red neuronal puede capturar relaciones complejas entre las variables clínicas y demográficas para predecir enfermedad cardíaca.  
- La técnica más adecuada dependerá de la prioridad: si se busca interpretabilidad, Random Forest puede ser más conveniente; si se busca máxima capacidad predictiva, MLP puede ser preferible.  
- El balanceo de clases mediante pesos de muestra ayuda a mejorar el desempeño en datasets desequilibrados.
