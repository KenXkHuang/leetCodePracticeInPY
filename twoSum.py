class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in map:
                return [map[target - nums[i]], i]
            else:
                map[nums[i]] = i
        return -1

    print(twoSum(nums=[2, 7, 11, 15],target=9))
