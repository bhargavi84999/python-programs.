n = int(input("Enter number: "))

if n % 2 == 0:
    print(n % 3)
else:
    print(n % 2)

a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
operator=input("enter a operator:")
match operator:
    case "+":
        print("result=",a+b)
    case "-":
        print("result=",a-b)
    case "*":
        print("result=",a*b)
    case "/":
      if b != 0:
         print("Result =", a / b)
      else:
          print("Division by zero is not possible")
    case _:
        print("Invalid Operator")
