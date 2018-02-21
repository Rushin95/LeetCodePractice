class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        while numbers[i]+numbers[j] != target and i >= 0 and j <= len(numbers)-1:
            if numbers[i]+numbers[j] > target:
                i-=1
            elif numbers[i]+numbers[j] < target:
                i+=1
                j+=1

        return [i+1,j+1]
