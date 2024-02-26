import json

__config_file_path:str = 'config.json'

with open(__config_file_path, 'r') as file:
    __config_data:str = json.load(file)

def get(key:str) -> str:
    return __config_data[key]