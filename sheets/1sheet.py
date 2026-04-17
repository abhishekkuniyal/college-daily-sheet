"""q1 Richest customer wealth lc1672"""

"""def count(accounts):
   wealth = []
   
   for i in accounts:
         total = 0
         for j in i:
               total += j
         wealth.append(total)
   max_balance = wealth[0]
   for k in wealth:
        if k> max_balance:
             max_balance = k
   return max_balance

print(count([[1,2,3],[3,2,1]]))
        """

""" q2 1480. Running Sum of 1d Array"""

"""def onedsum(nums):
   start = 0
   result = []
   for i in nums:
      start  = start + i
      result.append(start)

   return result

print(onedsum([1,2,3,4]))"""

""" q3 1816. Truncate Sentence"""

"""def trunc(sentence,k):
   
   words = sentence.split()
   words.pop(k)
   

print(trunc("Hello how are you Contestant", 4))"""
   


"""q4 1833. Maximum Ice Cream Bars """

"""def icecream(arr,coins):
   maxele = max(arr)
   count = [0]*(maxele+1) #created new array with length of maximum element + 1
   for num in arr:
      count[num] +=1

   result = []
   for i,c in enumerate(count):
      result.extend([i]*c) #counting sort use kiya hai
      #enumernate list ke items ko key value mai tod deta hai
      #agar multiple elements kissi array mai add karna hai to uske liye .extend use hota hai
   
   count  = 0
   for cost in result:
      if coins>= cost:
         coins -= 1
         count += 1
      else:
         break
   return count

   
   

print(icecream([7,3,3,6,6,6,10,5,9,2],56))"""
   
"""find the winner"""

"""def findthewinner(s:int,k:int):
   winner = 0
   for i in range(2,s+1):
      winner = (winner+k)%i
   return winner+1

print(findthewinner(5,2))"""



"""pascale triangle"""


def pastriangle(rows):
   for i in range(rows):
      print("")
      for j in range(i+1):
          print(j,end=" ")
   print(" ")

(pastriangle(5))