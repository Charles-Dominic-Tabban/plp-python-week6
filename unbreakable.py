while True:
    try:
        number = int(input("Enter a positive whole number: "))

        if number <= 0:
            print("Please enter a positive number.")
        else:
            print("Valid number:", number)
            break

    except ValueError:
        print("Not a number. Please try again.")