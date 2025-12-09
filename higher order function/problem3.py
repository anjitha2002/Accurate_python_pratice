
# Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict(d):
    result={}

    for key,value in d.items():
        part=key.split(".")
        t=result

        for p in part[:-1]:
            if p not in t:
                t[p]={}
                t=t[p]

        t[part[-1]]=value
    return result
print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
