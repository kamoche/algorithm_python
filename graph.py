class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex, values in self.adj_list.items():
            print(f'{vertex}: {values} ')

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True

        return False
    
    def remove_vertex(self, v1):
        if v1 in self.adj_list.keys():

            for other_vertex in self.adj_list[v1]:
                self.adj_list[other_vertex].remove(v1)
            
            self.adj_list.pop(v1,None)
            return True
        return False
    




    

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex('D')


graph.add_edge('A','B')
graph.add_edge('B','C')
graph.add_edge('C','A')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')



graph.print_graph()

# graph.remove_edge('B','C')
graph.remove_vertex('B')


graph.print_graph()


