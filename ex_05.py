large = None
small = None

while True:
    usrInput = input("Enter a number: ")
    
    try:
        usrVar = int(usrInput)
    except:
        if usrInput == 'done':
            print('Maximum is ', large)
            print('Minimum is ', small)
            break
        else:
            print('Invalid Input')
            continue

    if large is None:
        large = usrVar
        small = usrVar
    elif large < usrVar:
        large = usrVar
    elif small > usrVar:
        small = usrVar

    