'''
I am
a multi line comment
'''
# I am a single line comment

#importing example
import platform
print("import example:")
print(platform.python_version())

#function example
print("\nfunction example:")
def functionName(any,num : int):
    num += 1
    print(any,num)
    return None

functionName("I am a string + ",100)
functionName(num = 100, any = 2)
print(functionName(1,1))

#Variables example
Integer = 1
Float = 1.0
Boolean = True or False
       #0,1,  2,   3,  4
List = [1,2,None,True,1.0]
Nothing = None
Tuple = (1,2)

Value = List[0] #contains a value of 1
List[0] = 500 #modifies the value to 500 list is now [500,2,None,True,1.0]

Tuple = (1,2,3) #Tuples cannot be modified but can be reassigned
List[0] = Tuple[0] #List is back to its original value of 1

#class example
class Polygon():
    def __init__(self,numSides: int):
        self.numSides = numSides
    
    def display(self):
        print("Is a polygon with: ",self.numSides, " sides.")

print("\nclass example:")
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

print("\nclass inheritance example:")
box = Square(1,4)
box.display()

#conditions example
print("\nconditions example:")
x: int = 3
y = 5
if x == y:
    print("x is equal to y")
elif(not x == y):
    print("x is not equal to y")
else:
    print("x is neither equal nor not equal to y")

match(x):
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x does not match any of the case statements")

print("Conditionals:")
print (True != False) #True
print (x > 3) #False
print (x < 3) #False
print (x <= 3) #True
print (x >= 3) #True
print (x == y and True) #False
print (x == y or True) #True

#for loop example
print("\nfor loop example:")
#range(start, end, increment)
for i in range(0,3,1):
    print(i)

print("\nfor loop example 2:")
for item in [None,True,False,100]:
    print(item)


#Collection Slice
print("\nCollection Slice Example")
        #0,1,2,3,4,5
whole = [1,2,3,4,5,6]
length = len(whole) #6
#Slice Operator Start: End: Increment
print(whole[3:length])
print(whole[:])
