import re

def BiComp(v):
    global i
    num[v] = i
    L[v] = i
    i += 1
    ldata = [_ for _ in range(n + 1) if A[_][v] == 1]
    for u in ldata:
        if num[u] == 0:
            SE.append((u, v))
            father[u] = v
            BiComp(u)
            L[v] = min(L[v], L[u])
            if L[u] >= num[v]:
                if v != v0:
                    if v not in Points:
                        Points.append(v)
                else:
                    if len([father[_] for _ in range(n + 1) if father[_] == v]) > 1 and v not in Points:
                        Points.append(v)
                B = []
                B.append(SE[-1])
                while SE[-1] != (u, v):
                    SE.pop()
                    B.append(SE[-1])
                SE.pop()
                Blocks.append(B)
        else:
            if num[u] < num[v] and u != father[v]:
                SE.append((u, v))
                L[v] = min(L[v], num[u])


with open('graph2.txt', 'r') as file:
        text = file.read()
        matches = re.findall(r'\((\d+), (\d+)\)', text)

data = [*map(lambda t: tuple(map(int, t)), matches)]

n = max([max(data[i][1], data[i][1]) for i in range(len(data))])
A = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if (i, j) in data or (j, i) in data:
            A[i][j] = 1

v0 = 0
i = 1
SE = []
father = [-1 for _ in range(n + 1)]
father[v0] = -1
L = [n + 1 for _ in range(n + 1)]
B = []
Blocks = []
Points = []
num = [0 for _ in range(n + 1)]
BiComp(v0)

print("Points:", Points, end='\n\n')
print('\n\n'.join('Block {}: {}'.format(*k) for k in enumerate(Blocks, start=1)))

fileP = open('Points.txt', 'w')
fileB = open('Blocks.txt', 'w')

fileP.write(f'Начальная точка {v0}, точки сочленения графа:\n{Points}\n')
fileB.write(f'Начальная точка {v0}, блоки:\n\n')
fileB.write('\n\n'.join('Block {}: {}'.format(*k) for k in enumerate(Blocks, start=1)))
