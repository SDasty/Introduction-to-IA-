import time
import tracemalloc
from collections import deque

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

    def path(self):
        """path from root node."""
        node, path_back = self, []
        while node:
            path_back.append(node.position)
            node = node.parent
        return list(reversed(path_back))


class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return self.graph.get(state, [])

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal


# BFS
def breadth_first_graph_search(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.position):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.position)
        for action in problem.actions(node.position):
            child = Node(problem.result(node.position, action), node)
            if child.position not in explored and all(c.position != child.position for c in frontier):
                if problem.goal_test(child.position):
                    return child
                frontier.append(child)
    return None


# 
# IDS
# 
def iterative_deepening_search(problem):
    depth = 0
    while True:
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        depth += 1


def depth_limited_search(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit)


def recursive_dls(node, problem, limit):
    if problem.goal_test(node.position):
        return node
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occurred = False
        for action in problem.actions(node.position):
            child = Node(problem.result(node.position, action), node)
            result = recursive_dls(child, problem, limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result
        return "cutoff" if cutoff_occurred else None


# get time and memory usage
def time_memory(algoritmo, problem):
    tracemalloc.start()
    start = time.perf_counter()
    solution = algoritmo(problem)
    end = time.perf_counter()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "route": solution.path() if solution else None,
        "time": end - start,
        "peak memory": peak_memory / 1024  # KB
    }



# Main
if __name__ == "__main__":
    grafo_metro = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'H', 'I'],
        'F': ['C', 'J'],
        'G': ['D'],
        'H': ['E'],
        'I': ['E', 'J'],
        'J': ['F', 'I']
    }

    problem = Problem('A', 'J', grafo_metro)

    resultado_bfs = time_memory(breadth_first_graph_search, problem)
    resultado_ids = time_memory(iterative_deepening_search, problem)

    print("BFS")
    print("route:", resultado_bfs["route"])
    print("time :", resultado_bfs["time"])
    print("peak memory (KB):", resultado_bfs["peak memory"])

    print("\nIDS")
    print("route:", resultado_ids["route"])
    print("time:", resultado_ids["time"])
    print("peak memory (KB):", resultado_ids["peak memory"])