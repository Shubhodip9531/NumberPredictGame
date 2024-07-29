import random
random = random.randint(1,100)
user=int(input("Enter a number : "))
print(user)
i=5
point=0
while(i!=0):
  if(random!=user):
    if(random>user):
      print("Retry and enter a greater value : ")
      i=i-1
      user=int(input("Enter a number : "))
    else: 
      print("Retry and enter a lower value : ")
      i=i-1
      user=int(input("Enter a number : "))
  else:
    print("Congratulation")
    Point=point+i
    print(Point)
    break
else:
    print("Sorry you use your all try.")
