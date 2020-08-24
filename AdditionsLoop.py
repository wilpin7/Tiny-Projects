welcome = "Hello"
print ("Please enter your name : ")
name = input()
print(welcome + ' ' + name)

def repeatFunction():
  print("Enter the first number: ")
  number1 = int(input())
  number2 = int(input("Please enter the second number: "))
  print(number1 + number2)

repeatFunction()

while True:
  print("Congratulations" + " " + name + ", will that be all?")
  answer = input()
  if answer == "yes":
    exit()
  if answer == "no":
    repeatFunction()



