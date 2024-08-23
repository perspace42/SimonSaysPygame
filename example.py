'''
I am
a multi line comment
'''
# I am a single line comment

#importing example
import platform
print("import example:\n")
print(platform.python_version())

#function example
print("function example:\n")
def functionName(any,num : int):
    num += 1
    print(any,num)

functionName("I am a string + ",100)
functionName(num = 100, any = 2)

#Variables example
Integer = 1
Float = 1.0
Boolean = True or False
List = [1,2,None,True,1.0]
Nothing = None
Tuple = (1,2)

Value = List[0] #contains a value of 1
List[0] = 500 #modifies the value to 500

Tuple = (1,2,3) #Tuples cannot be modified but can be reassigned

#class example
class Polygon():
    def __init__(self,numSides: int):
        self.numSides = numSides
    
    def display(self):
        print("Is a polygon with: ",self.numSides, " sides.")

print("class example:\n")
shape = Polygon(2)
shape.display()

#class inheritance example
class Square(Polygon):
    def __init__(self,numSides: int, length: int):
        Polygon.__init__(self,numSides)
        self.length = length

    #override
    def display(self):
        super().display()
        print("Is a Square with a side length of: ", self.length)

print("class inheritance example:\n")
box = Square(1,4)
box.display()