n = 19
no_of_guesses = 0
print("!!Guess the correct no between 1 - 100 !!"
      "\n YOU HAVE ONLY 5 Guesses"
      "\n!!! LETS BEGIN !!!")
while(no_of_guesses<=4):
    i=int(input("Enter the no : "))
    no_of_guesses = no_of_guesses+1
    if i>n:
        print("Enter the smaller no")
    elif i<n:
        print("Enter the Greater no")
    elif i==n:
        print("You have guessed the right no")
        print("You Won")
        break
    if no_of_guesses>4:
        print("Out of guesses")
        print("You Lose")
        break