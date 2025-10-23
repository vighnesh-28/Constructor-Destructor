class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Hello,Good Morning Everyone,My Name is" , self.name)
    def __del__(self):
        print("object destroyed")
        
#driver code
name=Student("vighnesh")
name.display()
del name2
name2=Student("Veera")
name2.display()




