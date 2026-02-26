# 📊 Google Play Store Success Prediction

Proyecto de Machine Learning desarrollado para predecir el éxito de aplicaciones en Google Play Store.

---

## 🎯 Objetivo

Construir un modelo de Machine Learning capaz de predecir si una aplicación será exitosa, definiendo éxito como:

> Rating ≥ 4

El modelo recibe características de una app y estima su probabilidad de éxito.

---

## 📁 Dataset

Se utilizó el dataset:

Google Play Store Apps  
Fuente: Kaggle

El dataset incluye información sobre:

- Installs
- Price
- Size
- Category
- Content Rating
- Reviews
- Type (Free/Paid)
- Rating

---

## 🧹 Preprocesamiento y EDA

Se realizaron las siguientes etapas:

- Limpieza de datos
- Conversión de variables numéricas
- Tratamiento de outliers
- Transformaciones logarítmicas para reducir asimetría
- Análisis de correlación
- Análisis de desbalance de clases

Debido a la asimetría en variables como Installs, Price y Size, se aplicó transformación log1p para estabilizar varianza y mejorar el aprendizaje del modelo.

---

## ⚖️ Desbalance de clases

El dataset presenta desbalance moderado entre clases.

Por esta razón, además de Accuracy, se utilizó el **F1 Score** como métrica principal de evaluación, ya que equilibra precisión y recall.

---

## 🤖 Modelos Entrenados

Se entrenaron tres configuraciones:

1. Logistic Regression (modelo base)
2. Random Forest (modelo de ensamble)
3. Random Forest + GridSearchCV (modelo tuneado)

### 📊 Resultados

| Modelo | Accuracy | F1 Score |
|--------|----------|----------|
| Logistic Regression | 0.64 | 0.73 |
| Random Forest | 0.74 | 0.84 |
| Random Forest (Tuned) | 0.75 | 0.84 |

El modelo seleccionado fue **Random Forest tuneado**, por presentar el mejor equilibrio entre precisión y estabilidad.

---

## 🧠 Variables más relevantes

Según el análisis de importancia de variables:

- Size_log
- Installs_log

Son las características más influyentes en la predicción.

---

## 🚀 Despliegue del Modelo

El modelo fue desplegado mediante una API REST construida con Flask.

La API:

- Recibe datos crudos
- Aplica las mismas transformaciones del entrenamiento
- Construye el vector esperado
- Devuelve predicción y probabilidad

### 🔗 Endpoint

POST /predict

Ejemplo de entrada:

```json
{
  "Installs": 5000000,
  "Price": 0,
  "Size_KB": 20000,
  "Category": "GAME",
  "Content_Rating": "Teen",
  "Type": "Free"
}
