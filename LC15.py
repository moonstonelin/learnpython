class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if not nums:
            return ans

        nums = sorted(nums)
        i = 0

        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == -nums[i]:
                    ans.append([nums[i], nums[left], nums[right]])

                    while left + 1 < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1

                    while right - 1 > left and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1

                elif s < -nums[i]:
                    left += 1
                else:
                    right -= 1

            i += 1

        return ans

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
