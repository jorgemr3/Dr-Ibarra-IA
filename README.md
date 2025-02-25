# Descripción 📄

Este repositorio contiene un enfoque alternativo para evaluar la precisión de modelos predictivos, evitando algoritmos tradicionales como K-Nearest Neighbors (KNN). En su lugar, se implementa un método simplificado que:

1. **Selecciona los K casos óptimos por métrica** (Manhattan, Euclidiana, Coseno, etc.).
2. **Calcula la precisión** mediante matrices de confusión generadas al comparar etiquetas reales vs. predicciones basadas en los K seleccionados.

---

## Características clave 🔑

- 🎯 **Métricas implementadas**: Manhattan, Euclidiana, Euclidiana Normalizada, Coseno, Sorensen-Dice, Jaccard.
- 📈 **Selección adaptativa de K**: Optimiza K para cada métrica según la estabilidad de los resultados.
- 📊 **Matrices de confusión**: Diagnóstico detallado de errores por clase y métrica.
- 🧩 **Transparencia total**: Código modular y documentado para ajustes manuales.

---
