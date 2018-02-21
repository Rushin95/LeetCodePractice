class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        start = 0
        end = num/2
        ans = False

        if num == (num/2)**2 or num == num**2:
            return True

        while end - start != 1:
            mid = (start+end)/2
            if mid**2 < num:
                start = mid
            elif mid**2 > num:
                end = mid
            elif mid**2 == num:
                ans = True
                break

        return ans



            
