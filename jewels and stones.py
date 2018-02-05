class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Method - 1 .. Faster

        count = 0
        for stone in S:
            if stone in J:
                count += 1
        return count

        # Method - 2 .. Slower

#         count_dict = dict()
#         final_count = 0
#         for stone in S:
#             count_dict[stone] = count_dict.get(stone,0) + 1

#         for jewel in J:
#             final_count += count_dict.get(jewel,0)

#         return final_count
