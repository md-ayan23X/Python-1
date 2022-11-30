#EXAMPLES ON r+, w+, a+
 
Ayan=open("Details.txt","r")
print(Ayan.read())
Ayan=close()

Ayan=open("Details.txt","w")
Ayan.write("Hello,My name is Ayan")

Ayan=open("Details.txt"."a")
Ayan.write("\nHello, My full name is Md.Ayan Shaikh")

Ayan=open("Details.txt","r")
print(Ayan.read())


#SIMPLE CALCULATOR

def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  return x/y
num1=float(input("Enter the First value: "))
choice = input("Enter choice(+ , - , * , /): ")
if choice in ("+","-","*","/"):
  num2=float(input("Enter the Second value: "))
  if choice == "+":
            print(num1, "+", num2, "=", add(num1, num2))
  elif choice == "-":
            print(num1, "-", num2, "=", (num1-num2))

  elif choice == "*":
            print(num1, "*", num2, "=", (num1*num2))

  elif choice == "/":
            print(num1, "/", num2, "=", (num1/num2))
else:
   print("Invalid Input")
        