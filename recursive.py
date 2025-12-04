#recursive function
def count_down(n):
    print(n)
    n=n-1
    if(n>0):
        count_down(n)
    else:
        pass
count_down(3)

#factoria
def factorial(n):

    if n==1:
        return 1

    else:
        return n * factorial(n-1)

num=int(input("Enter the number"))
print(factorial(num))

#sum of numebers
def sum(n):

    if n==1:
        return 1

    else:
        return n + sum(n-1)

num=int(input("Enter the number"))
print(sum(num))