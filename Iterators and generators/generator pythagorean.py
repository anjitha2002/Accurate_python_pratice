def pythagorean():
    z=1
    while True:
        for x in range(1,z):
            for y in range(x,z):
                if x*x+y*y==z*z:
                    yield(x,y,z)
        z +=1

def take(n,seq):
    seq=iter(seq)
    r=[]
    try:
        for i in range(n):
            r.append(next(seq))
    except StopIteration:
        pass
    return r
print(take(10,pythagorean()))
