def sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if middle + 1 == len(array):
        return False

    if (array[middle] < element) & (array[middle + 1] >= element):
        return middle
    elif array[middle] >= element:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


l = list(map(lambda s: int(s), input("Последовательность чисел:").split(' ')))
n = int(input("Введите число:"))
sort(l)

result = binary_search(l, n, 0, len(l) - 1)
if result is False:
    print("Не найдено")
else:
    print("Позиция = ", result)





