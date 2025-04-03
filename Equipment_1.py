from collections import deque

def NearestEqupment(n, edges, availability, startProvider, targetEquipment):
    # Buildlding adjacency list for the graph
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS initialization
    queue = deque([(startProvider, [startProvider])])  # (current provider, path taken)
    visited = set([startProvider])

    while queue:
        provider, path = queue.popleft()

        
        if targetEquipment in availability.get(provider, []):
            return path  # Return the path to the provider

        # Exploring neighbours
        for neighbor in graph.get(provider, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return -1  # No provider found

n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
startProvider = 2
target_equipment = "excavator"

print(NearestEqupment(n, edges, availability, startProvider, targetEquipment))