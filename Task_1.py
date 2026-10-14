
class Graph:
    def __init__(self, V):
        self.V = V  # Total 5 vertices (0, 1, 2, 3, 4)
        self.adj = [[] for _ in range(V)]

    # Function to add an undirected edge between v and w
    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v's list
        self.adj[w].append(v)  # Add v to w's list (for undirected graph)

    # Prints BFS traversal from a given source s
    def BFS(self, s):
        visited = [False] * self.V
        queue = []

        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.adj[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


# --- Driver program ---
if __name__ == "__main__":
    # Create a graph with 5 vertices (0 to 4)
    g = Graph(5)

    # Adding edges based on the image:
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    g.addEdge(2, 3)

    print("Following is Breadth First Traversal (starting from vertex 2):")
    g.BFS(2)