import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Read the CSV file
df = pd.read_csv('data.csv')

# Create a directed graph
G = nx.DiGraph()

# keep track of all vendors
vendors = set()
# Add the main server node
for index, row in df.iterrows():
    vendor_node = row['Vendor Name']
    if vendor_node not in vendors:
        vendors.add(vendor_node)

for vendor_node in vendors:        
    G.add_node(vendor_node, type='vendor')

# Add nodes and edges based on the CSV file
for index, row in df.iterrows():
    vendor_node = row['Vendor Name']
    location_node = row['Location']
    controller_node = f"Controller {row['Serial Number']}"

    # Add location node and edge from server to location
    if location_node not in G:
        G.add_node(location_node, type='location')
    G.add_edge(vendor_node, location_node)

    # Add controller node and edge from location to controller
    if controller_node not in G:
        G.add_node(controller_node, type='controller')
    G.add_edge(location_node, controller_node)

# Define positions for the nodes
pos = nx.spring_layout(G)

# Define the path to the images
image_path = {
    'vendor': 'images/vendor.png',
    'location': 'images/location.png',
    'controller': 'images/controller.png'
}

# Function to get the appropriate image for a node
def get_image(node_type):
    path = image_path.get(node_type)
    if path and os.path.isfile(path):
        return mpimg.imread(path)
    return None

# Draw the nodes with images
ax = plt.gca()
fig = plt.gcf()

for node, (x, y) in pos.items():
    node_type = G.nodes[node]['type']
    img = get_image(node_type)
    if img is not None:
        imagebox = plt.imshow(img, extent=(x - 0.1, x + 0.1, y - 0.1, y + 0.1), aspect='equal', zorder=2)

# Draw edges
nx.draw_networkx_edges(G, pos, ax=ax, arrows=True)

# Draw labels
nx.draw_networkx_labels(G, pos, ax=ax, font_size=6, font_color='black')

plt.title("Energy Management System Network Diagram")
plt.axis('off')
plt.show()
