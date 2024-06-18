import pandas as pd
from pyvis.network import Network

# Read the CSV file
csv_file_path = 'webctrl.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Print column names to debug
print("Columns in CSV file:", df.columns)

# Create a Pyvis Network object, webctrl
net = Network(height='1000px', width='auto', neighborhood_highlight=True, select_menu=True, bgcolor="white", font_color="black")
#filter_menu=True
# Add the vendor nodes
vendors = set()
vendor = df['Vendor Name'].unique()
for x in vendor:
    if x not in vendors:
        vendors.add(x)
        net.add_node(str(x), label=str(x), color='blue')

# Add nodes and edges based on the CSV file
buildings = df['Building'].unique()

for index in buildings:
    if index == 'Unknown':
        continue  # Skip adding 'Unknown' as a building node
    
    # Add building node
    net.add_node(str(index), label=str(index), color='green')
    
    # Get the unique vendors for this building
    building_vendors = df[df['Building'] == index]['Vendor Name'].unique()
    
    for vendor_name in building_vendors:
        net.add_edge(str(vendor_name), str(index))
    
    # Filter the controllers for this building
    building_controllers = df[df['Building'] == index]
    
    for _, row in building_controllers.iterrows():
        # Ensure column names match those in your CSV file
        serial_number = row['Serial Number']
        driver_version = row['Driver Version']
        vendor_name = row['Vendor Name']
        
        controller_label = f"{serial_number} ({driver_version})"
        tooltip = f"Vendor: {vendor_name}\nBuilding: {index}"
        
        net.add_node(str(controller_label), label=str(controller_label), title=tooltip, color='red')
        net.add_edge(str(index), str(controller_label))

# Handle 'Unknown' building separately
unknown_controllers = df[df['Building'] == 'Unknown']

for _, row in unknown_controllers.iterrows():
    vendor_name = row['Vendor Name']
    serial_number = row['Serial Number']
    driver_version = row['Driver Version']
    controller_label = f"{serial_number} ({driver_version})"
    tooltip = f"Vendor: {vendor_name}\nBuilding: Unknown"
    
    existing_edges = [(edge['from'], edge['to']) for edge in net.get_edges()]

    # Check if the vendor is already connected to a building with this controller to remove duplicate edges
    is_already_connected = False
    for edge in existing_edges:
        if edge[0] == vendor_name and edge[1] != controller_label:
            is_already_connected = True
            break
    
    if not is_already_connected:
        net.add_node(str(controller_label), label=str(controller_label), title=tooltip, color='red')
        net.add_edge(str(vendor_name), str(controller_label))

# pyvis settings/filters
net.show_buttons(filter_=['physics'])

# Generate and save the network diagram
output_file_path = 'Diagram.html'  # Output file

# Show the network in a file
net.show(output_file_path, notebook=False)

# Read the generated HTML file and insert the header
with open(output_file_path, 'r') as file:
    html_content = file.read()

# Define the header HTML to insert an image on top of the diagram
header_html = '''
<header>
    <img src="images/berklab.png" alt="Berkeley Lab" style="width: 7%; height: auto; display: block; margin-left: 0; margin-right: auto;">
    <h1> Building Automation Systems Diagram </h1>
    <h3> By. Richard Azucenas </h3>
</header>
'''

# Insert the header at the beginning of the HTML content
html_content = html_content.replace('<head>', f'<head>\n{header_html}')

# Write the modified content back to the HTML file
with open(output_file_path, 'w') as file:
    file.write(html_content)

print(f"Network diagram with header has been saved to {output_file_path}")