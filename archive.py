import pandas as pd
from graphviz import Digraph

# Assuming your data is loaded correctly
df = pd.read_csv('data copy.csv')

dot = Digraph(comment='Energy Management System')

dot.node('Server', 'Energy Management System Program')

for location in df['Location'].unique():
    dot.node(location, location)
    dot.edge('Server', location)
    
    for index, row in df[df['Location'] == location].iterrows():
        controller_description = (f"Serial: {row['Serial Number']}\n"
                                  f"Driver: {row['Driver Version']}\n"
                                  f"Boot: {row['Boot Version']}\n"
                                  f"Vendor: {row['Vendor Name']}")
        controller_node_id = f"{row['Serial Number']}_{row['Driver Version']}"  # Unique ID for the node
        dot.node(controller_node_id, label=controller_description)
        dot.edge(location, controller_node_id)

# Save and render the diagram
dot_path = dot.save('energy_management_system.dot')
print(f"DOT file saved as {dot_path}")

try:
    dot.render('energy_management_system', format='png')
    print("Diagram saved as 'energy_management_system.png'")
except Exception as e:
    print(f"Rendering error: {e}")

# For debugging: Print the DOT file content
with open('energy_management_system.dot', 'r') as file:
    print(file.read())
