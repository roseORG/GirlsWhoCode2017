start = '''
Rihanna is in town for her concert. Help her get to her concert...
'''


print(start)
done = False

left= False
right= False

while not done:
    print("She's walking out of the building. Should she take a left or right?")
    print("Type 'left' to go left or 'right' to go right.")


    user_input = input()
    if user_input == "left":
        print("You decided to go left and ran into the paprazzi.") # finished the story by writing what happens
        done = True
        left= True
    elif user_input == "right":
        print("You decided to go right and ran into fans.") # finished the story writing what happens
        done = True
        right= True
    else:
        print("Wrong Option")
        done = False


done = False
while left:
    print("paprazzi are here!")
    print("Do you want to fight the paprazzi or run?")

    user_input = input()
    if user_input == "fight":
        print("Let's get it!")
        left = False

    elif user_input == "run":
        print("You broke your ankle")
        left = False
    else:
        print("Wrong Option")
        left= True
