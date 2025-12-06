class Iteration:
    def __init__(self):
        self.n=int(input("Enter the number:"))
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i +=1
            print(i)

        else:
            raise StopIteration

i=Iteration()
for x in i :
    pass


