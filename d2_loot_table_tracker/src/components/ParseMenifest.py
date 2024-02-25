#####################################################################
#####################################################################

# now that I am using the d2 manifest, 

import json

# Load the original JSON file
with open('d2_loot_table_tracker\DestinyCollectibleDefinition.json', 'r') as f:
    original_data = json.load(f)

# Initialize an empty dictionary to store the simplified data
simplified_data = {}

# List of fields to keep in the simplified dictionary
fields_to_keep = ['displayProperties', 'sourceString', 'sourceHash', 'itemHash', 'parentNodeHashes', 'hash', 'index', 'redacted', 'blacklisted']

# Iterate through each element in the original dictionary
for key, value in original_data.items():
    # Initialize a new dictionary for the simplified data of this element
    simplified_element = {}
    # Iterate through the fields we want to keep
    for field in fields_to_keep:
        # Check if the field exists in the original data
        if field in value:
            # Add the field to the simplified element
            simplified_element[field] = value[field]
    # Add the simplified element to the simplified data dictionary
    simplified_data[key] = simplified_element

# Save the simplified data to a new JSON file
with open('file_without_cosmetics.json', 'w') as f:
    json.dump(simplified_data, f, indent=4)

#####################################################################
#####################################################################
    
# import pickle
# import json
# # Open the manifest.pickle file for reading
# with open('Manifest.pickle', 'rb') as f:
#     # Deserialize the contents of the pickle file
#     manifest_data = pickle.load(f)

# # Initialize an empty list to store items with 'itemName'
# items_with_name = []

# # Iterate over the dictionary and filter out items with 'itemName'
# destinationDict = manifest_data['DestinyInventoryItemDefinition']    
# for key, val in destinationDict.items():
#     print()
#     print(key)
#     print(val)
#     items_with_name.append(key)
#     items_with_name.append(val)
# #     if 'itemName' in value:
# #         print(value)

# # Define the output file path
# output_file_path = 'DestinyInventoryItemDefinition.json'

# # Write the filtered data to a JSON file
# with open(output_file_path, 'w') as f:
#     json.dump(items_with_name, f, indent=4)

# print(f"Filtered data containing 'itemName' has been written to '{output_file_path}'")
