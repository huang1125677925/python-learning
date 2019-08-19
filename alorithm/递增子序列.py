def findSubsequences( nums) :
    res = [[nums[0]]]
    idx_map = {nums[0]: -1}
    for i in range(1, len(nums)):
        if nums[i] not in idx_map:
            idx_map[nums[i]] = len(res)
            res += [lst + [nums[i]] for lst in res if lst[-1] <= nums[i]] + [[nums[i]]]
        else:
            tmp = len(res)
            res += [res[j] + [nums[i]] for j in range(idx_map[nums[i]],tmp) if res[j][-1] <= nums[i]]
            idx_map[nums[i]] = tmp
        print(res)
        print(idx_map)
    print(res)
    print(idx_map)
    return [lst for lst in res if len(lst) > 1]

r=[4, 6, 7, 7]

print(findSubsequences(r))