##  XGBoost

XGBoost (**eXtreme Gradient Boosting**) es un algoritmo de *machine learning supervisado* basado en **árboles de decisión**.  
Funciona construyendo muchos árboles pequeños de forma **secuencial**, donde cada nuevo árbol corrige los errores del anterior.  

###  ¿Por qué usarlo aquí?
- Funciona muy bien con **datos tabulares** como este dataset médico.  
- Captura **relaciones complejas y no lineales** entre las variables.  
- Incluye **regularización (L1 y L2)**, lo que ayuda a evitar el sobreajuste.  
- Es robusto frente a **outliers y valores faltantes**.  
- Permite analizar la **importancia de cada variable**, clave en un contexto médico.  

###  Parámetros usados
**Modelo base**:
- `n_estimators = 100` → número de árboles  
- `max_depth = 4` → profundidad de los árboles  
- `learning_rate = 0.1` → velocidad de aprendizaje  
- `objective = "binary:logistic"` → clasificación binaria (enfermedad o no enfermedad)  

**Optimización con GridSearchCV**:  
Los mejores parámetros fueron:
- `n_estimators = 200`  
- `max_depth = 5`  
- `learning_rate = 0.05`  
- `subsample = 0.9`  
- `colsample_bytree = 0.9`  

###  Resultados
- **Modelo base**: Accuracy ≈ 88%  
- **Modelo optimizado**: Accuracy ≈ 90% y ROC-AUC ≈ 0.97  

###  Conclusión
XGBoost fue una excelente elección porque:  
- Es rápido y eficiente.  
- Logró un buen balance entre **precisión** y **recall**.  
- Identifica las variables más importantes para el diagnóstico de enfermedad cardíaca.  
