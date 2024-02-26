import os

def read_file(path) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
    
def write_to_file(path:str, columnNames:list, row:list) -> None:
    fileHasContent:bool = False

    try:
        fileHasContent:bool = os.path.getsize(path) > 0
    except Exception:
        pass

    file = open(path, "a", encoding="utf-8")

    if not fileHasContent:
        header_line = "\t".join(str(column) for column in columnNames) + "\n"
        file.write(header_line)


    line = str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n"

    file.write(line)
    file.close()