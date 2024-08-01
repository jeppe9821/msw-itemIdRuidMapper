import re
import maple
import file
import utils
import config

def __handle_metadata(metadata:str, original:list) -> list:
    result = []
    
    findAllMetadataProperties = re.finditer(r'((?!\s{2,}|\t)[\s\S]+?)+', metadata, re.MULTILINE)

    for m in findAllMetadataProperties:
        str = m[0]
        
        if '=' not in str:
            continue
        split = str.split('=')
        split[0] = split[0].strip()
        if split[0] not in original:
            result.append(split[0])

    return result

def __handle_equip(match:list, original:list) -> list:
    metadata = match.pop(0)

    return __handle_metadata(metadata, original)

def __handle_use(match:list, original:list) -> list:
    description = match.pop(0)
    metadata = match.pop(0) 

    return __handle_metadata(metadata, original)   

def __handle_setup(match:list, original:list):
    description = match.pop(0)
    metadata = match.pop(0)

    return __handle_metadata(metadata, original)

def __handle_etc(match:list, original:list):
    description = match.pop(0)
    metadata = match.pop(0)

    return __handle_metadata(metadata, original)

def __handle(invslot:int, match:list, original:tuple) -> list:
    result_equip = []
    result_use = []
    result_setup = []
    result_etc = []

    if invslot == maple.EQUIP_INVENTORY_SLOT_ID:
        result_equip.append(__handle_equip(match, original[0]))
    if invslot == maple.USE_INVENTORY_SLOT_ID:
        result_use.append(__handle_use(match, original[1]))
    if invslot == maple.SETUP_INVENTORY_SLOT_ID:
        result_setup.append(__handle_setup(match, original[2]))
    if invslot == maple.ETC_INVENTORY_SLOT_ID:
        result_etc.append(__handle_etc(match, original[3]))

    return (result_equip, result_use, result_setup, result_etc)

def collect_headers(file_content:str) -> list:
    # Get a line of data where one match is one line
    matches:list = re.findall(r'(\d+)\t+([^\t]+)\t([\s\S]+?)\t([^\n]+)', file_content, re.MULTILINE)
    
    baseheaders = ["Id", "Name", "Description", "IconRUID"]

    result = ([], [], [], [])

    for match in matches:
        match = list(match)

        raw_itemId:str = match.pop(0) #Ignore
        itemId:int = utils.parse_itemId_from_string(raw_itemId)
        inventory_slot:int = maple.get_inventory_slot(itemId)
        
        raw_name:str = match.pop(0) #Ignore

        r = __handle(inventory_slot, match, result)

        for x in range(len(result)):
            for i in r[x]:
                for j in i:
                    result[x].append(j)

        result = list(result)

    for x in range(len(result)):
        result[x] = sorted(result[x])
        for baseHeader in reversed(baseheaders):
            result[x].insert(0, baseHeader)

    print(result)

    return result