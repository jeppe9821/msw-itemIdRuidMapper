import re
import maple
import mverse
import file
import utils
import config

def run() -> None:
    file_content:str = file.read_file(config.get("Input"))

    # Get a line of data where one match is one line
    matches:list = re.findall(r'^\s*(\d+)\s+([^\t]+)\s+(.+)$', file_content, re.MULTILINE)
    
    for match in matches:
        raw_itemId:str = match[0]
        raw_name:str = match[1]
        raw_metadata:str = match[2]
        
        itemId:int = utils.parse_itemId_from_string(raw_itemId)
        category:tuple = maple.get_category(itemId)

        # Get the MSW resource ID
        ruid:str = mverse.get_ruid(category, [raw_itemId, raw_name, str(itemId)])

        # Get the correct inventory slot for the item
        inventory_slot:int = maple.get_inventory_slot(itemId)

        # Write to file
        if inventory_slot == maple.EQUIP_INVENTORY_SLOT_ID:
            file.write_to_file(config.get("Equip_Output"), ["Id", "Name", "IconRUID", "Metadata"], [itemId, raw_name, ruid, raw_metadata])
        else:
            file.write_to_file(config.get("Item_Output"), ["Id", "Name", "IconRUID", "Description", "Metadata"], [itemId, raw_name, ruid, raw_metadata]) 

        print("Parsed item id (", itemId, " [", raw_name, "]) into category (", category[1], " [", maple.get_category_name(category[1]),"]) with ruid (", ruid, ")")
        
run()