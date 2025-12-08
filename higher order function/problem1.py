
# Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.

def product(a,b):
    if b==0:
        return 0
    elif b>0:
        p=a+product(a,b-1)
        return p
    elif b<0:
        p=-product(a,-b)
        return p
    else:
        pass

print(product(3,5))
print(product(2,7))
print(product(6,-8))