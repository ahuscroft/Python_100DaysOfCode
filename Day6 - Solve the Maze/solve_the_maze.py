#Create function to turn robot to the right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Use 'while loop' to solve the maze by making the robot move along the right wall
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
