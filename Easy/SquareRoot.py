class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0 #creating the range for search...switching to bin cuz on time
        right = x

        while left <= right:
            mid= (left+right)//2
            
            if (mid*mid) > x:
                right = mid -1

            elif (mid*mid) < x:
                left = mid + 1
            else:
                return mid
        return right
