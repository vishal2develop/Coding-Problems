def ceilSearch(arr, low, high, num):
    # if num is less than or equal to low element, return index low
    if num <= arr[low]:
        return low
    # if num is greater than high element, return index -1
    if num > arr[high]:
        return -1
    # find new mid element
    mid = (low + high) // 2
    # if current element is equal to num, return index of current element
    if arr[mid] == num:
        return mid

# if num is greater than current element
    elif arr[mid] < num:
        # if index of next element is less than high and
        # num is less than or equal to the next element
        if mid + 1 <= high and num <= arr[mid + 1]:
            # return index of next element
            return mid + 1
        # reduce the search array
        else:
            return ceilSearch(arr, mid + 1, high, num)
    # if num is smaller than current element
    else:
        # if index of previous element is greater than or equal to low
        # num is greater than previous element
        if mid - 1 >= low and num > arr[mid - 1]:
            # return index of current element
            return mid
        else:

            # reduce the search array
            return ceilSearch(arr, low, mid - 1, num)

arr = list(map(int, "1,4,6,8,9".split(",")))
num = int("3")
index = ceilSearch(arr, 0, len(arr) - 1, num)
if index == 0 or index == -1 or arr[index] == num:
    print(arr[index])
else:
    print(str(arr[index]) + "," + str(arr[index - 1]))
