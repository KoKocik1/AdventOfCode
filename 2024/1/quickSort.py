def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = [x for x in list[1:] if x < pivot]
    right = [x for x in list[1:] if x >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)
