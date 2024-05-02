import random
test_list=[]

for i in range(1,10000,1):
    test_list.append(i)

random.shuffle(test_list)

print(test_list)

def binarySearch(n, List):
    List = List.sort()
    last = len(List) - 1
    while True:
        middle = len(List)//2
        if List[middle] == n:
            return(middle)
            break
        elif n < List[middle]:
            List = List[0:middle]

        else:
            List = List[middle: last]




# def findX(n, test_list):
#     a = len(test_list)
#     for i in range(0, a):
#         if test_list[i] == n:
#             print(i)
#             break

# # findX(675, test_list)
# # print(findX(675, test_list))