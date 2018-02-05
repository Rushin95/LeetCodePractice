class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #Method - 1
        num_1 = "{0:b}".format(x)
        num_2 = "{0:b}".format(y)

        n1 = num_1.zfill(max(len(num_2),len(num_1)))
        n2 = num_2.zfill(max(len(num_2),len(num_1)))

        count = 0
        for value1,value2 in zip(n1,n2):
            if value1 != value2:
                count += 1
        return count

        #Method - 2:
        # return bin(x^y).count('1')
        
