import re

def ReadEdgesFromFile(fileName):
    edges = []
    with open(fileName)as f:
        for item in f.readline()[1:-1].split('),'):
            edge = item.replace('(', '').replace(' ', '').replace(')', '').split(',')
            edges.append((int(edge[0]), int(edge[1])))
    return edges


def FindNodes(v, edges):
    res = []
    for i in edges:
        if v == i[0]:
            res.append(i[1])
        if v == i[1]:
            res.append(i[0])
    return res


def GetVertices(edges):
    vertices = [1]
    for edge in edges:
        for i in edge:
            if i not in vertices:
                vertices.append(i)
    return vertices


def IsTree(edges):
    return IsConnected(edges) and len(edges) == len(GetVertices(edges)) - 1


def IsConnected(edges):
    def check(u, edges, visited: dict):
        visitedVertices = 1
        visited[u] = True
        for v in FindNodes(u, edges):
            if not visited[v]:
                visitedVertices += check(v, edges, visited)
        return visitedVertices

    visited = {}
    for i in GetVertices(edges):
        visited[i] = False
    return check(edges[0][0], edges, visited) == len(GetVertices(edges))


def IsBipartite(edges):
    color = {}
    for i in GetVertices(edges):
        color[i] = 0

    def invert(c):
        if c == 1:
            return 2
        else:
            return 1

    def dfs(v, c):
        color[v] = c
        for u in FindNodes(v, edges):
            if color[u] == 0:
                dfs(u, invert(c))
            elif color[u] == c:
                return False

    for i in GetVertices(edges):
        if color[i] == 0:
            dfs(i, 0)

    return True


def DFS(edges):
    def dfs(v: int, edges: list, visited: dict, d_edges: list, rev_edges: list, father: dict, step: int):
        visited[v] = step
        step += 1
        for u in FindNodes(v, edges):
            if visited[u] == 0:
                d_edges.append((u, v))
                father[u] = v
                dfs(u, edges, visited, d_edges, rev_edges, father, step)
            elif visited[u] < visited[v] and father[v] != u:
                rev_edges.append((u, v))

    d_edges = []
    rev_edges = []
    visited = {}
    v_list = GetVertices(edges)
    father = {}
    for i in v_list:
        visited[i] = 0
    for v in v_list:
        if visited[v] == 0:
            father[v] = 1
            dfs(v, edges, visited, d_edges, rev_edges, father, 1)
    return d_edges, rev_edges


firstGraphEdges = ReadEdgesFromFile('graph1.txt')
secondGraphEdges = ReadEdgesFromFile('graph2.txt')

firstGraph = DFS(firstGraphEdges)
secondGraph = DFS(secondGraphEdges)

with open('T1.txt', 'w') as wr:
    wr.writelines(str(firstGraph[0]))
with open('B1.txt', 'w') as wr:
    wr.writelines(str(firstGraph[1]))
with open('T2.txt', 'w') as wr:
    wr.writelines(str(secondGraph[0]))
with open('B2.txt', 'w') as wr:
    wr.writelines(str(secondGraph[1]))


print(f'Первый граф связан: ' + str(IsConnected(firstGraphEdges)))
print(f'Первый граф дерево: ' + str(IsTree(firstGraphEdges)))
print(f'Первый граф двудольный: ' + str(IsBipartite(firstGraphEdges)))
print(f'Первый граф поиска в глубину связан: ' + str(IsConnected(firstGraph[0])))
print(f'Первый граф поиска в глубину дерево: ' + str(IsTree(firstGraph[0])))
print(f'Первый граф поиска в глубину двудольный: ' + str(IsBipartite(firstGraph[0])))

print(f'Второй граф связан: ' + str(IsConnected(secondGraphEdges)))
print(f'Второй граф дерево: ' + str(IsTree(secondGraphEdges)))
print(f'Второй граф двудольный: ' + str(IsBipartite(secondGraphEdges)))
print(f'Второй граф поиска в глубину связан: ' + str(IsConnected(secondGraph[0])))
print(f'Второй граф поиска в глубину дерево: ' + str(IsTree(secondGraph[0])))
print(f'Второй граф поиска в глубину двудольный: ' + str(IsBipartite(secondGraph[0])))
