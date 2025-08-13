# Ejercicio 3 – Navegación en una Red de Metro

## 📌 Contexto del Problema
La alcaldía de una importante ciudad solicita un sistema que permita a los pasajeros encontrar la **ruta más corta** entre dos estaciones del metro utilizando dos estrategias de búsqueda diferentes:

- **BFS (Breadth-First Search)** → Búsqueda en amplitud.
- **IDS (Iterative Deepening Search)** → Búsqueda con profundización iterativa.

El sistema también debe comparar el **tiempo de ejecución** y la **memoria utilizada** por cada algoritmo.

---

## 🗺 Mapa de la Red de Metro
La red cuenta con 10 estaciones y las conexiones son:

- A ↔ B, C  
- B ↔ A, D, E  
- C ↔ A, F  
- D ↔ B, G  
- E ↔ B, H, I  
- F ↔ C, J  
- G ↔ D  
- H ↔ E  
- I ↔ E, J  
- J ↔ F, I  

Todas las conexiones tienen **el mismo costo**.

---

## 🎯 Definición del Problema
1. **Estado inicial**: Estación donde inicia el pasajero.
2. **Estado objetivo**: Estación a la que desea llegar.
3. **Acciones**: Moverse a cualquier estación conectada directamente.
4. **Espacio de estados**: Todas las combinaciones posibles de estaciones y movimientos.
5. **Modelo de transición**: El estado resultante después de moverse de una estación a otra.

---

## ⚙️ Implementación
El programa está desarrollado en Python e incluye:
- Clase `Node` → Representa un nodo del grafo y reconstruye la ruta.
- Clase `Problem` → Define el estado inicial, objetivo, grafo y acciones.
- Funciones:
  - `breadth_first_graph_search(problem)` → Implementa BFS.
  - `iterative_deepening_search(problem)` → Implementa IDS.
  - `medir_algoritmo(algoritmo, problem)` → Mide tiempo y memoria de ejecución.
  
---

## 🚀 Ejecución
Ejemplo para encontrar la ruta más corta de **A** a **J**:

```bash
BFS
route: ['A', 'C', 'F', 'J']
time : 0.0015168039999480243
peak memory (KB): 4.5078125

IDS
route: ['A', 'C', 'F', 'J']
time: 0.0012667410001085955
peak memory (KB): 0.609375