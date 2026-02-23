print("Welcome to treasure island your mission to find the teasure ")
direction = input("please type right or left").lower()
if direction == "right":
    print("game over")
elif direction == "left":
    mind = input("please type swim or wait").lower()
    if mind == "swim":
        print("game over")
    elif mind == "wait":
        door = input("please choose door between red and blue and yellow").lower()
        if door == "red":
            print("game over")
        elif door == "blue":
            print("game over")
        elif door == "yellow":
            print("game win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("invalid direction")