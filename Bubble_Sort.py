# Laboratory Activity # 7
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                print(arr)

arr = [78, 62, 56, 27, 90, 65, 71, 87, 33, 86]
print("My array:", arr)
print("The output of the sorted array using bubble sort algorithm:", arr)
print("\n")
print("The process of bubble sort:")
bubble_sort(arr)
print("\n")

