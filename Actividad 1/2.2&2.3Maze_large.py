import heapq #El módulo heapq implementa colas de prioridad (heaps)

#####################################

class Node:
    def __init__(self, position, parent=None, path_cost=0, action=None): #AGREGAR ACTION
        self.position = position
        self.parent = parent
        self.path_cost = path_cost
        self.action = action  # COMPLETADO: agregado action

    def __lt__(self, other):
        return self.path_cost < other.path_cost


actions = {
    (-1, 0): "Up",
    (1, 0): "Down", 
    (0, -1): "Left",
    (0, 1): "Right"
}

class Problem:
    #DEFINA la Class problem como lo considere necesario, puede basarse del ejemplo de Bucharest#
    def __init__(self, maze, initial, goal, actions):
        self.maze = maze
        self.initial = initial
        self.goal = goal
        self.actions = actions
    
    def is_goal(self, state):
        return state == self.goal
# LABERINTO GRANDE CON OBSTÁCULOS ESPECIALES

print("LABERINTO GRANDE CON OBSTÁCULOS ESPECIALES")


# Modificar get_neighbors para manejar diferentes tipos de terreno
def get_neighbors_with_terrain(pos, maze, problem_obj):
    neighbors = []
    for move in problem_obj.actions.keys():
        neighbor = (pos[0] + move[0], pos[1] + move[1])
        if (0 <= neighbor[0] < len(maze) and 
            0 <= neighbor[1] < len(maze[0])):
            
            cell = maze[neighbor[0]][neighbor[1]]
            # Permitir movimiento a todos excepto paredes (#)
            if cell != "#":
                # Calcular costo según el terreno
                if cell == "~":  # Agua - más costoso
                    cost = 3
                elif cell == "^":  # Montaña - muy costoso  
                    cost = 5
                else:  # Terreno normal, inicio o salida
                    cost = 1
                
                neighbors.append((neighbor, problem_obj.actions[move], cost))
    return neighbors

def reconstruct_path(node):  #AJUSTAR FUNCIONES PARA ADEMAS DE LAS POSICIONES, MOSTRAR LAS ACCIONES TOMADAS
    path = []
    actions = []
    while node:
        path.append(node.position)
        if node.action:
            actions.append(node.action)
        node = node.parent
    path.reverse()
    actions.reverse()
    return {'path': path, 'actions': actions}

def find_exit_with_terrain(maze):
    start = None
    end = None
    
    # Encontrar S y E 
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return None

    problem = Problem(maze, start, end, actions)

    def manhatan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    start_node = Node(start, path_cost=0)
    frontier = [(manhatan_distance(start, end), start_node)]
    heapq.heapify(frontier)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == end:
            return reconstruct_path(node)

        for neighbor, action, terrain_cost in get_neighbors_with_terrain(node.position, maze, problem):
            new_cost = node.path_cost + terrain_cost  # Usar costo del terreno
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost, action=action)
                heapq.heappush(frontier, (manhatan_distance(neighbor, end), reached[neighbor]))

    return None

# maze grande con diferentes terrenos
large_maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", "~", "~", "#", " ", " ", "^", "^", " ", "#"],
    ["#", " ", "#", "~", "#", "#", " ", "#", "^", " ", " ", "#"],
    ["#", " ", " ", "~", " ", " ", " ", " ", "^", " ", "#", "#"],
    ["#", "#", " ", "~", "~", "~", "#", " ", "^", " ", " ", "#"],
    ["#", " ", " ", " ", " ", "~", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "~", "#", "#", " ", " ", "E", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

print("Reglas:")
print("# = Pared")
print("~ = Agua (costo 3)")  
print("^ = Montaña (costo 5)")
print("  = Terreno normal (costo 1)")
print("S = Inicio, E = Salida")

result_terrain = find_exit_with_terrain(large_maze)
if result_terrain:
    print(f"\nCamino encontrado: {result_terrain['path']}")
    print(f"Acciones: {result_terrain['actions']}")
    print(f"Número de pasos: {len(result_terrain['actions'])}")
else:
    print("No se encontró camino")

