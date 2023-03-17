def subsets(nums):
    n = len(nums)
    if n == 0:
        return []
    
    output = []
    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]
        # temp = []
        # for j in range(len(bitmask)):
        #     if bitmask[j] == '1':
        #         temp.append(nums[j])
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        # output.append(temp)
    return output

print(subsets([1, 2, 3]))