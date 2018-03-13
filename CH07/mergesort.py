data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def mergeSort(list):
    # determine whether the list is broken into individual pieces
    if len(list) < 2:
        return list

    #find the middle of the list
    middle = len(list)//2

    # Break the list into two pieces
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    # merge the two sorted lists into a larger piece
    print("Left side: ", left)
    print("Right side: ", right)
    merged = merge(left, right)
    print("Merged ", merged)
    return merged

def merge(left, right):
    # when the left side or right side is empty, 
    # it means that this is an individual item and is already sorted
    if not len(left):
        return left

    if not len(right):
        return right

    # define variables used to merge the two pieces
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # keep working until all the items are merged
    while(len(result) < totalLen):
        # perform the required comparison and merge the two pieces according to value
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        # when the left side or right side is longer, add the remaining elements to the result
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break

    return result

mergeSort(data)
