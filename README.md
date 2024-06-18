# EMS Network Diagrammer

A tool to create visualizations/mappings of the networks on the Energy Management Systems at Lawrence Berkeley National Laboratory.

### https://irimpo.github.io/EMS-Network-Diagrammer/

## Purpose
There are more than 800 controllers at Lawrence Berkeley National Laboratory that relay critical data for maintenance. This project automates the tedious job of creating diagrams of the network, providing a creative and efficient way to display all the controllers and their relationships by using CSV file reports from the building automation sytems: WebCTRL, Metasys, Lutron, Quantum, Wattstopper 

![alt text](https://i.imgur.com/umL2hqY.png)

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Pyvis
- Pandas

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/iRimpo/EMS-Network-Diagrammer
    cd EMS-Network-Diagrammer
    ```

2. Install the required Python packages:
    ```bash
    pip install pyvis pandas
    ```

3. Ensure you have a CSV file of controllers formatted correctly (see below).

## CSV File Format

Edit your CSV file to have the following columns:
- Status
- Boot Version
- Driver Version
- Location
- Full Source
- Serial Number
- Vendor Name
- Local Access Disabled
- Downloaded by
- Building

Example CSV content:
```csv
Status,Boot Version,Driver Version,Location,Full Source,Serial Number,Vendor Name,Local Access Disabled,Downloaded by,Building
Operational,1.0,2.3.4,Room 101,Source A,123456,VendorX,No,UserA,Building 1
Out of service,1.2,3.1.4,Room 202,Source B,654321,VendorY,Yes,UserB,Building 2
```
