import heapq

def dijkstra(graph, node):
    lead_time = {node: float('inf') for node in graph}
    node_from = {node: None for node in graph}

    lead_time[node] = 0
    heap = [(0, node)]
    visited = set()

    while heap:
        prev_time, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            new_time = prev_time + weight
            # lead_time안에 있다는 것은, 기준 노드 n으로부터 v까지의 소요 시간이 lead_time에 기록되어 있다는 뜻임.
            # 따라서 n -> u, u -> v까지의 소요 시간 합과 lead_time에 적힌 n -> v 소요 시간을 비교하여
            # 더 작은 값을 lead_time에 기록해야 함.
            # 작은 값으로 갱신 시, node_from 및 heap에 값 추가.
            if new_time < lead_time[v]:
                lead_time[v] = new_time
                node_from[v] = u
                heapq.heappush(heap, (new_time, v))

    return lead_time, node_from

def shortest_path(lead_time, node_from, start, end):
    path = ""
    node = end
    while node_from[node]:
        path = ' -> ' + node + path
        node = node_from[node]
    return node + path + f' (cost = {str(lead_time[end])})'

graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}

lead_time, node_from = dijkstra(graph, "A")
print(shortest_path(lead_time, node_from, "A", "F"))
lead_time, node_from = dijkstra(graph, "B")
print(shortest_path(lead_time, node_from, "B", "E"))