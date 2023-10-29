# Написать программу на любом языке в любой парадигме для бинарного поиска. 
# На вход подаётся целочисленный массив и число. 
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.


array = [3, 7, 12, 9, 25, 38, 43, 2, 99, 76, 33]
target = int(input("Введите число для поиска: "))

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    mid = 0


    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array.sort()
result = binary_search(array, target)
print(array)

if result > -1:
    print("Индекс искомого элемента: ", result)
else:
    print("Искомый элемент не найден в массиве.")
      