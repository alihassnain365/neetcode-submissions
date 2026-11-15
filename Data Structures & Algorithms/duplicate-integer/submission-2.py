class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if (len(nums) == 0 or len(nums) == 1):
            return False
        if (len(unique) != len(nums)):
            return True
        else:
            return False
        