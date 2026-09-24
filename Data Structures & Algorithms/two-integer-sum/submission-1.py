class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            
            left += 1

        return []