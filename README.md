# Automation Inventory Project

## Overview

The **Automation Inventory Project** is a Python program that reads an Excel file containing inventory data, processes it, and provides a detailed summary. The program counts the number of products per supplier, calculates the total inventory per supplier, and identifies suppliers with inventory levels less than 10 units. This automation is designed to streamline inventory management and assist with maintaining optimal stock levels.

## Features

- **Reads Inventory Data**: Parses an Excel file containing product and supplier information.
- **Counts Products per Supplier**: Displays the number of products provided by each supplier.
- **Calculates Total Inventory**: Computes the total quantity of products available for each supplier.
- **Identifies Low Stock**: Filters and displays suppliers with less than 10 units of inventory.
- **Sorted Output**: Presents the results in a clear and structured format.

## Requirements

Before running the program, make sure you have the following dependencies installed:

- **Python 3.x**
- **Required Python libraries**:
  - `pandas` for data manipulation and analysis.
  - `openpyxl` for reading and writing Excel files.

You can install the required libraries with the following commands:

```bash
pip install pandas openpyxl
