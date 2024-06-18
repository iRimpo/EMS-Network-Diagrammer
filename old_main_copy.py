import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
#pip install scipy

# Read the CSV file
df = pd.read_csv('data.csv')

# Create a directed graph
G = nx.DiGraph()

# Add the main server node
G.add_node('Server', type='server')

# Add nodes and edges based on the CSV file
for index, row in df.iterrows():
    location_node = row['Location']
    controller_node = f"Controller {row['Serial Number']}"

    # Add location node and edge from server to location
    if location_node not in G:
        G.add_node(location_node, type='location')
        G.add_edge('Server', location_node)

    # Add controller node and edge from location to controller
    if controller_node not in G:
        G.add_node(controller_node, type='controller')
        G.add_edge(location_node, controller_node)

# Define colors for different types of nodes
color_map = []
for node in G:
    if G.nodes[node]['type'] == 'server':
        color_map.append('red')
    elif G.nodes[node]['type'] == 'location':
        color_map.append('blue')
    else:
        color_map.append('green')

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=3000, font_size=6, font_color='black')
plt.title("Energy Management System Network Diagram")
# plt.savefig("output.png")
plt.show()