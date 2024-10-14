
class Solution:

    def missing_number(arr, n):
        
        total_sum = int(n* (n+1)// 2)
        array_sum = sum((arr))

        missing_number = total_sum - array_sum
        return missing_number
    