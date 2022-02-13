while (True):
    i = int(input("Enter a Number:"))
    if i<=100:
        print("Try again")
        continue
    if i>100:
        print("Congrats")
        break
