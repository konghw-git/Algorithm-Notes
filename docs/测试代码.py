from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        print(pre)

        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        print(suf)
        return [p * s for p, s in zip(pre, suf)]

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
