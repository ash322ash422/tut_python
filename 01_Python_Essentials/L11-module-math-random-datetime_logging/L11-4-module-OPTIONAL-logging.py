import logging
from datetime import datetime
import csv

# This script reads a CSV file, searches for specific data, and prints matching results.
# It logs each step of the process (file reading, searching, errors) into a log file for tracking and debugging.

# Logging Levels:
# logging.info() → normal steps
# logging.warning() → something unexpected
# logging.error() → failures


# --------------------------------------------------
# Step 0 : Logging setup
# --------------------------------------------------

logging.basicConfig(
    filename="etl_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Pipeline Started")


# --------------------------------------------------
# Step 1 : Read CSV File
# --------------------------------------------------

def read_csv(file_path):
    data = []
    try:
        logging.info(f"Trying to read file: {file_path}")
        
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        
        logging.info(f"File read successfully. Total records: {len(data)}")
    
    except Exception as e:
        logging.error(f"Error reading file: {e}")
    
    return data


# --------------------------------------------------
# Step 2 : Search Function
# --------------------------------------------------

def search_data(data, column, value):
    try:
        logging.info(f"Searching for value '{value}' in column '{column}'")
        
        results = [row for row in data if row[column].lower() == value.lower()]
        
        logging.info(f"Search completed. Matches found: {len(results)}")
        return results
    
    except Exception as e:
        logging.error(f"Error during search: {e}")
        return []


# --------------------------------------------------
# Step 3 : Main Execution
# --------------------------------------------------

def main():
    file_path = "data_sample.csv"
    
    data = read_csv(file_path)
    
    if not data:
        logging.warning("No data available to search")
        return
    
    # Example search
    column = "name"
    value = "Alice"
    
    results = search_data(data, column, value)
    
    print("Search Results:")
    for r in results:
        print(r)

    logging.info("ETL Pipeline Completed Successfully")


# --------------------------------------------------
# Run Program
# --------------------------------------------------

if __name__ == "__main__":
    main()
