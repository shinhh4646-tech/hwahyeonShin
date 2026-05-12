import itertools

def is_valid_coverage(selected_users, graph)
    N = len(graph)
    covered = [False] * N
    for u in selected_users:
        covered[u] = True
        for v in graph[u]:
            covered[v] = True
    return all(covered) 

def find_minimum_coverage(graph): 
    N = len(graph)
    nodes = list(range(N))
    for k in range(1, N + 1): 
        for subset in itertools.combinations(nodes, k):
            if is_valid_coverage(subset, graph):
                return (k, list(subset)) 
    return (0, [])

def find_fast_coverage(graph): 
    N = len(graph)
    selected_users = []
    uncovered = set(range(N))
    while uncovered:
        best_node = -1
        max_covered = -1
        for u in range(N):
            current_coverage = {u}.union(graph[u]).intersection(uncovered) 
            if len(current_coverage) > max_covered:
                max_covered = len(current_coverage)
                best_node = u
        selected_users.append(best_node)
        uncovered -= {best_node}.union(graph[best_node])
    return (len(selected_users), selected_users)