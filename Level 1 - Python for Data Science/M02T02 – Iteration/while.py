### While loop problems

# Write a program that asks the user to guess a secret number (for example, 7). The program should keep asking the user for a guess until they enter the correct number, using a while loop. Each time the guess is wrong, print a message asking them to try again.

secret_number = 7

user_input = int(input("Try to guess the secret single-digit number. "))

while True:
    if user_input == 7:
        print("7 is correct!")
        break
    else:
        print("Guess again.")
        user_input = int(input("Enter the secret single-digit number. "))


# Write a program that asks the user to enter a number. Then, using a while loop, print all the numbers from 1 up to and including the number entered by the user.

num = 1

user_input = int(input("Please enter a positive single-digital number. "))

while num <= user_input:
    print(num)
    num = num + 1 
    break
