print("Hii !! This a Mini Calculator made by me.")
print("Enter 'HELP' for the instructions.\nEnter 'QUIT' to exit.")
variable = input("> ").upper()
if variable == 'HELP':
    print("""
    Here is the instruction how it works:
    
        You are supposed to enter the operator which the calculator will understand and proceed accordingly.
        
        The operators are:-
                            '+' -> If you wants to add two numbers
                            '-' -> If you wants to subtract two numbers
                            '*' -> If you wants to multiply two numbers 
                            '/' -> If you wants to divide two numbers 
                            '**' -> If you wants to find the raise to power
                            '%' -> If you wants to find the remainder after dividing two numbers
                            '//' -> If you wants to find the quotient after dividing two numbers
                            '!' -> If you wants to find the factorial of a number
                            
                            NOTE => If you don't enter any number the calculator will consider it as 0.
                            
                    HOPE THIS CALCULATOR WILL HELP YOU TO FIND THE SOLUTION OF YOUR QUESTIONS!!
                    
                                        Press 'ENTER' to start.....
    """)
    variable = input("> ").upper()
    if variable == '':
        operator = ''
        store = ['+', '-', '*', '/', '**', '%', '//', '!']
        repeat = True
        while True:
            while operator == '':
                operator = input("Enter the operator= ")
                if operator == '':
                    print("Please enter any operator.")
                for items in store:
                    if items == operator:
                        num1 = ''
                        num2 = ''
                        if operator == '!':
                            num1 = input("Enter the number= ")
                            if num1 == '':
                                num1 = '0'
                        else:
                            num1 = input("Enter the number= ")
                            num2 = input("Enter the second number= ")
                            if num1 == '':
                                num1 = '0'
                            if num2 == '':
                                num2 = '0'


                        def addition(n1, n2):
                            add = n1 + n2
                            print(f"Addition of {n1} and {n2} is {add}.")


                        def subtraction(n1, n2):
                            sub = n1 - n2
                            print(f"Subtraction of {n1} and {n2} is {sub}.")


                        def multiplication(n1, n2):
                            mul = n1 * n2
                            print(f"Multiplication of {n1} and {n2} is {mul}.")


                        def division(n1, n2):
                            div = n1 / n2
                            print(f"Division of {n1} by {n2} is {div}.")


                        def raise_to(n1, n2):
                            power = n1 ** n2
                            print(f"Power of {n1} with raise to {n2} is {power}.")


                        def remainder(n1, n2):
                            number = n1 % n2
                            print(f"Remainder of {n1} divided by {n2} is {number}.")


                        def quotient(n1, n2):
                            number = n1 // n2
                            print(f"Quotient of {n1} divided by {n2} is {number}.")


                        def factorial(n1):
                            i = 1
                            factor = 1
                            while i <= n1:
                                factor = factor * i
                                i += 1
                            print(f"Factorial of {n1} is {factor}.")


                        if operator == '+':
                            addition(int(num1), int(num2))
                        elif operator == '-':
                            subtraction(int(num1), int(num2))
                        elif operator == '*':
                            multiplication(int(num1), int(num2))
                        elif operator == '/':
                            if num2 == '0':
                                print(f"Cannot divide {num1} with {num2}.")
                            else:
                                division(int(num1), int(num2))
                        elif operator == '**':
                            raise_to(int(num1), int(num2))
                        elif operator == '%':
                            if num2 == '0':
                                print(f"Cannot divide {num1} with {num2} therefore remainder can't be obtained.")
                            else:
                                remainder(int(num1), int(num2))
                        elif operator == '//':
                            if num2 == '0':
                                print(f"Cannot divide {num1} with {num2} therefore quotient can't be obtained.")
                            else:
                                quotient(int(num1), int(num2))
                        elif operator == '!':
                            factorial(int(num1))
            repeat = input("Do you want to do more calculations(Yes/No)= ").upper()
            if repeat == 'YES':
                repeat = True
                operator = ''
            elif repeat == 'NO':
                repeat = False
                break
elif variable == 'QUIT':
    print("Thank You😄😄!!")
    exit()
print("Thank You😄😄!!")