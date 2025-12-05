# problem 4
# Implement a function product, to compute product of a list of numbers.

def product(list):
    result=1
    for x in list:
        result=result*x
    return result
print(product([1,2,3]))


# problem 5
#  Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def factorial(n):
    numbers=[]
    for i in range(1,n+1):
        numbers.append(i)
    return product(numbers)
print(factorial(5))

# Problem 8:
# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

def cum_sum(list):
    result=[]
    sum=0
    for x in list:
        sum=sum+x
        result.append(sum)
    return result
print(cum_sum([1,2,3]))


# problem 9
# cumulative product
def cum_product(list):
    r=[]
    pr=1
    for x in list:
        pr=pr*x
        r.append(pr)
    return r
print(cum_product([1,2,3]))

# Problem 11: Write a function dups to find all duplicates in the list.

def dups(list):
    duplicate=[]
    seen=[]
    for x in list:
        if x in seen and x not in duplicate:
            duplicate.append(x)
        else:
            seen.append(x)
    return duplicate
print(dups([3,2,4,1,3,2,5,7]))

# Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(list,size):
    result=[]
    for i in range(0,len(list),size):
        result.append(list[i:i+size])
    return result
print(group([1,2,3,4,5,6,7,8],3))




