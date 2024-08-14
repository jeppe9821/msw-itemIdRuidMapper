import re
import maple
import mverse
import file
import utils
import config
import fileheader

def __find_header(headerName:str, headers:list):
    for i in range(len(headers)):
        if headerName in headers[i]:
            return i

def __parse_metadata(metadata:str, headers:list, output_values:list) -> None:
    result = []
    
    for _ in range(len(headers) - len(output_values)):
        output_values.append('null')

    findAllMetadataProperties = re.finditer(r'((?!\s{2,}|\t)[\s\S]+?)+', metadata, re.MULTILINE)

    for keyValuePair in findAllMetadataProperties:        
        if '=' not in keyValuePair[0]:
            continue

        split:list = keyValuePair[0].split('=')
        key:str = split[0].strip()
        value:str = split[1].replace(",", "").strip()

        index:int = __find_header(key, headers)

        output_values[index] = value

def handle_equip(match:list, headers:list, output_values:list) -> None:
    raw_metadata:str = match.pop(0)

    descriptionFindSplit:list = raw_metadata.split(',')
    description:str = descriptionFindSplit[len(descriptionFindSplit) - 1]

    if(len(description.strip()) > 2):
        output_values[2] = description
    else:
        output_values[2] = "null"

    raw_metadata = raw_metadata.replace(description, "")

    __parse_metadata(raw_metadata, headers, output_values)

    file.write_list_to_file(config.get("Equip_Output"), output_values) 

def handle_use(match:list, headers:list, output_values:list) -> None:
    raw_description:str = match.pop(0)
    raw_metadata:str = match.pop(0)

    output_values[2] = raw_description

    __parse_metadata(raw_metadata, headers, output_values)

    file.write_list_to_file(config.get("Item_Output"), output_values) 
    
def handle_setup(match:list, headers:list, output_values:list) -> None:
    raw_description:str = match.pop(0)
    raw_metadata:str = match.pop(0)

    output_values[2] = raw_description

    __parse_metadata(raw_metadata, headers, output_values)

    file.write_list_to_file(config.get("Setup_Output"), output_values) 


def handle_etc(match:list, headers:list, output_values:list) -> None:
    raw_description:str = match.pop(0)
    raw_metadata:str = match.pop(0)

    output_values[2] = raw_description

    __parse_metadata(raw_metadata, headers, output_values)

    file.write_list_to_file(config.get("Etc_Output"), output_values)

def handle_writetofile(invslot:int, match:list, headers:list, output_values:list) -> None:
    if invslot == maple.EQUIP_INVENTORY_SLOT_ID:
        handle_equip(match, headers[0], output_values)
    if invslot == maple.USE_INVENTORY_SLOT_ID:
        handle_use(match, headers[1], output_values)
    if invslot == maple.SETUP_INVENTORY_SLOT_ID:
        handle_setup(match, headers[2], output_values)
    if invslot == maple.ETC_INVENTORY_SLOT_ID:
        handle_etc(match, headers[3], output_values)

def run() -> None:
    file_content:str = file.read_file(config.get("Input"))

    headers = fileheader.collect_headers(file_content)

    file.write_list_to_file(config.get("Equip_Output"), headers[0])
    file.write_list_to_file(config.get("Item_Output"), headers[1])
    file.write_list_to_file(config.get("Setup_Output"), headers[2])
    file.write_list_to_file(config.get("Etc_Output"), headers[3])

    # Get a line of data where one match is one line
    # (\d+)\t+([^\t]+)\t([\s\S]+?)\t([^\n]+)
    matches:list = re.findall(r'(\d+)\t+([^\t]+)\t([^\n]+)', file_content, re.MULTILINE)
    
    for match in matches:
        match = list(match)

        raw_itemId:str = match.pop(0)

        itemId:int = utils.parse_itemId_from_string(raw_itemId)
        category:tuple = maple.get_category(itemId)
        inventory_slot:int = maple.get_inventory_slot(itemId)

        raw_name:str = match.pop(0)

        # Get the MSW resource ID
        ruid:str = mverse.get_ruid(category, [raw_itemId, raw_name, str(itemId)])

        if(ruid == None):
            ruid = 'null'

        output_values = [itemId, raw_name, "null", ruid]

        handle_writetofile(inventory_slot, match, headers, output_values)

        print("Parsed item id (", itemId, " [", raw_name, "]) into category (", category[1], " [", maple.get_category_name(category[1]),"]) with ruid (", ruid, ")")
        
run()