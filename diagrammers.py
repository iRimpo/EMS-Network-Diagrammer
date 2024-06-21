import pandas as pd
from pyvis.network import Network

# ---------------------------- WebCTRL ----------------------------
def webctrl(csv_file_path, output_file_path, net=None):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Print column names to debug
    print("Columns in CSV file:", df.columns)

    # Create a Pyvis Network object if not provided
    if net is None:
        net = Network(height='1000px', width='auto', neighborhood_highlight=True, select_menu=True, bgcolor="white", font_color="black")

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

# ---------------------------- Metasys ----------------------------
def metasys(csv_file_path, output_file_path, net=None):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Print column names to debug
    print("Columns in CSV file:", df.columns)

    # Create a Pyvis Network object if not provided
    if net is None:
        net = Network(height='1000px', width='auto', neighborhood_highlight=True, select_menu=True, bgcolor="white", font_color="black")

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
            name = row['Item']
            description = row['Description']
            vendor_name = row['Vendor Name']
            
            controller_label = f"{name}"
            tooltip = f"Vendor: {vendor_name}\nBuilding: {index}\nDescription: {description}"
            
            net.add_node(str(controller_label), label=str(controller_label), title=tooltip, color='red')
            net.add_edge(str(index), str(controller_label))

    # Handle 'Unknown' building separately
    unknown_controllers = df[df['Building'] == 'Unknown']

    for _, row in unknown_controllers.iterrows():
        vendor_name = row['Vendor Name']
        name = row['Item']
        description = row['Description']
        controller_label = f"{name}"
        tooltip = f"Vendor: {vendor_name}\nBuilding: {index}\nDescription: {description}"
        
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