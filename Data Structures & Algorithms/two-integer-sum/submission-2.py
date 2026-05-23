class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # iterate through nums and find target-num in it
        # if it's not in the hashmap add the number as key and idx as value
        # otherwise return value idx and num idx
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
        return []
