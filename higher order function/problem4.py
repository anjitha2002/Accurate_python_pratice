# Problem 4: Write a function treemap to map a function over nested list.

def Treemap(fn,list):
    result=[]
    for item in list:
        if type(item)==list:
            result.append(Treemap(fn,item))
        else:
            result.append(fn(item))
    return result
print(Treemap(lambda x: x * 2,[1, 2, [3, 4, [5]]]))