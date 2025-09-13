# XGBoost para predicción de enfermedades cardíacas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, accuracy_score
from xgboost import XGBClassifier, plot_importance

# Reproducibilidad
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Cargar dataset
df = pd.read_csv("heart_disease_dataset.csv")  # cambia al nombre real de tu archivo

print(df.head())
print(df.info())

# Variables predictoras (X) y variable objetivo (y)
X = df.drop("heart_disease", axis=1)
y = df["heart_disease"]

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

# Definir modelo base
xgb = XGBClassifier(
    eval_metric="logloss",
    random_state=RANDOM_STATE
)


# Hiperparámetros para búsqueda en malla
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [3, 5, 7],
    "learning_rate": [0.01, 0.1, 0.2],
    "subsample": [0.8, 1.0],
    "colsample_bytree": [0.8, 1.0]
}

# Grid Search con validación cruzada
grid = GridSearchCV(
    estimator=xgb,
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    verbose=1,
    n_jobs=-1
)

grid.fit(X_train, y_train)

print(f"Mejores parámetros: {grid.best_params_}")
best_model = grid.best_estimator_

# Evaluación en test
y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No Enfermo", "Enfermo"], yticklabels=["No Enfermo", "Enfermo"])
plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# AUC-ROC
roc_auc = roc_auc_score(y_test, y_proba)
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1], [0,1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Curva ROC")
plt.legend()
plt.show()

# Importancia de características
plot_importance(best_model, importance_type="gain")
plt.title("Importancia de Características")
plt.show()

# Ejemplo de predicción con un nuevo paciente
nuevo_paciente = pd.DataFrame([{
    "age": 50, "sex": 1, "cp": 2, "trestbps": 130, "chol": 250,
    "fbs": 0, "restecg": 1, "thalach": 150, "exang": 0, "oldpeak": 2.3,
    "slope": 2, "ca": 0, "thal": 3, "smoking": 1, "diabetes": 0, "bmi": 27.5
}])

prediccion = best_model.predict(nuevo_paciente)[0]
probabilidad = best_model.predict_proba(nuevo_paciente)[0][1]

print("\nNuevo paciente -> Diagnóstico:")
print(f"Clase predicha: {'Enfermo' if prediccion==1 else 'No Enfermo'}")
print(f"Probabilidad de enfermedad: {probabilidad:.2%}")
