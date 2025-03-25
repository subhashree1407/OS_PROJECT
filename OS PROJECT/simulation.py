import networkx as nx
import matplotlib.pyplot as plt
import time

def animate_graph(graph):
    plt.ion()  # Interactive mode ON
    fig, ax = plt.subplots()
    
    for i in range(3):  # Animate 3 times
        ax.clear()
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, node_color="cyan", edge_color="black", node_size=2000, font_size=12, ax=ax)
        plt.draw()
        plt.pause(1)

    plt.ioff()  # Turn off interactive mode
    plt.show()
