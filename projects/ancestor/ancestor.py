def earliest_ancestor(ancestors, starting_node):

    # reverse list into a dict
    graph = {}
    for p, c in ancestors:
        if c not in graph:
            graph[c] = []
        graph[c].append(p)

    s = []
    s.append(starting_node)
    visited = []
    
    while len(s):
        v = s.pop()
        if v not in visited:            
            visited.append(v)
            if v not in graph:
                if len(visited) > 1:
                    return v
                else:
                    return -1

            s.append(min(graph[v]))

    return visited.pop()

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 6))
