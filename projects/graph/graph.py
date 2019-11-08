"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError('Cant create edge, one or more given vertices doesnt exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Add node to visited then print
        visited.add(starting_vertex)
        print(starting_vertex)
        # Go though the vertices connected to the current vertex
        for next_vert in self.vertices[starting_vertex]:
            # if the next vert is not in visited already, call
            # the recursive function on it
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        # storing lists of traversed vertices in the queue
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            # get the list of traversed vertices from the queue
            current_path = queue.dequeue()
            # get the last vertex in the list
            vertex = current_path[len(current_path) - 1]
            if vertex is destination_vertex:
                return current_path
            # if its not the destination it goes through all the vertices the current
            # vertex is connected to
            for next_vert in self.vertices[vertex]:
                # checks if this vertex has been visited, if not
                # it adds it to the visited list
                # then creates a new list of the most
                # up to date path, by grabbing the old one
                # and appending the vert to it
                # then adds it to the queue
                if next_vert not in visited:
                    visited.add(next_vert)
                    path = list(current_path)
                    path.append(next_vert)
                    queue.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        # storing lists of traversed vertices in the stack
        stack.push([starting_vertex])
        while stack.size() > 0:
            # get the list of traversed vertices from the stack
            current_path = stack.pop()
            # get the last vertex in the list
            vertex = current_path[len(current_path) - 1]
            if vertex is destination_vertex:
                return current_path
            # if its not the destination it goes through all the vertices the current
            # vertex is connected to
            for next_vert in self.vertices[vertex]:
                # checks if this vertex has been visited, if not
                # it adds it to the visited list
                # then creates a new list of the most
                # up to date path, by grabbing the old one
                # and appending the vert to it
                # then adds it to the stack
                if next_vert not in visited:
                    visited.add(next_vert)
                    new_path = list(current_path)
                    new_path.append(next_vert)
                    stack.push(new_path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('Starting dft')
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('Starting bft')
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('Starting dft recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Starting bfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Starting dfs')
    print(graph.dfs(1, 6))
