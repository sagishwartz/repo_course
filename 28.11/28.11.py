##Answer 1
#a# while-loop is another type of loop which can be used for tasks where the number of iterations is not known.
#b# Yes
##Answer 2
# While loop checks the condition first and then executes the statement
# whereas do while loop will execute the statement at least once, then the condition is checked
##Answer 3
# n = int(input('insert a number: '))
# fact = 1
# for i in range(1, n + 1):
#     if fact == 0:
#         print(1)
#     else:
#         fact = fact * i
# print(f'The factorial is: {fact}')
##Answer 4
# lst1 = [76, 17, 89, 68, 25, 94]
# for num_lst1 in lst1:
#     if num_lst1 > 85:
#         print(f'Very Good {num_lst1}') ### added format for my check
#     if num_lst1 <59:
#         print(f'failed {num_lst1}') ### added format for my check
#     if 59 <= num_lst1 <= 85: ### tried with else, didn't find the right solution
#         print(num_lst1)
##Answer 5 - ##############not sure this is the right solution although the outcome is right
# n = 0
# while True:
#     wheels = int(input('how many wheels do you need: '))
#     if wheels >=0:
#         if wheels <= 4:
#             n = n+wheels
#     if wheels > 4:
#         n == 0
#     if wheels < 0:
#         break
# print(n)
# ##Answer 6
# playr1_win = 0
# playr2_win = 0
# while True:
#     player1 = int(input('player1 won the set (insert 1 or 0): '))
#     player2 = int(input('player2 won the set (insert 1 or 0): '))
#     if player1 == 1:
#         playr1_win=playr1_win+player1
#         if playr1_win == 3:
#             print('player1 won')
#             break
#     if player2 == 1:
#         playr2_win=playr2_win+player2
#         if playr2_win == 3:
#             print('player2 won')
#             break
# print(f'{playr1_win}' + ':' + f'{playr2_win}')
# ##Answer 7
# while True:
#     print("Hello User, please put a number")
#     number = int(input())
#     if number % 7 == 0 or '7' in str(number) :
#         print("BOOM")
#     else:
#         print('Looser :)')




















