# Problem 17: Write a program reverse.py to print lines of a file in reverse order.
f=open('f1.txt','r')
lines=f.readlines()
lines.reverse()
for line in lines:
    print(line,end="")

# Problem 18: Write a program to print each line of a file in reverse order.
f=open('f1.txt','r')
for line in f:
    print(line.rstrip()[::-1])

# #     Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
#
# f=open('f1.txt','r')
# lines=f.readlines()
# print("head lines")
# for i in lines[:10]:
#     print(i,end="")
#     print("tail lines")
# for i in lines[-10:]:
#     print(i,end="")


# Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?
def word_warap(text, width):

    words = text.split()
    line = " "

    for w in words:
        if len(line)+len(w)+1<=width:
            if line == " " :
                line=w
            else:
                line += " "+w
        else:
            # print(line)
            line=w
    if line:
        print(line)
file = open('f1.txt', 'r')
for line in file:
    print(word_warap(line,70))

