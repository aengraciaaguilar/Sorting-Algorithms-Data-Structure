# Laboratory Activity # 7
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2


def quick_sort(arrays, left, right):
    if left < right:
        partition_positions = partition(arrays, left, right)
        quick_sort(arrays, left, partition_positions - 1)
        quick_sort(arrays, partition_positions + 1, right)

def partition(arrays, left, right):
    i = left
    j = right - 1
    the_pivot = arrays[right]
    while i < j:
        while i < right and arrays[i] < the_pivot:
            i += 1
        while j > left and arrays[j] >= the_pivot:
            j -= 1

