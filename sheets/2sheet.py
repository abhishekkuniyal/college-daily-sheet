"""3 sum"""
#brute force approach
"""def threesum(nums):
   new = []
   target = 0
   n = len(nums)
   for i in range(n):
      for j in range(i+1,n):
         for k in range(j+1,n):
            if nums[i]+nums[j]+nums[k] == target:
               new.append((nums[i],nums[j],nums[k]))
   return new
print(threesum([-1,0,1,2,-1,-4]))"""


def threesum(nums):
   new = set()
   target = 0
   n = len(nums)
   for i in range(n):
      seen = set()
      current = target- nums[i]
      for j in range(i+1,n):
         complement = current - nums[j]
         if complement in seen:
            new.add(tuple(sorted((nums[i],nums[j],complement))))

         seen.add(nums[j])
   return list(new)
print(threesum([-1,0,1,2,-1,-4]))