def willYouMakeIt(Station, Mpg, GLeft):

    if Station/GLeft <= Mpg:
        print("You will make it")
    else:
        print("You wont make it")

willYouMakeIt(50, 25, 2)

willYouMakeIt(int(input("How far is the station? : ")), int(input("What is your gas miledge? :")), int(input("How many Gallons left? :")))




