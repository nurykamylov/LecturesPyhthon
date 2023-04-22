                                            # Функция
"""
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)

n = int(input('n = ')) # 5
sumNumbers(n) # 15

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

n = int(input("n = ")) # 5
print(sumNumbers(n)) # 15

def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5)) 

def new_string(symbol, count=3):
 return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

def concatenatio(*params):
    res = ""
    for item in params:
     res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))# asdw
print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

                                    # Рекурсия 
def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
                                    # Сортировки

# def quicksort(array):    
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))


def MergeSort(num):
    if len(num) > 1:
        mid = len(num)//2
        left = num[:mid]
        right = num[mid:]
        MergeSort(left)
        MergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num[k] = left[i]
                i+=1
            else:
                num[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            num[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            num[k] = right[j]
            j+=1
            k+=1
list = [45,13,532,53,75,3,234,64,75,34,2,9]
print(MergeSort(list))
