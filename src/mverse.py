import requests
import config

API_URL:str = config.get("API_Mverse")

def get_ruid(category:tuple, tags:list) -> str:
    for tag in tags:
        mverse_data:dict = __get_http_mverse_data(tag, category)
        ruid:str = __try_get_ruid(tag, mverse_data)

        if ruid:
            return ruid

def __try_get_ruid(tag:str, mverse_data:dict) -> str:
    try:
        return __get_ruid_from_json_data(mverse_data)
    except TagCannotBeUsed as e:
        print("The tag (", tag, ") could not be used to find RUID. Retrying with another tag. Error message: [", e.message, "]")
        return ""

def __get_http_mverse_data(tag:str, category:tuple) -> dict:
    
    params = {
        "count": 150,
        "page": 1,
        "category": str(category[0]) + "," + str(category[1]),
        "sort": 0,
        "tag": tag
    }

    result:dict = {}

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    result = response.json()
    
    return result

def __get_ruid_from_json_data(json_data:dict) -> str:
    if "data" in json_data and "matches" in json_data["data"] and json_data["data"]["matches"]:
        matches = json_data["data"]["matches"]
        if len(matches) > 1:
            raise TagCannotBeUsed("There are too many matches! The item id cannot be used as a tag")
        else:
            return matches[0]["guid"]
    raise TagCannotBeUsed("There was no results")


class TagCannotBeUsed(Exception):
    """Raised when the tag cannot be used as a search index for MSW resources"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    pass