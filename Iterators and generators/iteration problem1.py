class Reviteration:
    def __init__(self,list):
        self.list=list
        self.i=len(list)-1
    def __iter__(self):

        return self
    def __next__(self):
        if self.i>=0:
           value=self.list[self.i]
           self.i -=1
           print(value)

r=Reviteration([10,20,30,40,50])
for x in r:
    pass

