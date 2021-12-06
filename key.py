def checkSpecialKeys():
    global input
    pressed = False

    GPIO.output(L3, GPIO.HIGH)

    if (GPIO.input(C4) == 1):
        print(input)
        print("Input reset!");
        pressed = True

    GPIO.output(L3, GPIO.LOW)
    #new code for changing secrete code
    GPIO.output(L4, GPIO.HIGH)

    if (GPIO.input(C4) == 1):
        print(input)
        print("changing code...")
        secretCode = input
        print(secretCode)
    GPIO.output(L4, GPIO.LOW)




    GPIO.output(L1, GPIO.HIGH)

    if (not pressed and GPIO.input(C4) == 1):
        if input == secretCode:
            print("Code correct!")
            # TODO: Unlock a door, turn a light on, etc.
        else:
            print("Incorrect code!")
            print(input)
            # TODO: Sound an alarm, send an email, etc.
        pressed = True

    GPIO.output(L3, GPIO.LOW)

    if pressed:
        input = ""

    return pressed

# reads the columns and appends the value, that corresponds
# to the button, to a variable