def find_max(nums):
    result=nums[0]
    for x in nums:
        if x > result:
            result = x
            return result
        find_max([1,8,2])
