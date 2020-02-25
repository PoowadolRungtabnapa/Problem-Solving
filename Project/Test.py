import matplotlib.pyplot as plt
import networkx as nx
G =nx.Graph()
G.add_edges_from([("A","C"),("A","D"),("A","B"),("B","K"),("B","H"),("B","G"),("K","C"),("K","G"),("G","H"),("H","F"),("H","E"),("H","J"),("F","J"),("J","Z"),
                  ("Z","E"),("D","E")])
Alist =['A',"C","D","E","B","H","K"]
newedge =[("A","C"),("A","D"),("D","E"),("H","E"),("B","H"),("B","K"),("K","C")]
color_map =[]
for i in G: # นี้คือหลบทีใช้ในการกำหนดสีของnodeที่เราสนใจเก็บข้อมูลแบบ list 
  if i in Alist:
        color_map.append('Y')
        print(i)
  else:
        print(i)
        color_map.append('B')
#plt.figure(15,figsize=(35,35)) <<<ขยายความกว้างmap
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos, edgelist=newedge,width=6, alpha=0.5, edge_color='R', style='dashed') #บรรทัดนี้คือการกำหนดสีของเส้นที่เราสนใจโดยเก็บการเชื่อมโยงในรู้แบบ list คือ newedge 
nx.draw(G,pos,node_color=color_map,with_labels=True,font_color="R")
plt.show()