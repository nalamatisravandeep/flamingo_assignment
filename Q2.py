from collections import deque, defaultdict

def hasCircularDependency(n, edges):
    adj = defaultdict(list)
    in_degree = [0] * n
    for a, b in edges:
        adj[b].append(a)    
        in_degree[a] += 1   

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    processed = 0

    while queue:
        u = queue.popleft()
        processed += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return processed != n

# Example 1
n1 = 4
edges1 = [[0, 1], [1, 2], [2, 3]]
print(hasCircularDependency(n1, edges1))  

# Example 2
n2 = 4
edges2 = [[0, 1], [1, 2], [2, 0]]
print(hasCircularDependency(n2, edges2))  
