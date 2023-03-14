class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        return self.perms(nums, 0)
        # return res
        
    # def dfs(self, nums, path, res):
    #     if not nums:
    #         res.append(path)
    #         return
    #     for i in range(len(nums)):
    #         self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
    def perms(self, nums, start):
        out = []
        if start == len(nums):
            return [[]]
        
        current = nums[start]
        temp = self.perms(nums, start+1)
        for i in temp:
            for j in range(len(i)+1):
                k = i[:]
                k.insert(j, current)
                out.append(k)
        
        return out

s = Solution()
print(s.permute([1, 2]))