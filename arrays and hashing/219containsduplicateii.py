class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = {}
        for i, num in enumerate(nums):
            if num in result and i-result[num]<=k:
                return True
            else:
                result[num]=i

        return False