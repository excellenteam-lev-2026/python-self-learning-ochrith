

def join(*lists,sep="_"):
    result=[]

    for l in lists:
        result=result+[sep]+l
    return result[1:]





