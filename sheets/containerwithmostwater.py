def container(arr):
   w= h = maxarea = 0
   for i in range(len(arr)):
      for j in range(i+1,len(arr)):
         w  = j-i
         h = min(arr[i],arr[j])
         result = w*h
         maxarea=  max(result,maxarea)
   return maxarea
         
print(container([1,8,6,2,5,4,8,3,7]))