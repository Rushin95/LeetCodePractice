class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        power = 0
        if x < 0:
            power = 1
            x = abs(x)
        ans = 0

        while x > 0:
            r = x % 10
            ans = ans*10 + r
            x = x// 10
        if (ans <= 2147483647):
            return ans * ((-1)**(power))
        else:
            return 0
