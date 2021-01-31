while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == 'quit':
        print("...Exiting progrmam")
        break
    elif text == "H20":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")