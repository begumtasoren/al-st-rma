#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        
        left = 0
        current_sum = 0 
        
        for right in range(len(arr)):
            current_sum += arr[right]
            
            while current_sum > s and left <= right:
                current_sum -= arr[left]
                
                left += 1
                
            if current_sum == s:
                return [left + 1, right + 1]
                
        return -1
    
#Input: arr[] = [1,2,3,7,5], n = 5, s = 12
#Output: 2 4
#Explanation: The sum of elements from 2nd to 4th position is 12.