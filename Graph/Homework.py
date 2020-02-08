import networkx as nx
import matplotlib.pylab as plt

G = nx.Graph()

G.add_edges_from([('A','B'),('A','M'),('A','L'),('B','C'),('B','D'),
                  ('B','N'),('B','O'),('C','D'),('D','E'),('D','O'),
                  ('E','F'),('F','G'),('F','N'),('G','H'),('H','N'),
                  ('H','I'),('H','P'),('P','O'),('P','I'),('P','M'),
                  ('I','J'),('J','K'),('K','M'),('K','L'),])

Alist = nx.all_neighbors(G,'A')
Elist = nx.all_neighbors(G,'E')
Ilist = nx.all_neighbors(G,'I')

A = set()
E = set()
I = set()

for a in Alist :
    A.add(a)
    for n in nx.all_neighbors(G,f'{a}') :
        A.add(n)

for e in Elist :
    E.add(e)
    for m in nx.all_neighbors(G,f'{e}') :
        E.add(m)

for i in Ilist :
    I.add(i)
    for j in nx.all_neighbors(G,f'{i}') :
        I.add(j)

print(A)
print(E)
print(I)

print(A&E&I)