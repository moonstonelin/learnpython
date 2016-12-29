class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            r = self.myPow(x, n/2)
            if n%2 == 1:
                return x*r*r
            else:
                return r*r