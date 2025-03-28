def countTargetPairs(nums, target):
    nums.sort()
    count = 0
    lengte = len(nums)
    
    for i in range(lengte - 1):
        for j in range(i + 1, lengte):
            if nums[i] + nums[j] < target:
                count += 1
            else:
                count = count

    
    return count

print(countTargetPairs([-1, 1, 2, 3, 1], 2))
print(countTargetPairs([-6, 2, 5, -2, -7, -1, 3], -2))
