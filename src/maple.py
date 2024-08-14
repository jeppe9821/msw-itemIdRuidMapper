SPRITE_CATEGORY:int = 0
Item:int = 10


AVATAR_CATEGORY:int = 25
Cap:int = 29
Cape:int = 30
Coat:int = 31
Gloves:int = 32
LongCoat:int = 33
Pants:int = 34
Shoes:int = 35
FaceAccessory:int = 37
EyeAccessory:int = 38
Earrings:int = 39
OneHandedWeapon:int = 40
TwoHandedWeapon:int = 41
Shield:int = 42

EQUIP_INVENTORY_SLOT_ID:int = 1000000
USE_INVENTORY_SLOT_ID:int = 2000000
SETUP_INVENTORY_SLOT_ID:int = 3000000
ETC_INVENTORY_SLOT_ID:int = 4000000


def get_category(itemId:int) -> tuple:
    if itemId >= 1000000 and itemId <= 1002857:
        return (AVATAR_CATEGORY, Cap) 

    if itemId >= 1010000 and itemId <= 1012134:
        return (AVATAR_CATEGORY, FaceAccessory)
    
    if itemId >= 1020000 and itemId <= 1022073:
        return (AVATAR_CATEGORY, EyeAccessory)
    
    if itemId >= 1032000 and itemId <= 1032061:
        return (AVATAR_CATEGORY, Earrings)

    if itemId >= 1040000 and itemId <= 1042147:
        return (AVATAR_CATEGORY, Coat)

    if itemId >= 1050000 and itemId <= 1052170:
        return (AVATAR_CATEGORY, LongCoat)

    if itemId >= 1060000 and itemId <= 1062100:
        return (AVATAR_CATEGORY, Pants)

    if itemId >= 1070000 and itemId <= 1072367:
        return (AVATAR_CATEGORY, Shoes)

    if itemId >= 1080000 and itemId <= 1082249:
        return (AVATAR_CATEGORY, Gloves)

    if itemId >= 1092000 and itemId <= 1092061:
        return (AVATAR_CATEGORY, Shield)

    if itemId >= 1102000 and itemId <= 1102194:
        return (AVATAR_CATEGORY, Cape)
    
    if itemId >= 1112000 and itemId <= 1112904:
        return (SPRITE_CATEGORY, Item) #Rings

    if itemId >= 1302000 and itemId <= 1702201:
        return (AVATAR_CATEGORY, OneHandedWeapon)
    
    if itemId >= 2000000 and itemId <= 4280001:
        return (SPRITE_CATEGORY, Item)

    raise Exception("ERROR: Could not find any category for itemId (", itemId, ")")

def get_inventory_slot(itemId:int) -> int:
    if itemId >= 1000000 and itemId < 2000000:
        return EQUIP_INVENTORY_SLOT_ID
    if itemId >= 2000000 and itemId < 3000000:
        return USE_INVENTORY_SLOT_ID
    if itemId >= 3000000 and itemId < 4000000:
        return SETUP_INVENTORY_SLOT_ID
    if itemId >= 4000000 and itemId < 5000000:
        return ETC_INVENTORY_SLOT_ID


def get_category_name(categoryId:int) -> str:
    if categoryId == Cap:
        return "Cap"
    if categoryId == FaceAccessory:
        return "FaceAccessory"
    if categoryId == EyeAccessory:
        return "EyeAccessory"
    if categoryId == Earrings:
        return "Earrings"
    if categoryId == Coat:
        return "Coat"
    if categoryId == LongCoat:
        return "LongCoat"
    if categoryId == Pants:
        return "Pants"
    if categoryId == Shoes:
        return "Shoes"
    if categoryId == Gloves:
        return "Gloves"
    if categoryId == Shield:
        return "Shield"
    if categoryId == Cape:
        return "Cape"
    if categoryId == OneHandedWeapon:
        return "OneHandedWeapon"
    if categoryId == Item:
        return "Item"
    
    raise Exception("The category id (" + str(categoryId) + ") does not have a name equivalent. Make sure to add it in maple.py")