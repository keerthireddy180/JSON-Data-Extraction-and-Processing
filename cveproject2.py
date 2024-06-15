import json

def extract_details(data, path=None):
    # Initialize results and path tracking for nested items
    results = []
    if path is None:
        path = []

    # Check if the current data is a dictionary and process accordingly
    if isinstance(data, dict):
        # Temporary storage for current level details
        current_details = {}
        for key, value in data.items():
            if key in ['product', 'vendor', 'version', 'datePublished', 'dateUpdated']:
                current_details[key] = value
            elif isinstance(value, (dict, list)):
                # Recursive call to process nested dictionaries or lists
                results += extract_details(value, path + [key])
        if current_details:
            results.append(current_details)

    # Process each item if it's a list
    elif isinstance(data, list):
        for item in data:
            results += extract_details(item, path + ["list_item"])

    return results

# Replace 'your_file_path_here' with the path to your CVE JSON file
with open('C:/Users/dhanr/Downloads/CVE-2019-5016-2.json', 'r', encoding='utf-8') as file:
    cve_data = json.load(file)

extracted_data = extract_details(cve_data)
print(extracted_data)
