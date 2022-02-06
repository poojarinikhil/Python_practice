print("Enter number one")
num1 = int(input())
print("Enter number two")
num2 = int(input())
print("Enter the operator")
expression= input()
if num1== 45 and num2== 3 and expression=="*" :
    print(555);
elif num1==56 and num2==9 and expression=="+":
    print(77)
elif num1==56 and num2==6 and expression=="/":
    print(4)
elif expression == "+":
    print(num1+num2)
elif expression == "-":
    print(num1-num2)
elif expression == "*":
    print(num1 * num2)
elif expression == "/":
    print(num1/num2)