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
  - `openpyxl` for reading and writing Excel files.

You can install the required libraries with the following commands:

```bash
pip install  openpyxl
```
# Automation Scripts

## Overview

This directory contains a collection of Python scripts designed for automating tasks within AWS using the **Boto3** library. The scripts are intended to simplify and streamline common infrastructure management tasks such as monitoring EC2 instances, scheduling tasks, and tagging resources.

## Scripts

- **Check EC2 State**:  
  This script checks the current state (running, stopped, etc.) of EC2 instances in your AWS account.

- **Check EC2 Health Status**:  
  This script retrieves and displays the health status of EC2 instances, helping to monitor their operational state and identify any potential issues.

- **Write a Scheduled Task in Python**:  
  This script demonstrates how to set up scheduled tasks using Python, which can be used to automate recurring actions like instance backups or status checks.

- **Tag EC2 Instances**:  
  This script allows you to apply custom tags to EC2 instances, helping with organization, cost tracking, or resource management.

## Requirements

- Python 3.x
- Boto3 library: Install it using `pip install boto3`
- AWS credentials configured (e.g., using AWS CLI or environment variables)

## Usage

To run any of these scripts, ensure you have the necessary AWS permissions to interact with EC2 resources and that your credentials are properly set up. Execute the scripts using Python:

```bash
python <script_name>.py
```

