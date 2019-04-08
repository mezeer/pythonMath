import math

userInput = input("Enter what your are solving for (leg or hypotenuse): ")

if userInput.lower() == "leg":
  a, b = [int(x) for x in input("Enter the two values here (seperated by white space): ").split()]
  print(math.sqrt((b**2)-(a**2)))

elif userInput.lower() == "hypotenuse" or userInput.lower() == "hypot"  :
  a, b = [int(x) for x in input("Enter the two values here (seperated by white space): ").split()]
  print(math.sqrt((a**2)+(b**2)))

else:
  print("Please enter a valid type (leg or hypotenuse)")
