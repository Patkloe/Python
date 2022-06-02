class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
         conv=-1*x
         val=str(conv)
         rev=val[::-1]
         res=int(rev)
         ret=-1*res
         if ret>=pow(-2,31):
          return ret
         else:
          return 0
        else:
         val=str(x)
         ret=val[::-1]
         if int(ret)<=pow(2,31):
          return int(ret)
         else:
          return 0
