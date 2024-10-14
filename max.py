
def finding_max_number(arr):

    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [1,2,5,8,9]
print(finding_max_number(arr))


    