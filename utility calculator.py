# write a program which would keep adding numbers and stop as soon as the usder presses q on the keyboard
sum = 0
while(True):
    user_input = (input("Enter the price of the item you'd like to purchace or enter 'q' to exit"))
    if (user_input != 'q'):
        sum = int(user_input) + sum
        print("total amount so far is" )
        print(sum)
        print (f"your total bill so far is {sum}")
    else:
        print("thank you for shopping with us.")
        break

    

        
