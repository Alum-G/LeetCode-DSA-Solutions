from typing import List

#Creating a class of 
class Solution:
    def sum_of_two(self, nums: List[int], target: int) -> List[int]:
        #create a an empty dictionary of indexes
        num_list = {}

        #iterate over the indexes and values
        for i, num in enumerate(nums):
            #calculate for complement 
            complement = target - num
            
            #if complement in num_list, return the complement and index
            if complement in num_list:
                return [num_list[complement], i]
            #If not create a new value and store it's index
            num_list[num] = i
        #If solution not found return an empty list
        return []

# Create an instance of the Solution class and call the sum_of_two method
answer = Solution()

# Example usage
nums = [3, 4, 5, 6, 7, 8, 9]
target = 10  
result = answer.sum_of_two(nums, target)
print(result)
