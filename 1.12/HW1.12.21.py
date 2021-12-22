# #Answer1
# a. A function is a block of code which only runs when it is called
# b. def and than the function

# #Answer2
# a. Parameters allow us to pass information or instructions into functions and procedures.
# we can use also default parameters and it  makes the function  more useful
# b. need to put function name and next ()
# C. inside the parameter you can add = for example my_func(a=100)

# #Answer3
# a. Adding a description for the return, helps you and anyone else using your
# function to determine exactly what the value should be used for within the calling script or functio
# b.  with return
# c. None

# #Answer4
# a. by using the function random, randint is a random for int
# b.randon
# c. import random

# #Answer5
# import random
# def myCheckEven(nums):
#     if nums%2==0:
#         print(True)
#     else:
#         print(False)
# nums = int(input('inset a number:'))
# myCheckEven(nums)
# #Answer6
# def myAverage(lst):
#     sum_num = 0
#     for num in lst:
#         sum_num=sum_num+num
#     avg = sum_num / len(lst)
#     return avg
# print("The average is", myAverage([50,5,555,44,85]))
# #Answer7
# def mycalculationadd(x=0,y=0):
#     add=x+y
#     return add
#
# def mycalculationsub(x=0, y=0):
#     sub=x-y
#     return sub
#
# def mycalculationmul(x=0, y=0):
#     mul=x*y
#     return mul
#
# def mycalculationdiv(x=0, y=0):
#     div=x/y
#     return div
# xnum=int(int(input('insert x number: ')))
# ynum=int(int(input('insert y number: ')))
#
# print(mycalculationadd(xnum,ynum))
# print(mycalculationsub(xnum,ynum))
# print(mycalculationmul(xnum,ynum))
# print(mycalculationdiv(xnum,ynum))



#Answer8
def findMinMax(nums): #------------------dont know :( I tried may options, something I am missing
    min = max = nums[0]
    for num in nums[1:]:
        if num >= 10:
            min = num
    for num in nums[1:]:
        if num <= 100:
            max=num
    return max,min
print(findMinMax([1, 2, 11, 15, 20,555]))
# # #Answer9
# import random
#
# the_number = random.randint(1, 100)
# guess = int(input("Take a guess: "))
# tries = 1
#
# # guessing loop
# while guess != the_number:
#     print("Lower..." if guess > the_number else "Higher")
#     guess = int(input("Take a guess: "))
#     tries += 1
#     if guess == the_number:
#         print("You guessed it! The number was", the_number)
#         print("And it only took you", tries, "tries!\n")
#         break
