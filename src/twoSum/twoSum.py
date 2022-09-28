from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashMap = {} # Mapping the vlaue to index of that value
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevHashMap:
                return [prevHashMap[diff], i]
            # If solution not found we update the prevHashMap
            prevHashMap[n] = i
        return
    