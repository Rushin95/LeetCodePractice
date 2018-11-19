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
            temp = nums[i] # save the value at the current index

            while 1:
                new_position = (j-k)%n # 

                if new_position == i: # new position is same as old one
                    break
                else:
                    nums[j] = nums[new_position]
                    j = new_position
            nums[j] = temp
        '''
        Best Solutions:
        public class Solution {

            public void rotate(int[] nums, int k) {
                k %= nums.length;
                reverse(nums, 0, nums.length - 1); # reverse whole array
                reverse(nums, 0, k - 1); # reverse first k
                reverse(nums, k, nums.length - 1); # reverse the rest
            }

            public void reverse(int[] nums, int start, int end) {
                while (start < end) {
                    int temp = nums[start];
                    nums[start] = nums[end];
                    nums[end] = temp;
                    start++;
                    end--;
                }
            }
        }
        '''
