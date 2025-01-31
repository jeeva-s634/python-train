def ASCII(x):
    if type(x)==str:
        return ord(x)
    return(x)
list=["A",-20,'a',94,66]
list.sort(key=ASCII)
print(list)
