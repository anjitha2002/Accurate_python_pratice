a=[1,2,3,4,5,6,7,8,9]
even_no=[x for x in a if x%2==0]
print(even_no)


a=[1,2,3,4]
b=[2,3,5,7]
new=zip(a,b)
nlist=[x+y for x,y in new]
print(nlist)

newlist=[(x,y) for x in range(5) for y in range(5) if x%2 ==0 ]
print(newlist)

newlist=[(x,y) for x in range(5) for y in range(x) if x%2 ==0 ]
print(newlist)

newlist=[(x,y) for x in range(5) for y in range(5) if x%2 ==0 and x!=y]
print(newlist)



# pythagorean triplets

n=25
triplet=[(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x*x +y*y==z*z ]
print(triplet)

# map
def square(x):
    return x*x
num= list(map(square,range(5)))
print(num)

# filter
def even(x):
    return x%2==0
num= list(filter(even,range(5)))
print(num)

# enumerates
for index,value in enumerate(["a","b","c"]):
    print(index,value)


