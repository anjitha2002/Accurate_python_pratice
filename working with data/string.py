# Problem 13: Write a function lensort to sort a list of strings based on length.

def lensort(words):
    return sorted(words,key=len)
words=['apple','banana','strawberry','pl']
print(lensort(words))


# Problem 16: Write a function extsort to sort a list of files based on extension.
def extsort(list):
    return sorted(list,key=len)
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))