# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    #普通遍历
    def twoSum(self, num, target):
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == target:
                    tmp = []
                    tmp.append(num[i])
                    tmp.append(num[j])
                    return tmp
    #字典哈希
    def twoSum2(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if (target-nums[i]) in dic:
                return [dic[target-nums[i]], i]
            else:
                dic[nums[i]] = i


nums = [2, 7, 11, 15, 1,8] 
target = 9
solution = Solution()
result = solution.twoSum2(nums, target)
print(result)

