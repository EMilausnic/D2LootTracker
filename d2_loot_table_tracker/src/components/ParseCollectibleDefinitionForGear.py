import json

# Load JSON files
with open('d2_loot_table_tracker/partially_parsed_file.json', 'r') as file:
    original_data = json.load(file)

with open('d2_loot_table_tracker/DestinyInventoryItemLiteDefinition.json', 'r') as file2:
    lookup_data = json.load(file2)
items_to_remove = []

# Iterate through items in original file
for item_id, item_data in original_data.items():
    # Look up corresponding information from lookup file
    if str(item_data['itemHash']) in lookup_data:
        item_info = lookup_data[str(item_data['itemHash'])]
        if 'itemTypeDisplayName' in item_info:
            item_type_display_name = item_info['itemTypeDisplayName']
            item_data['itemTypeDisplayName'] = item_type_display_name

        if 'itemTypeAndTierDisplayName' in item_info:
            item_tier_display_name = item_info['itemTypeAndTierDisplayName']
            item_data['itemTypeAndTierDisplayName'] = item_tier_display_name

    # Remove unwanted fields if necessary
    del item_data['redacted']  # Example of removing 'sourceString' field
    del item_data['blacklisted']  # Example of removing 'sourceString' field
    
    

    allowed_weapon_types = ["Sword", "Shotgun", "Scout Rifle", "Submachine Gun", "Linear Fusion Rifle", "Glaive", "Grenade Launcher", "Fusion Rifle", "Sidearm", "Combat Bow", "Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sniper Rifle", "Grenade Launcher", "Trace Rifle", "Machine Gun"]
    allowed_armor_types = ["Gauntlets", "Helmet", "Chest Armor", "Leg Armor", "Hunter Cloak", "Warlock Bond", "Titan Mark"]

    allowed_gear_types = ["Sword", "Shotgun", "Scout Rifle", "Submachine Gun", "Linear Fusion Rifle", "Glaive", "Grenade Launcher", "Fusion Rifle", "Sidearm", "Combat Bow", "Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sniper Rifle", "Grenade Launcher", "Trace Rifle", "Machine Gun", "Gauntlets", "Helmet", "Chest Armor", "Leg Armor", "Hunter Cloak", "Warlock Bond", "Titan Mark"]
    # # Add items to remove list
    # if item_data['sourceString'] == "Source: Eververse" or 'Ornament' in item_data.get('itemTypeDisplayName', ''):
    #     items_to_remove.append(item_id)

    # now remove everything that is not a piece of gear
    if item_data['sourceString'] == "Source: Eververse" or 'Ornament' in item_data.get('itemTypeDisplayName', '') or item_data.get('itemTypeDisplayName', '') not in allowed_gear_types:
        items_to_remove.append(item_id)


    # # remove items only earned in eververse
    # if item_data['sourceString'] == "Source: Eververse":
    #     del original_data[item_id]

    # # remove armor and weapon orniments
    # if ('Ornament' in item_data['itemTypeDisplayName']):
    #     del original_data[item_id]
        
# Remove items marked for removal
for item_id in items_to_remove:
    del original_data[item_id]
# Write modified JSON data to a new file
with open('modified_file.json', 'w') as file:
    json.dump(original_data, file, indent=4)