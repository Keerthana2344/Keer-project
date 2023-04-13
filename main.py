print("Hello vidya")
name=input("Enter your name: ")
time=float(input("Enter the current time: "))

if(time<=12):
  print("Good morning ",name)
elif(time<=16):
  print("Good afternoon ",name)
elif(time<=20):
  print("Good evening ",name)
else:
  print("Good night")