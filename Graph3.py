# 무방향 그래프 클래스 만들기
import heapq
import collections
class Graph:
    def __init__(self):
        self.graph = {}

    def display(self):
        from pprint import pprint
        pprint(self.graph)
        print()

    def add_nodes(self, *nodes):
        for node in nodes:
            if node not in self.graph:
                self.graph[node] = {}

    def add_edges(self, *edges):
        for edge in edges:
            u, v = edge[0], edge[1]

            # 가중치는 있으면 넣고, 없으면 0으로
            w = edge[2] if len(edge) >= 3 else 0

            self.graph[u][v] = w
            self.graph[v][u] = w


    def delete_edges(self, *edges):
        for u, v in edges:
            self.graph[u].pop(v, None)
            self.graph[v].pop(u, None)

    def delete_nodes(self, *nodes):
        for node in nodes:
            if node not in self.graph:
                continue
            for v in self.graph[node]:
                self.graph[v].pop(node, None)
            del self.graph[node]


    def dfs(self, start):
        res = []
        visited = set()
        def _dfs(node):
            if node in visited:
                return
            visited.add(node)
            res.append(node)

            for v in self.graph[node]:
                _dfs(v)

        _dfs(start)
        return res

    def dfs_stack(self, start):
        res = []
        stack = [start]
        visited = set(stack)

        while stack:
            u = stack.pop()
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)

        return res

    def bfs(self, start):
        res = []
        deq = collections.deque()
        deq.append(start)
        visited = set(deq)

        while deq:
            u = deq.popleft()
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    deq.append(v)

        return res

    def dijkstra(self, start):
        lead_time = {node: float('inf') for node in self.graph}
        node_from = {node: None for node in self.graph}
        lead_time[start] = 0

        heap = []
        heapq.heappush(heap, [0, start])
        visited = set(heap)

        while heap:
            # prev_time은 start부터 u까지 걸리는 최소 시간.
            prev_time, u = heapq.heappop(heap)

            if u in visited:
                continue
            visited.add(u)

            for v, weight in self.graph[u]:
                new_time = prev_time + weight
                if new_time < lead_time[v]:
                    lead_time[v] = new_time
                    node_from[v] = u
                    heapq.heappush(heap, [lead_time[v], v])

        return lead_time, node_from

    def get_shortest_path(self, start, end):
        lead_time, node_from = self.dijkstra(start)

        res = []
        node = end
        while node_from[node]:
            res.append(node)
            node = node_from[node]
        res.append(node)
        return res[::-1]

print('node 추가 전')
g = Graph()
g.add_nodes('A', 'B', 'C', 'D', 'E', 'F')
print('node 추가 후')
g.display()
g.add_edges(['A', 'B', 1], ['A', 'D', 5], ['A', 'C', 4], ['B', 'D', 2], ['D', 'C', 4], ['C', 'E', 3], ['D', 'F', 3], ['E', 'F', 2])
print('edge 추가 후')
g.display()

print('DFS:')
print(g.dfs('A'))
print(g.dfs_stack('A'))
print(g.bfs('A'))