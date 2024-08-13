graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()
    elif node in visited:
        return
    visited.add(node)

    for next in graph[node]:
        dfs(graph, next, visited)

    return visited

# 스택을 이용하여 구하기
def dfs_2(graph, node):
    res = []
    stack = [node]
    visited = set(node)

    while stack:
        current_node = stack.pop()
        res.append(current_node)
        for v in graph[current_node]:
            if v not in visited:
                stack.append(v)
                visited.add(v)

    return res

def bfs(graph, node):
    res = []
    queue = [node]
    visited = set(node)

    while queue:
        u = queue.pop(0)
        res.append(u)
        for v, w in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)

    return res



graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}

print(bfs(graph, 'A'))