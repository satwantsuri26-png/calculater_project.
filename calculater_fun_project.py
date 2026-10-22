
print("===CALCULATOR===")

num_one = float(input("Please enter your first number:"))
num_two = float(input("Please enter your second number"))
operation = input("Please enter the operation you'd like to apply; (x, +, -, ÷) :")

if operation == ("÷") :
    print ("The answer is: ", num_one/num_two )

if operation == ("x") :
    print ("The answer is: ", num_one*num_two )

if operation == ("-") :
    print ("The answer is: ", num_one/num_two )

if operation == ("+") :
    print ("The answer is: ", num_one + num_two )

else:
    print ("Sorry this operation isn't defined. Please try again")
    pass


#   Use if / elif / else to call the right function and print the result.
#   For any other word, print "Unknown operation."
# Then add:
#   except ValueError: for letters instead of numbers
#   except ZeroDivisionError: for dividing by zero
#   finally: print a thank-you line
