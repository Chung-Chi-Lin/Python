from typing import List
# 回傳索引值，為 nums 相加符合 target 數。
# 不能使用同一索引
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for index2 in range(index+1, len(nums)):
                if nums[index] + nums[index2] == target:
                    return [index, index2]

result = Solution()

# Output: [0,1]
print("1", result.two_sum([2, 7, 11, 15], 9))

# Output: [1,2]
print("2", result.two_sum([3, 2, 4], 6))

# Output: [0,1]
print("3", result.two_sum([3, 3], 6))

print("-----------------------------------------------------")
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution2:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[num] = index
        return []



result2 = Solution2()

# Output: [0,1]
print("1", result2.two_sum([2, 7, 11, 15], 9))

# Output: [1,2]
print("2", result2.two_sum([3, 2, 4], 6))

# Output: [0,1]
print("3", result2.two_sum([3, 3], 6))