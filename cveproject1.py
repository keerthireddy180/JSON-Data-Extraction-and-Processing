import json

def print_cve_details(data, depth=0):
    indent = "    " * depth  # Create indentation based on the depth of recursion
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                print(f"{indent}CVE Key: {key}")
                print_cve_details(value, depth + 1)
            elif isinstance(value, list):
                print(f"{indent}CVE Key: {key}")
                for item in value:
                    print_cve_details(item, depth + 1)
            else:
                print(f"{indent}CVE Key: {key}")
                print(f"{indent}Value: {value}")
    elif isinstance(data, list):
        for item in data:
            print_cve_details(item, depth + 1)

# Load the CVE JSON data
with open('C:/Users/dhanr/Downloads/CVE-2019-5016-2.json', 'r', encoding='utf-8') as file:
    cve_data = json.load(file)

# Print the CVE details
print_cve_details(cve_data)
