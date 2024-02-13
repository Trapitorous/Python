number1=int(input("1st Number: "))
number2=int(input("2nd Number: "))
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(number1%number2)

# comparison operator
number3=int(input("3rd Number: "))
number4=int(input("4th Number: "))
print(f"{number3} is equal to {number4} {number4==number3}" )
print(f"{number3} is not equal to {number4} {number4!=number3}" )
print(f"{number3} is less than {number4} {number4>number3}" )
print(f"{number3} is grater than {number4} {number4<number3}" )
print(f"{number3} is grater than or equal to{number4} {number4<=number3}" )

# logical operator
number5=int(input("5th number: "))
number6=int(input("6th number: "))
print(f"{number5} and {number6} both are true {number5==number6 and number5>number6}")
print(f"{number5} and {number6} one is true {number5==number6 or number5>number6}")
