# Laboratory Activity # 7
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2


def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)


arr = [78, 62, 56, 27, 90, 65, 71, 87, 33, 86]
print("My array:", arr)
print("The output of the sorted array using selection sort algorithm:", arr)
print("\n")
print("The process of selection sort:")
selection_sort(arr)
print("\n")


