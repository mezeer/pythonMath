import math
a = float(input("Enter the A value: "))
b = float(input("Enter the B value: "))
c = float(input("Enter the C value: "))

if b**2-4*a*c < 0: 
  print("This equation has no solution")
  
elif b**2-4*a*c == 0: 
  print("This equation has one solution: ", (-b+math.sqrt(b**2-4*a*c))/2*a)
else:
  print("\nSolutions:", (((b * -1) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)), ",", (((b * -1) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)))
