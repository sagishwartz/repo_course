# Solution 1
list1=[10,20,30,40,50,60,70,80,90]
list2=list1[::-3]
print(list2)

#-----------------------------------

# Solution 2
hours24=[13,14,15,16,17,18,19,20,21,22,23,24]
hours12=[hour-12 for hour in hours24]
print(hours12)
mainhours=[hour-12 for hour in hours24 if hour%3==0]
print(mainhours)

#-----------------------------------

# Solution 3
worker={'name':'gil','salary':5000,'married':False,'car':'ford'}
print(worker.values())
worker['married']=True
worker.pop('car')
worker['spouse']='talia'
print(worker)