import csv
import re

# Function to extract unique ID and convert it to the second URL
def convert_url(first_url):
    # Extracting unique ID using regular expression
    unique_id = re.search(r'/([0-9a-fA-F-]+)\?', first_url).group(1)
    # Constructing the second URL
    second_url = f'https://tulser.askme.nl/ContentV2/Content/tulser/RetrieveContent/{unique_id}'
    return second_url

# Path to your CSV file
csv_file_path = "links_complete.csv"

# Open the CSV file and read URLs from it
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header row if present
    next(csv_reader, None)
    # Process each row
    for row in csv_reader:
        # Assuming the URL is in the first column of each row
        first_url = row[0]
        # Convert the first URL to the second URL
        second_url = convert_url(first_url)
        
        with open("converted_links.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([second_url])

