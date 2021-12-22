#Solution 1
name=input('Please provide a name?: ')
print('t' in name)

#-----------------------------------

#Solution 2
num=int(input('Please provide a number?: '))
if num > 5:
    print('ABOVE')
else:
    print('BELOW')

#-----------------------------------

#Solution 3
sideA=int(input('side a: '))
sideB=int(input('side b: '))
sideC=(sideA**2 + sideB**2)**0.5
print(sideC)
