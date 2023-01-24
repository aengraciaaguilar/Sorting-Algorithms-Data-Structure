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

        if i < j:
            arrays[i], arrays[j] = arrays[j], arrays[i]
            print("\t\t\t ", arrays)

    if arrays[i] > the_pivot:
        arrays[i], arrays[right] = arrays[right], arrays[i]
        print("\t\t\t ", arrays)
    return i


arrays = [78, 62, 56, 27, 90, 65, 71, 87, 33, 86]
print("My array:", arrays)
print("he output of the sorted array using quick sort algorithm::", (arrays))
print("\n")
print("The process of quick sort:")
quick_sort(arrays, 0, len(arrays) - 1)

