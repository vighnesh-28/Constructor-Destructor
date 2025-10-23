class Student:
    def __init__(self,name):
        self.name = name
    def display (self):
        print('Hello,Good Morning Everyone,My Name is' , self.name)
name =Student('T.Vighnesh')
#driver code
name.display()
