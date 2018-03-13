graph = {'A' : ['B', 'F'], 
        'B': ['A', 'C'], 
        'C': ['B','D'], 
        'D': ['C','E'], 
        'E': ['D','F'], 
        'F': ['E', 'A']
        }

def find_path(graph, start, end, path = []):
    path = path + [start]

    if start == end:
        print("Ending")
        return path

    for node in graph[start]:
        print("Checking Node", node)

        if node not in path:
            print("Path so far", path)

            newp = find_path(graph, node, end, path)
            if newp:
                return newp

find_path(graph, 'B', 'E')
