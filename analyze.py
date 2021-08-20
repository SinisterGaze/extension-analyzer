import os 

def find_extension(file):
    index = file.rfind('.')
    if index != -1:
        return file[index:]
    else:
        return ""

def count_frequency(elements):
    counter = {}
    for item in elements:
        if item in counter:
            counter[item]+=1
        else:
            counter[item] = 1
    return counter

def sort_dict(d, reverse = True):
    keys = sorted(d, key = d.get, reverse=reverse)
    values = sorted(d.values(), reverse=reverse)
    return dict(zip(keys,values))

def get_ext_types(PATH):
    os.chdir(PATH)
    ext_types = []

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        dirnames[:] = [d for d in dirnames if not d[0] == "."]
        filenames[:] = [file for file in filenames if not file[0] == "."]
        exts = [find_extension(file) for file in filenames]
        exts = [ext for ext in exts if '.' in ext]
        ext_types.extend(exts)

    return count_frequency(ext_types)

def display(ext_dict):
    print(f"Type    -   Frequency")
    print(f"---------------------")
    for ext, freq in ext_dict.items():
        print(f"{ext}    -    {freq}")





if __name__ == "__main__":
    DIR_PATH = input("Enter the desired path to analyze: ")
    exts = sort_dict(get_ext_types(DIR_PATH))
    display(exts)