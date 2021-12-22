#formatted string with empty placeholders, values inserted by position
print('today is {} and {}'.format('sunday','21/11'))

#formatted string with named placeholders, values inserted by name
msg='Student {name} got {grade} mark on subject {subject}'
print(msg.format(subject='chemistry',name='Ilya',grade=95))

#combination of positional and named placeholders
msg1='number {} divided by {number2} results in {number3:.6f}'
print(msg1.format(2,number2=3,number3=2/3))

#formatted result using suffix - comma separated thousands
msg2='Here in {country} live {population:,} people'
my_country=input('What is your country?: ')
my_population=9000000
formatted_msg=msg2.format(country=my_country,population=my_population)
print(formatted_msg)
print(msg2)

#formatted string with numbered placeholders, values inserted by order number
print('a city is called a {2} made of {0} and {1}'.format('concrete','glass','jungle'))

#f-string, placeholders accept any expression
num_a=5
num_b=10
print(f'{num_a} plus {num_b} equals {num_a+num_b}')

#string is built from list
lst1=['hello','from','python']
print(lst1)
print(" ".join(lst1))

#print members of list without loops
print(lst1[0])
print(lst1[1])
print(lst1[2])

#print members of list in 'for' loop
lst1=['hello','from','python']
for x in lst1:
    print(x)
print('hi')

#iterate over string
for char in 'london':
    print(char)

#iterate over list of strings
names = ['dani','ran','suzi','moshe']
for name in names:
    print(name.upper())

#use range() to repeat operation 5 times
for num in range(5):
    print('apple')

#build sequence starting at 2
for num in range(2,5):
    print(num)

#build sequence with step of 3
for num in range(1,20,3):
    print(num)

#build decreasing sequence
for num in range(10,1,-2):
     print(num)

#iterate over list of lists using nested 'for' loop
lst1=[['a','r','h'],[1,4,7,5],[True,False]]
for lst2 in lst1:
     print(f'the list of {lst2} consists of:')
     for member in lst2:
          print(member)

#exit loop using break
lst2=[5,9,-48,6,100]
for num in lst2:
    print(f'now checking {num}')
    if num==9:
        print('number was found')
        break
print('exited')

#skip to next iteration using continue
lst3=[500,900,0,600,1000]
for salary in lst3:
    if salary==0:
        continue
    print(f'the worker gets {salary}')