import heapq #El módulo heapq implementa colas de prioridad (heaps)

#####################################

class Node:
    def __init__(self, position, parent=None, path_cost=0, action=None): #AGREGAR ACTION
        self.position = position
        self.parent = parent
        self.path_cost = path_cost
        self.action = action  

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

##########################################

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


##############################################



def find_all_exits(maze):
    """Encuentra todas las posiciones marcadas como 'E'"""
    exits = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'E':
                exits.append((i, j))
    return exits

def find_best_exit(maze):
    """Encuentra la mejor salida entre múltiples opciones"""
    start = (1, 1)  # Posición de S
    exits = find_all_exits(maze)
    
    if not exits:
        return None, "No hay salidas"
    
    best_result = None
    best_cost = float('inf')
    best_exit = None
    
    print(f"Salidas encontradas: {exits}")
    
    for i, exit_pos in enumerate(exits):
        print(f"\nProbando salida {i+1}: {exit_pos}")
        
        # Crear problema específico para esta salida
        problem_temp = Problem(maze, start, exit_pos, actions)
        
        # Modificar temporalmente find_exit para esta salida específica
        def manhatan_distance(pos, goal):
            return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

        def get_neighbors(pos):
            neighbors = []
            for move in problem_temp.actions.keys():
                neighbor = (pos[0] + move[0], pos[1] + move[1])
                if (0 <= neighbor[0] < len(maze) and 
                    0 <= neighbor[1] < len(maze[0]) and 
                    maze[neighbor[0]][neighbor[1]] != "#"):
                    neighbors.append((neighbor, problem_temp.actions[move]))
            return neighbors

        start_node = Node(start, path_cost=0)
        frontier = [(manhatan_distance(start, exit_pos), start_node)]
        heapq.heapify(frontier)
        reached = {start: start_node}

        while frontier:
            _, node = heapq.heappop(frontier)
            if node.position == exit_pos:
                result = reconstruct_path(node)
                cost = len(result['actions'])
                print(f"  Costo: {cost} pasos")
                
                if cost < best_cost:
                    best_result = result
                    best_cost = cost
                    best_exit = exit_pos
                break

            for neighbor, action in get_neighbors(node.position):
                new_cost = node.path_cost + 1
                if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                    reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost, action=action)
                    heapq.heappush(frontier, (manhatan_distance(neighbor, exit_pos), reached[neighbor]))
    
    return best_result, best_exit

# Laberinto con múltiples salidas
maze_multiple = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", "#", " ", "#", " ", "E", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", "E", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

best_result, best_exit = find_best_exit(maze_multiple)
if best_result:
    print(f"\nMEJOR SALIDA: {best_exit}")
    print(f"Camino óptimo: {best_result['path']}")
    print(f"Acciones: {best_result['actions']}")
    print(f"Costo total: {len(best_result['actions'])} pasos")