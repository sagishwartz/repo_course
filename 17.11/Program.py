# test a membership
name=input('What is your name?: ')
print('t' in name or 'T' in name)

# if..else block
food=input('What is in bag:')
if food=='ice cream':
    print('i like strawberry flavor')
else:
    print('No ice cream?')
print('Lets eat')

# if..elif..else block
color=input('what is your car color:?')
if color=='black':
    print('chic')
elif color=='yellow':
    print('sunshine')
    print('not interested')
else:
    print('it is normal')

# testing a number
age=int(input('Enter your age?: '))
if age>=18:
    print("allowed to enter")
else:
    print("grow up and come later")

# nested 'if' block
time=int(input('Time to get to work: '))
if time>=10:
    if time <= 20:
        print('{} reasonable'.format(time))
    else:
        print('{} too long'.format(time))
else:
    print('{} lucky you'.format(time))
print('trip time to workplace')
print('end of analysis')

# debugging a program (use breakpoints)
num_list=[89,-3,10,247,45]
num_list.remove(max(num_list))
num_list.sort(reverse=True)
num_list.pop(1)
num_list.clear()
num_list.append('grass')