class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for i in nums:
            if i not in mapp:
                mapp[i] = 1
            else:
                return True

        return False