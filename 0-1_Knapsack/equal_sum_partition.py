from subset_sum import subset_sum

def equal_sum_part(arr, n):
    arr_sum = sum(arr)

    if arr_sum % 2 != 0:
        return False
    else:
        return subset_sum(arr, arr_sum // 2, n)

arr = [1, 5, 11, 5, 1]
n = len(arr)

print(equal_sum_part(arr, n))