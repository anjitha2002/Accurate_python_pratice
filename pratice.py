yellow = (255, 255, 0)

r, g, b = yellow
print(r,g,b)



def square(x):
    return x*x
print(square(3)+square(2))


x = 0
y = 0
def incr(x):
    y = x + 1r
    return y
incr(1)
print(incr(3), y)

pi = 3.14
def area(r):
    return pi * r * r
print(area(3))


x = 5
def f():
    return x*x
print(x)
print(f())

x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)


x = 1
def f():
        y = 6
        x = 2
        return x + y
print(x)
print(f())
print(x)


x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)


print(2 < 3 and not 3 > 1)

x = 4
y = 5
p = x < y or x < z
print(p)

x = 2
if x == 2:
    print(x)
else:
    x +

x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)r
x[2] = 2
print(x)

for x in [1, 2, 3, 4]:
    print(x)

for i  in range(10):
   print(i, i*i, i*i*i)

x=max([1,3,8])
print(x)


