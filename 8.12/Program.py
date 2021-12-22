list1=[ 60,20,30,40,50,60,70,80,60 ]

# create a list based on anther list with filtered members
list2=[]
for num in list1:
    if num!=60:
        list2.append(num)
print(list2)

# same task using list comprehension
list2=[num for num in list1 if num!=60 ]
print(list2)

# create list using more complex filter
list2=[num for num in list1 if num not in [60,80] ]
print(list2)

# list comprehension syntax
#[ <expression of arg> for <arg> in <list> if <condition> ]

# create list of power 2 of numbers in another sequence
list2=[ num*num for num in range(1,11) ]
print(list2)

# create list of first letters from words in another list
list1=['Keep','It','Simple','Stupid']
list2=[ word[0] for word in list1 ]
print(list2)

# create list of first 2 letters of words in another list with filter
listofWords = ["hello", "python", "world", "experts", "fun"]
first2=[ word[:2] for word in listofWords if word!="experts" ]
print(first2)

# create list of even numbers from another list
nums=[2, 6, 11, 200, -20, 3]
print([num for num in nums if num % 2 == 0])

# create list of random numbers
import random
rand_nums = [ random.randint(1,100) for num in range(10) ]
print(rand_nums)

# syntax for if-else block in one line
size=input('big or small?: ')
print('Tel Aviv') if size=='big' else print('Jaffa')

# regular if-else block
if size=='big':
    print('Tel Aviv')
else:
    print('Jaffa')