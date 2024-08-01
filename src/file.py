import os
import re

def read_file(path) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def __get_file(path:str):
    fileHasContent:bool = False

    try:
        fileHasContent:bool = os.path.getsize(path) > 0
    except Exception:
        pass
    
    if fileHasContent:
        file = open(path, "a", encoding="utf-8")
    else:
        file = open(path, "w+", encoding="utf-8")

    return file

def write_list_to_file(path:str, list:list) -> None:
    file = __get_file(path)

    line = "\t".join(str(i) for i in list) + "\n"

    line = line.replace("\n", "")

    line = line + "\n"

    file.write(line)
    file.close()