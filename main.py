from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
   
  visited = {}
  visited[source] = (0,0)
  queue = deque([source])
  while queue:
    node = queue.popleft()
    for neighbor, weight in graph[node]:
      if neighbor not in visited:
        visited[neighbor] = (visited[node][0] + weight, visited[node][1] + 1)
        queue.append(neighbor)
  return visited

    

    
    
def bfs_path(graph, source):
    parent = {source: None}
    queue = deque([source])

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in parent:
                parent[neighbor] = current_vertex
                queue.append(neighbor)

    return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    path = []
    current = destination
    while current is not None:
        path += str(current)
        current = parents[current]
    return path[:0:-1]


  path_string = ""
  for node in path:
    path_string += node

  return path_string

