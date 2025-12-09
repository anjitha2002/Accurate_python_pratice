# Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(d,parent=""):
    result={}
    for key,value in d.items():
        if parent=="":
            new_key=parent+key
        else :
            new_key=parent+"."+key

        if type(value) is dict:
            result.update(flatten_dict(value,new_key))
        else:
            result[new_key]=value
    return result
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
