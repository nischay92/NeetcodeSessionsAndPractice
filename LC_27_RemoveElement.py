# Remove Element (LC:27)
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l+=1
        return l                 

