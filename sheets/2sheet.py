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


"""def threesum(nums):
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
print(threesum([-1,0,1,2,-1,-4]))"""



"""subarray sums k"""
"""
def subarraysum(nums,m):
   sub = []
   for i in range(len(nums)):
      for j in range(i+1, len(nums)+1):
         sub.append(nums[i:j])
   add = []
   for k in range (len(sub)):
      add.append(sum(sub[k]))
   freq = {}
   for k in add:
      if k in freq:
         freq[k] +=1
      else:
         freq[k] = 1
   for key,value in freq.items():
      if key == m:
         return value
print(subarraysum([1,2,3],3))"""

"""different approach"""

"""prefix sum array"""

"""def prefixsum(arr):
   prefix = [0]*len(arr)
   prefix[0]= arr[0]

   for i in range(len(arr)):
      prefix[i]= prefix[i-1]+ arr[i]
   return prefix



print(prefixsum([1,2,3]))"""


"""mximum subarray product"""
"""def maxproductsum(arr):
  prefix_pro = [0]*len(arr)
  prefix_pro[0]= arr[0]
  for i in range(1,len(arr)):
    prefix_pro[i]= prefix_pro[i-1]*arr[i]

  return max(prefix_pro)

print(maxproductsum([2,3,-2,4]))"""




"""maximums subarray sum"""
"""def subarr(nums):
   sub = []
   for i in range(len(nums)):
      for j in range(i+1,len(nums)+1):
         sub.append(nums[i:j])
   sumar = []
   for k in sub:
      sumar.append(sum(k))
   return max(sumar)
print(subarr([-2,1,-3,4,-1,2,1,-5,4]))"""


def prefixsum(arr):
   prefix = [0]*len(arr)
   prefix[0]= arr[0]

   for i in range(len(arr)):
      prefix[i]= prefix[i-1]+ arr[i]
   return(prefix)



print(prefixsum([-2,1,-3,4,-1,2,1,-5,4]))