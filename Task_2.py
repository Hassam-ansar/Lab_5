
def pop(queue):
    first = queue[0]
    del queue[0]
    return first


class Graph:

    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)

        if w not in self.adj[v]:
            self.adj[v].append(w)
        if v not in self.adj[w]:
            self.adj[w].append(v)

    def bfs(self, s,goal=None):
        if s not in self.adj:
            print(f"Vertex {s} does not exist in graph.")
            return

        visited = []
        queue = []

        visited.append(s)
        queue.append(s)

        while queue:
            s = pop(queue)
            print(s, end=" ")
            if s==goal:
                print()
                print(f"Goal Found: {s}")
                return

            for i in self.adj[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print()
        if goal is None:
            print()
        else:
            print("Goal not found: ")

g = Graph()

print("Task 2")

g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('B','K')
g.add_edge('B','J')
g.add_edge('D','G')
g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')
g.add_edge('K','N')
g.add_edge('K','M')
g.add_edge('I','L')

# g.bfs('A')
g.bfs('A','G')