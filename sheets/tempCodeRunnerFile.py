def happynumber(n):
   seen = set()
   while n!=1:
      if n in seen:
         return False
      seen.add(n)
      n = sum(int(digit)**2 for digit in str(n))
         
   return n
print(happynumber(100)
)