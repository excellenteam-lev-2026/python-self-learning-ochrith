from pathlib import Path

path="C:/Users"
def get_deep_files(path):
    directory = Path(path)
    result=[]
    for file in directory.iterdir():
        if file.is_file() and file.name.startswith("deep"):
            result.append(file.name)


    return result


print(get_deep_files(path))
