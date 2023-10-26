class Graph:
    def __init__(self):
        # Initialize an empty adjacency list when a Graph object is created.
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            # If the vertex is not already in the adjacency list, add it.
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        # Print the graph's adjacency list, showing the vertices and their connections.
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.adjacency_list.keys() and vertex_2 in self.adjacency_list.keys():
            # If both vertices exist, add an edge (connection) between them.
            self.adjacency_list[vertex_1].append(vertex_2)
            self.adjacency_list[vertex_2].append(vertex_1)
            return True
        else:
            return False

    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.adjacency_list.keys() and vertex_2 in self.adjacency_list.keys():
            if vertex_2 in self.adjacency_list[vertex_1]:
                # If an edge exists between vertex_1 and vertex_2, remove it.
                self.adjacency_list[vertex_1].remove(vertex_2)
            if vertex_1 in self.adjacency_list[vertex_2]:
                self.adjacency_list[vertex_2].remove(vertex_1)
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            # If the vertex exists, remove it from the graph and all its connections.
            del self.adjacency_list[vertex]
            for value_lst in self.adjacency_list.values():
                if vertex in value_lst:
                    value_lst.remove(vertex)
            return True
        return False

# Create a Graph object
my_graph = Graph()

# Add vertices (A, B, C, D) to the graph
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

# Add edges to connect the vertices
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")

# Print the graph's adjacency list
my_graph.print_graph()

# Remove vertex "A" and its connections from the graph
my_graph.remove_vertex("A")

# Print the graph again after removing "A"
print("After remove..")
my_graph.print_graph()
