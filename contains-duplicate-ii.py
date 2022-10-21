class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}
        for i in range(len(nums)):
            if nums[i] in ht:
                for j in ht[nums[i]]:
                    if (i - j <= k):
                        return True
                ht[nums[i]].append(i)
            else:
                ht[nums[i]] = [i]
        return False

        # naive approach
        '''for i in range(len(nums)):
            for j in range(max(0, i-k), i):
                if (nums[i] == nums[j]):
                    return True
        return False'''