class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def get_gcd(a,b):
            if b == 0:
                return a
            else:
                return get_gcd(b, a%b)

        n = len(nums)
        for i in range(get_gcd(n,k)):
            j = i
            temp = nums[i]

            while 1:
                d = (j-k)%n
                if d == i:
                    break
                else:
                    nums[j] = nums[d]
                    j = d
            nums[j] = temp
