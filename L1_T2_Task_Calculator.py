import math
def calculator():
    if var == 1:
        return a + b
    elif var == 2:
        return a - b
    elif var == 3:
        return a * b
    elif var == 4:
        return a / b
    elif var == 5:
        return a % b
    


print("""Enter '1' for addition
Enter '2' for substraction
Enter '3' for multiplication
Enter '4' for division
Enter '5' for modulus
""")

a = int(input("Enter the first number : "))  
b = int(input("Enter the second number : "))  
var = int(input("Choose the operation : "))

print(calculator())


#TIME COMPLEXITY OF CODE IS O(1)
#SPACE COMPLEXITY OF CODE IS O(1)