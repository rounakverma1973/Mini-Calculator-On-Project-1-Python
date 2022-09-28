

#Project 1
#Made my Rounak Verma #
#Working on the project of the mini calculator

name = input("Enter your name here :__");

print("Hi there, We are glad to have you here." +" "+ name);


number1 = input("Enter The first number here  :  ");
number2 = input("Enter the second number here :  ");
operator = input("Enter the operation that you would like to perform on these both two numbers:+,/,-,*  :   ");

#Converting the numbers entered by the users into Integers#
number1 = int(number1);
number2 = int(number2);

if operator == "+":
     solution1 = (number1 + number2);

     #converting the values of solution 1 into string so that it can be easily concatenated along with the string#
     solution1 = str(solution1);
     print("Hence Your final Answer is : " + solution1);

elif operator == "-":
     solution2 = (number1 - number2);
     # converting the values of solution 2 into string so that it can be easily concatenated along with the string#
     solution2 = str(solution2);
     print ("Hence Your final Answer is : "+ solution2);

elif operator == "*":
     solution3 = (number1 * number2);
     # converting the values of solution 3 into string so that it can be easily concatenated along with the string#
     solution3 = int(solution3);
     print ("Hence Your final Answer is : "+ solution3);

elif operator == "/":
     solution4 = (number1/ number2);
     # converting the values of solution 4 into string so that it can be easily concatenated along with the string#
     solution4 = str(solution4);
     print ("Hence Your final Answer is : "+solution4);

else:
    print("Oops!! It seems As if It is An Invalid Syntax  ");
    print("Trying Entering the Operations and values again.");

#Printing a entering statement#
print ("Thanks ! A lot for using our mini calculator . Hoping that you will visit the next time as well");

