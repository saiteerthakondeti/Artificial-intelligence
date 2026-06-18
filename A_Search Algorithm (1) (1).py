import heapq

def a_star_search(graph, heuristics, start, goal, graph_name):
    print(f"\n{'='*50}")
    print(f"A* SEARCH - {graph_name}")
    print(f"Start: {start}, Goal: {goal}")
    print(f"{'='*50}")
    
    # Priority queue: (f = g+h, g, path, node)
    pq = [(heuristics[start], 0, [start], start)]
    visited = {}
    step = 1
    
    while pq:
        f, g, path, node = heapq.heappop(pq)
        
        if node in visited and visited <= g:
            continue
        visited = g
        
        print(f"Step {step}: Expand {node}")
        print(f" g={g}, h={heuristics[node]}, f={f}, path={path}")
        
        if node == goal:
            print(f"\nGOAL REACHED!")
            print(f"Optimal Path: {' -> '.join(path)}")
            print(f"Total Cost: {g}")
            return g, path
        
        for neighbor, cost in graph.get(node, []):
            if neighbor not in path: # avoid cycles
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_f, new_g, new_path, neighbor))
                print(f" Enqueue {neighbor}: g={new_g}, h={heuristics[neighbor]}, f={new_f}")
        
        step += 1
        print()
    
    print("Goal not reachable")
    return float('inf'), []

# ======================================================
# GRAPH 1: From Image 2 - S to G
# ======================================================
graph1 = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4), ('E', 5)],
    'D': [('E', 2)],
    'E': [('F', 4)],
    'F': [('G', 3.5)],
    'C': [], 'G': []
}
heuristics1 = {
    'S': 11.5, 'A': 10.1, 'B': 5.8, 'C': 3.4,
    'D': 9.2, 'E': 7.1, 'F': 3.5, 'G': 0
}

# ======================================================
# GRAPH 2: From Image 1 - A to G 
# ======================================================
graph2 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}
heuristics2 = {
    'A': 5, 'B': 6, 'C': 4, 'D': 3, 
    'E': 3, 'F': 1, 'G': 0
}

# ======================================================
# GRAPH 3: From Image 1 - S to G
# ======================================================
graph3 = {
    'S': [('A', 3), ('D', 2)],
    'A': [('B', 5), ('C', 10)],
    'B': [('C', 2), ('D', 1), ('E', 1)],
    'C': [('G', 4)],
    'D': [('E', 4)],
    'E': [('G', 3)],
    'G': []
}
heuristics3 = {
    'S': 7, 'A': 9, 'B': 4, 'C': 2, 
    'D': 5, 'E': 3, 'G': 0
}

# ======================================================
# RUN ALL 3 A* SEARCHES
# ======================================================
if __name__ == "__main__":
    # Graph 1: S -> G with decimals
    a_star_search(graph1, heuristics1, 'S', 'G', "GRAPH 1: S to G")
    
    # Graph 2: A -> G 
    a_star_search(graph2, heuristics2, 'A', 'G', "GRAPH 2: A to G")
    
    # Graph 3: S -> G 
    a_star_search(graph3, heuristics3, 'S', 'G', "GRAPH 3: S to G")
