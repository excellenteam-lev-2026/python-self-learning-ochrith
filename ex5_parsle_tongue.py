#parsle_tongue
#you have to be in the directory where logo.jpg is located
import re


def open_file_carefully(path):

    pattern = re.compile(b"[a-z]{5,}!")  #format regex
    with open(path,'rb') as f :
        for line in f :
            result= pattern.findall(line)
            if result:
                yield result


for t in open_file_carefully("./logo.jpg"):
    for i in t:
        print(i)
