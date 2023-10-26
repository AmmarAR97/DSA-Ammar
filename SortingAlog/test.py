# import os
# import pandas as pd

# # Function to process a single Excel file
# def process_excel_file(file_path):
#     df = pd.read_excel(file_path, skiprows=2)  # Skip the first 30 rows
#     return df

# # Function to process all Excel files in a directory and consolidate them
# def consolidate_excel_files(directory_path, output_file):
#     all_data = pd.DataFrame()
    
#     for filename in os.listdir(directory_path):
#         if filename.endswith(".xlsx"):
#             file_path = os.path.join(directory_path, filename)
#             df = process_excel_file(file_path)
#             all_data = all_data.append(df, ignore_index=True)
    
#     all_data.to_excel(output_file, index=False)

# # Provide the path to the directory containing Excel files
# input_directory = "/Users/thedarkhorse/Desktop"

# # Specify the output file name
# output_file = "consolidated_output.xlsx"

# # Call the function to consolidate Excel files
# consolidate_excel_files(input_directory, output_file)

# print(f"Consolidated data saved to {output_file}")

import os
import pandas as pd

# Function to process a single Excel file
def process_excel_file(file_path):
    df = pd.read_excel(file_path, skiprows=31, engine='xlrd')  # Specify engine
    return df

# Function to process all Excel files in a directory and consolidate them
def consolidate_excel_files(directory_path, output_file):
    all_data = pd.DataFrame()
    for filename in os.listdir(directory_path):
        if filename.endswith(".xls"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            df = process_excel_file(file_path)
            all_data = pd.concat([all_data, df], ignore_index=True)

    
    all_data.to_excel(output_file, index=False)

# Provide the path to the directory containing Excel files
input_directory = "/Users/thedarkhorse/Desktop"

# Specify the output file name
output_file = "consolidated_output.xlsx"

# Call the function to consolidate Excel files
consolidate_excel_files(input_directory, output_file)

print(f"Consolidated data saved to {output_file}")

