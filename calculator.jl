println("Hii !! This a Mini Calculator made by me.")
println("Enter 'HELP' for the instructions.\nEnter 'QUIT' to exit.")
variable = uppercase(readline())

if variable == "HELP"
    println("""
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
    
    variable = uppercase(readline())
    if variable == ""
        # Function definitions
        function addition(n1, n2)
            add = n1 + n2
            println("Addition of $n1 and $n2 is $add.")
        end
        
        function subtraction(n1, n2)
            sub = n1 - n2
            println("Subtraction of $n1 and $n2 is $sub.")
        end
        
        function multiplication(n1, n2)
            mul = n1 * n2
            println("Multiplication of $n1 and $n2 is $mul.")
        end
        
        function division(n1, n2)
            div = n1 / n2
            println("Division of $n1 by $n2 is $div.")
        end
        
        function raise_to(n1, n2)
            power = n1 ^ n2
            println("Power of $n1 with raise to $n2 is $power.")
        end
        
        function remainder(n1, n2)
            number = n1 % n2
            println("Remainder of $n1 divided by $n2 is $number.")
        end
        
        function quotient(n1, n2)
            number = n1 ÷ n2
            println("Quotient of $n1 divided by $n2 is $number.")
        end
        
        function factorial_func(n1)
            factor = 1
            for i in 1:n1
                factor *= i
            end
            println("Factorial of $n1 is $factor.")
        end
        
        # Define valid operators as a Set for faster lookup
        valid_operators = Set(["+", "-", "*", "/", "**", "%", "//", "!"])
        
        while true
            operator = ""
            while operator == ""
                print("Enter the operator= ")
                operator = readline()
                
                if operator == ""
                    println("Please enter any operator.")
                    continue
                end
                
                # Check if operator is valid
                if operator in valid_operators
                    num1 = ""
                    num2 = ""
                    
                    if operator == "!"
                        print("Enter the number= ")
                        num1 = readline()
                        if num1 == ""
                            num1 = "0"
                        end
                        n1_val = parse(Int, num1)
                        factorial_func(n1_val)
                    else
                        print("Enter the number= ")
                        num1 = readline()
                        print("Enter the second number= ")
                        num2 = readline()
                        
                        if num1 == ""
                            num1 = "0"
                        end
                        if num2 == ""
                            num2 = "0"
                        end
                        
                        # Convert strings to numbers
                        n1_val = parse(Int, num1)
                        n2_val = parse(Int, num2)
                        
                        # Execute operations
                        if operator == "+"
                            addition(n1_val, n2_val)
                        elseif operator == "-"
                            subtraction(n1_val, n2_val)
                        elseif operator == "*"
                            multiplication(n1_val, n2_val)
                        elseif operator == "/"
                            if n2_val == 0
                                println("Cannot divide $n1_val with $n2_val.")
                            else
                                division(n1_val, n2_val)
                            end
                        elseif operator == "**"
                            raise_to(n1_val, n2_val)
                        elseif operator == "%"
                            if n2_val == 0
                                println("Cannot divide $n1_val with $n2_val therefore remainder can't be obtained.")
                            else
                                remainder(n1_val, n2_val)
                            end
                        elseif operator == "//"
                            if n2_val == 0
                                println("Cannot divide $n1_val with $n2_val therefore quotient can't be obtained.")
                            else
                                quotient(n1_val, n2_val)
                            end
                        end
                    end
                else
                    println("Invalid operator '$operator'. Please try again.")
                    println("Valid operators are: +, -, *, /, **, %, //, !")
                    operator = ""
                    continue
                end
            end
            
            print("Do you want to do more calculations (Yes/No)= ")
            repeat_input = uppercase(readline())
            
            if repeat_input == "YES"
                continue
            elseif repeat_input == "NO"
                break
            else
                println("Invalid input. Please enter 'Yes' or 'No'.")
                # Ask again
                print("Do you want to do more calculations (Yes/No)= ")
                repeat_input = uppercase(readline())
                if repeat_input == "NO"
                    break
                end
            end
        end
    end
elseif variable == "QUIT"
    println("Thank You😄😄!!")
    exit()
end

println("Thank You😄😄!!")