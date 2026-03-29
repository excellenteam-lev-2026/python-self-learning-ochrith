
#for this exercice ,all the element are list of the same size
def interleaves(*args):

    for i in range(len(args[0])):
        for item in args:
            yield item[i]

#test with example
result=[]
for item in interleaves('abc', [1, 2, 3], ('!', '@', '#')):
    result=result+[item]

print(result)

