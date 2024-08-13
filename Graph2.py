## 다익스트라 알고리즘을 활용하여 최단 경로 찾기

import heapq

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["A", "B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

# node는 시작 노드 (기준 노드)를 의미함.
def dijkstra(graph, node):

    # 소요 시간을 기록할 사전
    lead_time = {node: float('inf') for node in graph}

    # 현재 노드의 이전 노드를 기록할 사전
    node_from = {node: "" for node in graph}

    # 출발 노드는 자기 자신으로부터의 소요시간이므로 0.
    lead_time["A"] = 0

    heap = [(0, node)]
    visited = set()

    while heap:
        prev_time, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            # lead_time안에 있다는 것은, 기준 노드 n으로부터 v까지의 소요 시간이 lead_time에 기록되어 있다는 뜻임.
            # 따라서 n -> u, u -> v까지의 소요 시간 합과 lead_time에 적힌 n -> v 소요 시간을 비교하여
            # 더 작은 값을 lead_time에 기록해야 함.
            new_time = lead_time[u] + weight
            if new_time < lead_time[v]:
                lead_time[v] = new_time
                node_from[v] = u
                heapq.heappush(heap, (lead_time[v], v))

    return lead_time, node_from

def shortest_path(node_from, lead_time, start, end):
    path = ""
    node = end
    while node_from[node]:
        path = " -> " + str(node) + path
        node = node_from[node]
    return f"{str(node) + path} (cost = {str(lead_time[end])})"

lead_time, node_from = dijkstra(graph, 'A')
print(lead_time)
print(node_from)

print(shortest_path(node_from, lead_time, 'A', 'F'))