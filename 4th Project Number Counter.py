def loopCycle():
    count = int(input("Enter the number you want to start the counter: ")) #Start at 0
    endingCounter = int(input("Enter the number you want the counter to end: "))
    addingNumber = int(input("Enter how much you want to add every time: "))

    while count <= endingCounter:
        print(count)
        count = count + addingNumber

    print("The counter has ended")

loopCycle()