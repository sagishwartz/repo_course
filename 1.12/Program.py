# import a module
import random

# generate some random numbers in range
for n in range(4):
    print(random.randint(2,6))

# another numbers generation
die1=random.randint(1,6)
die2=random.randint(1,6)
print(f'dice are {die1} and {die2}')

# generate decimal number in range
print(f'{random.uniform(1, 2):.2f}')


# declaration of function
def printMinInList(nums):
    min = nums[0]
    for num in nums[1:]:
        if num < min:
            min = num
    print(f'lowest number is {min}')

# calling (using) a function
printMinInList([5,8,3])
printMinInList([4,9,7])

# function with no parameters
def printHyphens():
    for n in range(20):
        print('-',end='')
    print()

printHyphens()
printHyphens()

# function with parameter
def sayHello(name):
    print(f'Hello {name}')

sayHello('Eitan')
sayHello('Nathan')

# function with default parameter
def printPerson(name,age,city='Ramat Gan'):
    print(f'hello {name} aged {age} from {city}')

# set all parameters
printPerson('Itzik',12,'Haifa')

# use the default value
name1='Shahar'
printPerson(name1,26)

# set values by parameter name
printPerson(age=34,name='Gal')

# function with return value
def getCirclePerimeter(radius):
    per=2*3.14*radius
    return per

print(getCirclePerimeter(4))

# another function with return value
def findMinInList(nums):
    min = nums[0]
    for num in nums[1:]:
        if num < min:
            min = num
    return min

print(findMinInList([3,9,1]))

# return can end a loop
def findDivisilbleBy100(list1):
    for num in list1:
        if num%100==0:
            return num
    return None

lst=[34,5,400,508,600]
print(findDivisilbleBy100(lst))
