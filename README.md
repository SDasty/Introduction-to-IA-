# Introduction-to-IA-
### hello this is our repository

# Enunciado del Punto 1

### A partir del Notebook "2.BestFirstSearch.ipynb" de la semana 2, resolver el problema que soluciona la ruta óptima hasta Bucharest, mediante el algoritmo de A*Search usando la heurística.

## Análisis del Problema
### Descripción del Problema
El problema consiste en encontrar la ruta más corta desde la ciudad de Arad hasta Bucharest en Romania, utilizando un mapa con 20 ciudades interconectadas. Este es un problema clásico de búsqueda de caminos en inteligencia artificial.

### Modelado como Grafo
- Estados: Las ciudades de Romania (Arad, Sibiu, Timisoara, etc.).
- Estado Inicial: Arad.
- Estado Objetivo: Bucharest.
- Acciones: Moverse de una ciudad a otra ciudad directamente conectada.
- Función de Costo: Distancia real en kilómetros entre ciudades conectadas.
- Función Heurística: Distancia en línea recta desde cada ciudad hasta Bucharest.

## Características del Espacio de Búsqueda
Espacio de estados finito: 20 ciudades
Grafo no dirigido: Se puede viajar en ambas direcciones entre ciudades conectadas
Costos positivos: Todas las distancias son valores positivos
Heurística admisible: La distancia en línea recta nunca sobrestima la distancia real

## Cómo se Aplica A*
### Funcionamiento del Algoritmo A*
A* es un algoritmo de búsqueda informada que utiliza tanto el costo real acumulado como una estimación heurística para guiar la búsqueda hacia la solución óptima. En nuestro código, A* se implementa siguiendo estos principios fundamentales:

Función de Evaluación
La función de evaluación de A* es:

f(n) = g(n) + h(n)
Donde:

- g(n): Costo real del camino desde el estado inicial hasta el nodo n (implementado como node.path_cost).
- h(n): Estimación heurística del costo desde n hasta el objetivo (función heuristic()).
- f(n): Estimación del costo total del mejor camino que pasa por n.

## Implementación del Algoritmo en el Código

### 1. Inicialización


initial_node = Node(problem.initial)
initial_node.g = 0
initial_node.h = heuristic(initial_node.state, problem.goal)
initial_node.f = initial_node.g + initial_node.h
openList = [initial_node]
closedList = []

### 2. Bucle Principal del Algoritmo

while openList:
    current = min(openList, key=lambda node: node.f)  # Selección por menor f
    if problem.is_goal(current.state):               # Verificación de objetivo
        return current
    openList.remove(current)                         # Mover a lista cerrada
    closedList.append(current)
    
### 3. Expansión y Evaluación de Sucesores

for child in expand(problem, current):
    child.g = child.path_cost
    child.h = heuristic(child.state, problem.goal)
    child.f = child.g + child.h

## Heurística Utilizada
Se utiliza la distancia en línea recta desde cada ciudad hasta Bucharest, implementada en el diccionario heuristica:

heuristica = {
    'Arad': 366,
    'Sibiu': 253,  
    'Pitesti': 100,
    'Bucharest': 0,
    # ... resto de ciudades
}

Esta heurística es admisible porque la distancia en línea recta nunca puede ser mayor que la distancia real por carretera.

### Estructura de Datos
- openList: Lista de nodos por evaluar (frontera).
- closedList: Lista de nodos ya evaluados.
- Node: Clase que contiene estado, padre, costo del camino, y valores g, h, f.

## ¿Por qué se Considera que la Ruta Encontrada es Óptima?
### Propiedades que Garantizan la Optimalidad

### 1. Heurística Admisible
La heurística utilizada (distancia en línea recta) es admisible porque:

- Nunca sobrestima el costo real hasta el objetivo.
- Para cualquier ciudad, la distancia en línea recta ≤ distancia real por carretera.
- h(Bucharest) = 0, lo cual es exacto.

### 2. Heurística Consistente (Monótona)
La heurística también es consistente, lo que significa:

- Para cualquier nodo n y sucesor n': h(n) ≤ costo(n,n') + h(n').
- Esto garantiza que los valores f nunca disminuyan a lo largo de cualquier camino.

### 3. Teorema de Optimalidad de A*
Cuando la heurística es admisible y consistente, A* garantiza encontrar la solución óptima porque:

- Nunca expande un nodo cuyo valor f sea mayor al costo de la solución óptima.
- Siempre explora primero los caminos más prometedores.
- No puede terminar en una solución subóptima debido a las propiedades de la heurística.

## Resultado Esperado
Con los datos proporcionados, la ruta óptima de Arad a Bucharest es: Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest.

Con un costo total de: 140 + 80 + 97 + 101 = 418 km.


# Punto 2
## Problemas identificados

### 1. HEURÍSTICA INADECUADA
- La distancia Manhattan no considera los costos reales del terreno.
- Puede subestimar el costo real en terrenos complejos.
- Ejemplo: un camino directo a través de montañas puede parecer mejor, pero ser mucho más costoso que un rodeo por terreno normal.

### 2. EXPLORACIÓN INEFICIENTE
- El algoritmo puede explorar caminos caros innecesariamente.
- No hay memoria de terrenos ya evaluados con costos altos.

### 3. ESCALABILIDAD
- En laberintos grandes (como el de 12x9), el tiempo aumenta significativamente.
- La memoria usada crece con el número de posiciones alcanzables.

### 4. MÚLTIPLES SALIDAS
- El algoritmo original solo encuentra **una** salida.
- Para múltiples salidas, hay que ejecutar el algoritmo varias veces.
- No hay optimización para encontrar la mejor salida de forma eficiente.

---

##  Propuestas de mejora
- Implementar heurísticas más sofisticadas que consideren tipos de terreno.
- Usar algoritmos bidireccionales para múltiples salidas.
- Implementar poda más agresiva para reducir el espacio de búsqueda.
