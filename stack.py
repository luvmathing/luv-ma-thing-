# burger = []
# for b in range(3):
#     burger.append(int(input()))

# drink = []
# for d in range(2): 
#     drink.append(int(input()))

# set = min(burger) + min(drink) - 50  # 세트가격 = 버거가격+음료가격-50
# print(set)

# # burger = [int(input()) for b in range(3)]
# # drink = [int(input()) for d in range(2)]
# # print(min(burger) + min(drink) - 50)

# # list = [1, 2, 3]

# numbers = [int(input()) for i in range(9)]
# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)


import sys
n = int(sys.stdin.readline()) # input으로 그냥 했을 때 시간초과

stack = []

for a in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)  
    elif order[0] == "size":
        print(len(stack))  
    elif order[0] == "empty":
         if stack:
            print(0)
         else: print(1)
    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else: print(-1)