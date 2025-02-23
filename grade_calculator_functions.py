grade = int(input("Enter your score: "))

if grade == 100 or grade >= 95:
  print("Your Grade is: A" )
elif grade >= 90:
  print("Your Grade is: B" )
elif grade >= 85:
  print("Your Grade is: C" )
elif grade >= 75:
  print("Your Grade is: D" )
else:
    print("Your Grade is: F" )