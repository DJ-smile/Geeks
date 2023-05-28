def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Сортировка списка с помощью bubble_sort
unsorted_list = [5, 2, 9, 1, 7]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список (сортировка пузырьком):", sorted_list)

# Поиск элемента с помощью binary_search
target_element = 7
index = binary_search(target_element, sorted_list)
if index != -1:
    print("Элемент", target_element, "найден на позиции", index)
else:
    print("Элемент", target_element, "не найден в списке.")

unsorted_list2 = [12, 8, 4, 6, 10]
sorted_list2 = bubble_sort(unsorted_list2)
print("Отсортированный список (сортировка пузырьком):", sorted_list2)

target_element2 = 12
index2 = binary_search(target_element2, sorted_list2)
if index2 != -1:
    print("Элемент", target_element2, "найден на позиции", index2)
else:
    print("Элемент", target_element2, "не найден в списке.")