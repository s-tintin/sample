
# RECURSIVE MANNER

def binarySearchRecursive(arr, start, end, target):
    if start < end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearchRecursive(arr, start, mid - 1, target)
        elif arr[mid] < target:
            return binarySearchRecursive(arr, mid + 1, end, target)

    else:
        return False


# ITERATIVE MANNER

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1

    return -1


if __name__ == '__main__':

    arr = [1, 2, 4, 8, 90, 100]
    target = 1

    result = binarySearchRecursive(arr, 0, len(arr) - 1, target)
    print(result)

    # result = binarySearch(arr, target)
    # print(result)


