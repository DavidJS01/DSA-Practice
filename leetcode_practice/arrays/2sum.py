class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]: #type: ignore
    map = {}
    for i, n in enumerate(nums): # for index, value in nums
        diff = target - n # the value we are looking for is target - n
        if diff in map: # if the value we need is in the hashmap
            print([map[diff], i]) # return the index of the value, and the other value
        map[n] = i # if value not in hashmap, add value: index pair
            
# enumerate: returns a counter for each iteration value in nums
# ex: (index:0, value:'value')


