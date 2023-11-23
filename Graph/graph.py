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

    def bfs(self, vertex):
        # Set to keep track of visited vertices
        visited = set()
        
        # Mark the starting vertex as visited and initialize the queue
        visited.add(vertex)
        queue = [vertex]

        # Continue BFS until the queue is empty
        while queue:
            # Get the current vertex from the front of the queue
            current_vertex = queue.pop(0)
            
            print(current_vertex)

            # Explore adjacent vertices
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                # Visit unvisited adjacent vertices and enqueue them
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex):
        # Set to keep track of visited vertices
        visited = set()

        # Initialize the stack with the starting vertex
        stack = [vertex]

        # Continue DFS until the stack is empty
        while stack:
            # Get the current vertex from the top of the stack
            current_vertex = stack.pop()

            # Visit and mark the current vertex as visited
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

            # Explore adjacent vertices
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                # Push unvisited adjacent vertices onto the stack
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)




# Create a Graph object
my_graph = Graph()

# Add vertices (A, B, C, D) to the graph
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

# Add edges to connect the vertices
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")

# # Print the graph's adjacency list
# my_graph.print_graph()

# # Remove vertex "A" and its connections from the graph
# my_graph.remove_vertex("A")

# # Print the graph again after removing "A"
# print("After remove..")
# my_graph.print_graph()

# print using bfs
# my_graph.bfs("A")

# print using dfs
my_graph.dfs("A")