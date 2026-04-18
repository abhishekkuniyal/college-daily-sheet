"""matrix transformation"""
"""
#how to create the matrix in python
def twod(r, c, arr: list):
    for i in range(r):
        row = []
        for j in range(c):
            val = int(input(f"Enter value for ({i},{j}): "))
            row.append(val)
        arr.append(row)
    return arr

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print(twod(rows, cols, []))"""


"""def revresenumber(n):
    rev = 0
    original = n
    while n>0:
        last = n%10
        rev = rev*10+last
        n = n//10
    return (abs(original - rev))
n = int(input("enter the number you have to find the reversed:"))
print(revresenumber(n))
"""

def happynumber(n):
   seen = set()
   while n!=1:
      if n in seen:
         return False
      seen.add(n)
      n = sum(int(digit)**2 for digit in str(n))
         
   return True
print(happynumber(100)
)