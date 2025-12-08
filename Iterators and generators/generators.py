def integers():
    i=1
    while True:
        yield i
        i=i+1

def square():
    for i in integers():
        yield i*i

def take(n,seq):
    seq=iter(seq)
    r=[]
    try:
        for i in range(n):
            r.append(next(seq))
    except StopIteration:
        pass
    return r
print(take(5,square()))

