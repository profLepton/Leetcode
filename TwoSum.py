def twoSum(nums, target):
    d = {} 
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            return [i, d[target - nums[i]]]
        d[nums[i]] = i


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    result = twoSum(nums, target)
    print(result)