'''import calculation
import graph_matrix
import graphs
import heuristic
import brute_force
g1 = graph_matrix.random_graph_generate(8)

#print(g1.ability_matrix)
#print(g1.adjacency_matrix)

calculation.print_special_states(g1)
print('the probability if all the transitions are activated: ')
calculation.print_result(g1)
print('\nthe result of deactivate all useless transitions :')
heuristic.deactivate_all_useless_transitions(g1)
print('\nthe result of dijkstra :')
heuristic.dijkstra(g1)
heuristic.brute_force_after_daut(g1)
brute_force.brute_force(g1)'''
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题风格
sns.set_theme(style="whitegrid")

# 加载内置的企鹅数据集
penguins = pd.DataFrame({
    '职称': {0:"正教授", 1:"副教授", 2:"助理教授"},
    '频数': {0:151, 1:131, 2:58}
})

# 绘制分组柱状图，按物种和性别分组，显示体重均值和标准差
g = sns.barplot(
    data=penguins,
    x="职称",
    y="频数",

)

# 添加标题和坐标轴标签
g.set_title("Penguin body mass by species and sex")
g.set_xlabel("Species")
g.set_ylabel("Body mass (g)")

# 显示图形
plt.show()

'''
'''transition_probs = {
    's0': [('s1', 0.5, True), ('s1', 0.5, True)],
    's2': [('s4', 0.98, False), ('s3', 0.02, False)],
    's1': [('s3', 0.01, False), ('s4', 0.99, True)],
    's4': [('s4', 1, True)]}
print("Length : %d" % len (transition_probs))
for state, transitions in transition_probs.items():
    print(state)
    print(transitions)'''

'''from tkinter import *
from PIL import ImageTk, Image

# create a window
window = Tk()

# load the image
img = Image.open("graph.png")

# create a PhotoImage object from the image
photo_img = ImageTk.PhotoImage(img)

# create a label and display the image
label = Label(window, image=photo_img)
label.grid(row=5,column=1)

# start the window
window.mainloop()'''

import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
import pygraphviz as pgv

# Define the graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(['Rainy', 'Sunny'])

# Add edges
controllable_edges = [('Rainy', 'Rainy'), ('Rainy', 'Sunny'), ('Sunny', 'Rainy')]
uncontrollable_edges = [('Sunny', 'Sunny')]

G.add_edges_from(controllable_edges, weight=0.0, color='r', controllable=True)
G.add_edges_from(uncontrollable_edges, weight=0.0, color='b', controllable=False)

# Draw the graph
A = to_agraph(G)
A.graph_attr.update(rankdir='LR')
A.node_attr.update(color='lightblue2', style='filled', shape='circle', fontname='Arial', fontsize=24)
A.edge_attr.update(fontsize=20, fontname='Arial')

# Draw controllable edges in red
controllable_edges = [(u, v) for u, v in G.edges() if G[u][v]['controllable'] == True]
for u, v in controllable_edges:
    e = A.get_edge(u, v)
    e.attr['color'] = 'red'
    e.attr['penwidth'] = 3

# Draw uncontrollable edges in blue
uncontrollable_edges = [(u, v) for u, v in G.edges() if G[u][v]['controllable'] == False]
for u, v in uncontrollable_edges:
    e = A.get_edge(u, v)
    e.attr['color'] = 'blue'
    e.attr['penwidth'] = 3

# Save the graph
A.draw('weather_model.png', format='png', prog='dot')