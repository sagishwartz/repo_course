# #Answer1
# first = input('first name: ')
# last = input('last name: ')
# print(f'My first name is {first} and last name is {last}')
# #Answer2
# animal_name = input('insert animal name: ')
# if len(animal_name) < 4:
#     print('The name is short')
# else:
#     print('Animal char name is longer than 4')
# #Answer3
# msg = 'Yankee, go home'
# replace_msg = msg.replace(',','!')
# print(replace_msg)
# print(f'The number of letter e return in the sentence is:', replace_msg.count('e'))
# #Answer4
# for odd_num in range(1,10,2):
#     print(odd_num)
# #Answer5
# pep= input("enter a list of people you know (separated by spaces):")
# pep_list=pep.split(" ")
# for pip in pep_list :
#     if pip =="sara":break
#     print(pip)
#Answer5 with while
# while True:
#     name=input('enter name:')
#     if name.lower()=='sara':
#         break
#     print(name)
# #Answer6
# sum = 0
# number_list = [89, 54, 78, 65, 21, 45, 86]
# for num in number_list:
#     if num > 59:
#         sum = sum+num / len(number_list)
# print(sum)
# # #Answer7
# a = int(input('insert a number: '))
# b = int(input('insert b number: '))
# x = 'a + b'
# t = x.split(" ")
# if len(t) > 1:
#     print(a+b)
# else:
#     print('wrong outcome')
# #Answer8
# a = int(input('insert a number: '))
# b = int(input('insert b number: '))
# x = 'a / b'
# t = x.split(" ")
# if len(t) > 1 and x[4] != 0:
#     print(format(a / b, ".2f"))
# else:
#     print('wrong outcome')
# #Answer9
# sum = 0
# while True:
#     num_str=input('insert a Number: ')
#     if num_str != 'end'  and num_str.isdigit(): ### wanted to catch also all not int not just end
#         num1=int(num_str)
#         sum = sum + num1
#     else:
#         break
# print(sum)

# #Answer10
# clock = int(input('please enter a hour in the day: '))
# if clock <5:
#     print('night')
# if clock >= 5:
#     if clock <=11:
#         print('MORNING')
# if clock >= 12:
#     if clock <= 17:
#         print('Day')
# if clock >= 18:
#     if clock <= 22:
#         print('EVENING')
#     else:
#         print('night')
### #Answer11
# MyName = 'Sagi Schwartz'
# print(MyName)
# print(MyName[-6:-1])
# print(MyName[2])
# x=len(MyName)
# third=int(x*0.33)
# print(MyName[:third])
# print(MyName.count('a'))
# ','.join(MyName)
# if 'b' in MyName:
#     print(True)
# else:
#     print(False)
# print([MyName])
# new_name = MyName.split()
# print(new_name[::-1])
# last_name_upper = new_name[1]
# print(last_name_upper.upper())
# first_name = new_name[0]
# first_name.replace('Sagi','Si')
# print(first_name.replace('Sagi','Si') + ' ' +last_name_upper.upper())
# #Answer12
# lst1 = [8, 1000, -3, 2, 5]
# print(lst1)
# print(max(lst1))
# print(min(lst1))
# x = len(lst1)
# sum=0
# for num in lst1:
#     sum=sum+num
# print(sum/x)
# remove2 = lst1.pop(round(len(lst1)/2))
# print(lst1)
# print(sorted(lst1))
# print(lst1[1::])
# z = (sum/x)
# for t in lst1:
#     if t < int(z):
#         print(t, end=",")



















