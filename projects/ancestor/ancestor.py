# find node in values, check if key of that node is a value in another node. keep checking until get to node not in values
def earliest_ancestor(ancestors, starting_node, visited=None):
    values = []
    keys = []
    # build up the values list with the second value in the tuple.
    # this value is always a child, so we know there is a value connected to it
    # build keys list with the first value, these are all parent nodes
    for pair in ancestors:
        keys.append(pair[0])
        values.append(pair[1])
    # build visited set
    if visited is None:
        visited = set()
    # base case, if the node is not a child (in values) and it hasnt been visited (not part of the path)
    # return -1
    if starting_node not in values and starting_node not in visited:
        return -1
    # check the values for one == current node
    # if it finds it, add they key to visited, then cal the recursion
    # with the new starting node
    for pair in ancestors:
        if pair[1] == starting_node:
            visited.add(pair[0])
            return earliest_ancestor(ancestors, pair[0], visited)
    return starting_node


# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, value):
#         self.queue.append(value)
#
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#
#     def size(self):
#         return len(self.queue)
#
#
# class Graph:
#     def __init__(self):
#         self.vertices = {}
#
#     def add_vertex(self, vertex_id):
#         if vertex_id not in self.vertices:
#             self.vertices[vertex_id] = set()
#
#     def add_edges(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise KeyError('Vertex does not exist')
#
#
# def earliest_ancestor(ancestors, starting_node):
#     graph = Graph()
#
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#
#         graph.add_edges(pair[1], pair[0])
#
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_length = 1
#     earliest_ancestor = -1
#
#     while q.size() > 0:
#         path = q.dequeue()
#         vertex = path[-1]
#
#         if(len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
#             earliest_ancestor = vertex
#             max_path_length = len(path)
#
#         for neighbor in graph.vertices[vertex]:
#             new_path = list(path)
#             new_path.append(neighbor)
#             q.enqueue(new_path)
#     return earliest_ancestor


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 9))