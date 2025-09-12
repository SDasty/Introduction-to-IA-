import opendatasets as od
import os
import kagglehub as kh
import pandas as pd
from kagglehub import dataset_load
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

dataset_url = "https://www.kaggle.com/datasets/pratyushpuri/heart-disease-dataset-3k-rows-python-code-2025"
od.download(dataset_url)

df = pd.read_csv("heart-disease-dataset-3k-rows-python-code-2025/heart_disease_dataset.csv")
print(df.head())

print("Dataset cargado: ", df.shape)
print("Columnas: ", df.columns.tolist())
print("Tipos de datos: ", df.dtypes)
print("Valores nulos: ", df.isnull().sum())
print("Valores duplicados: ", df.duplicated().sum())
print("Valores únicos: ", df.nunique())

X = df.drop('heart_disease', axis=1)
y = df['heart_disease']

#División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#Estandarización de los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


#Entrenamiento del modelo
clf = RandomForestClassifier(
    n_estimators=200,        # Numero de arboles
    max_depth=20,            # Profundidad maxima de los arboles
    min_samples_split=2,     # Minimo de muestras para dividir un nodo
    min_samples_leaf=1,      # Minimo de muestras para ser una hoja
    max_features='sqrt',     # Mejora la diversidad
    bootstrap=True,          # Bootstrap sampling
    random_state=42,         # Semilla para reproducibilidad
    class_weight='balanced', # Balance de clases
    n_jobs=-1                # Numero de procesos para el entrenamiento
)

clf.fit(X_train_scaled, y_train)
y_pred = clf.predict(X_test_scaled)
N = y_test.shape[0]
C = (y_test == y_pred).sum()
accuracy_base = accuracy_score(y_test, y_pred)
print(f"Precisión base: {accuracy_base:.4f} ({accuracy_base*100:.1f}%)")

#Optimización de hiperparámetros con GridSearchCV

print("Optimización de hiperparámetros con GridSearchCV")

param_dist = {
    'n_estimators': [50, 100, 150, 200, 250, 300],
    'max_depth': [10, 15, 20, 25, None],
    'min_samples_split': [2, 5, 10, 15],
    'min_samples_leaf': [1, 2, 4, 8],
    'max_features': ['sqrt', 'log2', None]
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42, class_weight='balanced', n_jobs=-1),
    param_dist,
    n_iter=20,  # Solo prueba 20 combinaciones aleatorias
    cv=3,       # Solo 3 folds en lugar de 5
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

print("Entrenando el modelo con los mejores hiperparámetros...")
random_search.fit(X_train_scaled, y_train)

print("Mejores hiperparámetros: ", random_search.best_params_)
print("Mejor precisión: ", random_search.best_score_*100, '%')

#Evaluación del modelo con los mejores hiperparámetros
best_clf = random_search.best_estimator_
y_prediccion_final = best_clf.predict(X_test_scaled)
accuracy_final = accuracy_score(y_test, y_prediccion_final)

print("Precisión final: ", accuracy_final*100, '%')

#Después del entrenamiento, agregar:
cv_scores = cross_val_score(clf, X_train_scaled, y_train, cv=10)
print(f"Validación cruzada: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

#Después del entrenamiento:
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': clf.feature_importances_ * 100
}).sort_values('importance', ascending=False)

print("Top 5 características más importantes:")
for i, row in feature_importance.head().iterrows():
    print(f"{row['feature']}: {row['importance']:.2f}%")






