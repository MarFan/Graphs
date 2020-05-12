import sys
sys.path.insert(0, '../graph')
from util import Queue, Stack

def earliest_ancestor(ancestors, starting_node):

    graph = {}
    for p, c in ancestors:
        if c not in graph:
            graph[c] = []
        graph[c].append(p)

    s = Stack()
    s.push(starting_node)
    visited = []
    
    while s.size() > 0:
        v = s.pop()
        if v not in visited:            
            visited.append(v)
            if v not in graph:
                if len(visited) > 1:
                    return v
                else:
                    return -1

            s.push(min(graph[v]))

    return visited.pop()

if __name__ == '__main__':
    from os import system
    system('clear')
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 6))
