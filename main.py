import pandas as pd
from diagrammers import webctrl, metasys
from pyvis.network import Network

# Read the CSV file
webctrl_data = 'webctrl.csv'
metasys_data = 'metasys.csv'

# Generate and save the network diagram
output_file_path = 'Diagram.html'  # Output file

# Create a Pyvis Network object, webctrl
net = Network(height='1000px', width='auto', neighborhood_highlight=True, select_menu=True, bgcolor="white", font_color="black")

# --------------- Diagrammers ---------------
webctrl(webctrl_data, output_file_path, net=net)
metasys(metasys_data, output_file_path, net=net)

# pyvis settings/filters
net.show_buttons(filter_=['physics'])

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