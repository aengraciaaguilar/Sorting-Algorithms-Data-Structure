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
