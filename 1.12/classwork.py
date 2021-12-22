# Solution 1
import random
city=input('Provide US city: ')
print(random.choice(city))

#-----------------------------------

# Solution 2
def timeTo12h(time):
    if time>12:
        time=time-12
    if time==0:
        time=12
    print(time)

timeTo12h(3)
timeTo12h(17)
timeTo12h(20)

#-----------------------------------

# Solution 3
def power2(num):
    res=num**2
    return res

print(power2(5))
print(power2(10))