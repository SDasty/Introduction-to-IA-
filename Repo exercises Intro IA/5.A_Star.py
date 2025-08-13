import heapq  # El módulo heapq para implementar colas de prioridad (heaps)

class Node:  # definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # El estado que define el nodo
        self.parent = parent  # El nodo padre de donde se origina el nodo actual
        self.action = action  # Action tomada desde el padre para llegar al nodo
        self.path_cost = path_cost  # costo desde el nodo raiz (estado inicial), hasta el nodo actual
        self.g = path_cost  # g(n) = costo desde inicio hasta n
        self.h = 0  # h(n) = heurística desde n hasta objetivo
        self.f = 0  # f(n) = g(n) + h(n)

    def __lt__(self, other):  # comparar dos objetos de clase node basado en el costo f
        return self.f < other.f

def expand(problem, node):
    """Expansión del nodo generando sus nodos hijos"""
    s = node.state
    for action in problem.actions(s):
        state_goal = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, state_goal)
        yield Node(state_goal, node, action, cost)

class Problem:  # DEFINICION DEL PROBLEMA
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial  # Estado inicial
        self.goal = goal  # Estado objetivo
        self.actions = actions  # acciones disponibles desde un estado.
        self.result = result  # estado resultante de aplicar una acción
        self.action_cost = action_cost  # costo de una acción
        self.is_goal = is_goal  # verificación de si el estado es el estado objetivo

# Definir el diccionario heuristica ANTES de las funciones que lo usan
heuristica = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

def heuristic(state, goal):
    """Función heurística para tu algoritmo A_Star"""
    return heuristica.get(state, 0)  # Usar .get() para acceder al diccionario

def h(state):
    """Función h para la función f"""
    return heuristica.get(state, 0)  # Usar .get() para acceder al diccionario

def result(state, action):
    return action

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))  # En el caso de que no se encuentre un costo, el valor sera infinito

def is_goal(state, goal):
    return state == goal

def f(node):
    """Función de evaluación A*: f(n) = g(n) + h(n)"""
    return node.f

def A_Star(problem):
    """Algoritmo A* corregido siguiendo el pseudocódigo"""
    
    # Crear nodo inicial
    initial_node = Node(problem.initial)
    initial_node.g = 0
    initial_node.h = heuristic(initial_node.state, problem.goal)
    initial_node.f = initial_node.g + initial_node.h
    
    # Inicialización de las listas abierta y cerrada
    openList = [initial_node]
    closedList = []
    
    while openList:
        # Obtener el nodo con el menor costo f
        current = min(openList, key=lambda node: node.f)
        
        # Si el nodo actual es el objetivo, se retorna el nodo
        if problem.is_goal(current.state):
            return current
        
        # Mover el nodo actual de la lista abierta a la cerrada
        openList.remove(current)
        closedList.append(current)
        
        # Revisar los nodos hijos del nodo actual
        for child in expand(problem, current):
            # Verificar si el hijo ya está en la lista cerrada
            if any(node.state == child.state for node in closedList):
                continue
            
            # Calcular los valores g, h, f para el hijo
            child.g = child.path_cost
            child.h = heuristic(child.state, problem.goal)
            child.f = child.g + child.h
            
            # Verificar si el hijo ya está en la lista abierta
            existing_node = None
            for node in openList:
                if node.state == child.state:
                    existing_node = node
                    break
            
            if existing_node is None:
                # Si no está en openList, añadirlo
                openList.append(child)
            elif child.g < existing_node.g:
                # Si está en openList pero con peor costo, reemplazarlo
                openList.remove(existing_node)
                openList.append(child)
    
    return None  # No se encontró solución

def recover_path(node):
    """Función para recuperar el camino desde el nodo solución"""
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return list(reversed(path))

# Variables del problema
initial = 'Arad'
goal = 'Bucharest'

actions = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Dobreta'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

action_costs = {
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Arad', 'Zerind'): 75,
    ('Sibiu', 'Arad'): 140,
    ('Sibiu', 'Oradea'): 151,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Timisoara', 'Arad'): 118,
    ('Timisoara', 'Lugoj'): 111,
    ('Zerind', 'Arad'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Oradea', 'Zerind'): 71,
    ('Fagaras', 'Sibiu'): 99,
    ('Fagaras', 'Bucharest'): 211,
    ('Rimnicu Vilcea', 'Sibiu'): 80,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Rimnicu Vilcea', 'Craiova'): 146,
    ('Lugoj', 'Timisoara'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Pitesti', 'Rimnicu Vilcea'): 97,
    ('Pitesti', 'Craiova'): 138,
    ('Pitesti', 'Bucharest'): 101,
    ('Craiova', 'Rimnicu Vilcea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Craiova', 'Dobreta'): 120,
    ('Mehadia', 'Lugoj'): 70,
    ('Mehadia', 'Dobreta'): 75,
    ('Bucharest', 'Fagaras'): 211,
    ('Bucharest', 'Pitesti'): 101,
    ('Bucharest', 'Giurgiu'): 90,
    ('Bucharest', 'Urziceni'): 85,
    ('Giurgiu', 'Bucharest'): 90,
    ('Urziceni', 'Bucharest'): 85,
    ('Urziceni', 'Vaslui'): 142,
    ('Urziceni', 'Hirsova'): 98,
    ('Vaslui', 'Urziceni'): 142,
    ('Vaslui', 'Iasi'): 92,
    ('Iasi', 'Vaslui'): 92,
    ('Iasi', 'Neamt'): 87,
    ('Hirsova', 'Urziceni'): 98,
    ('Hirsova', 'Eforie'): 86,
    ('Eforie', 'Hirsova'): 86,
    ('Neamt', 'Iasi'): 87,
    ('Dobreta', 'Craiova'): 120,
    ('Dobreta', 'Mehadia'): 75,
}

# Crear el problema
problem = Problem(
    initial, 
    goal, 
    lambda s: actions.get(s, []), 
    result, 
    action_cost, 
    lambda state: is_goal(state, goal)
)

# Ejecutar A*
solution = A_Star(problem)

if solution:
    path = recover_path(solution)
    total_cost = solution.path_cost
    
    # Mostrar el resultado en el formato solicitado
    print(" -> ".join(path) + f": {total_cost}")
        
else:
    print("No se encontró solución")