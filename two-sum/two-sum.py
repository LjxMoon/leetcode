def twoSum(self, nums, target):
    obj = {}
    i = 0
    for num in nums:
        otherNum = target - num
        if num in obj:
            return [obj.get(num), i]
        obj[otherNum] = i
        i = i + 1