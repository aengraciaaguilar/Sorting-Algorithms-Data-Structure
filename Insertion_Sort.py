# Laboratory Activity # 7
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = anchor
        print(arr)

arr = [78, 62, 56, 27, 90, 65, 71, 87, 33, 86]
print("My array:", arr)
print("The output of the sorted array using insertion sort algorithm:", arr)
print("\n")
print("The process of insertion sort:")
insertion_sort(arr)
print("\n")
