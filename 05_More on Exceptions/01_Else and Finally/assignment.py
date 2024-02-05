#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number greater then number one"))
except ValueError:
    print('an integer wwas not given')
    
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    answer = (number1/number2)
    print("answer equals" , answer)
 
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print('numbers were divible')


