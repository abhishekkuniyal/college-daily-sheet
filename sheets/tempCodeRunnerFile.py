def findthewinner(s:int,k:int):
   winner = 0
   for i in range(2,s+1):
      winner = (winner+k)%i
   return winner+1

print(findthewinner(5,2))