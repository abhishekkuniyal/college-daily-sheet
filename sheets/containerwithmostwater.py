"""def container(arr):
   w= h = maxarea = 0
   for i in range(len(arr)):
      for j in range(i+1,len(arr)):
         w  = j-i
         h = min(arr[i],arr[j])
         result = w*h
         maxarea=  max(result,maxarea)
   return maxarea
         
print(container([1,8,6,2,5,4,8,3,7]))""" #brute force

#optimial approach:
"""def maxArea(self, arr: List[int]) -> int:
              maxarea =0
              lp =0 
              rp = len(arr)-1
              while lp<rp:
                w = rp-lp
                h = min(arr[lp],arr[rp])
                result = w*h
                maxarea = max(maxarea,result)

                if arr[lp]<arr[rp]:
                    lp+=1
                else:
                    rp-=1
              return maxarea"""