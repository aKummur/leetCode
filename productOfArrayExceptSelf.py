nums = [1, 2, 3, 4]


res = []
# left products
p = 1
for i in range(len(nums)):
    res.append(p)
    p = p * nums[i]
# right products
p = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= p
    p = p * nums[i]

print(res)