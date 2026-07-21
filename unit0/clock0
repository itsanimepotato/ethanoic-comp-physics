Web VPython 3.2

'''
This is a program that simulates an analog clock.
We will modify this program to allow user input to:
 -- start and stop the clock
 -- set the initial time of the clock

Your first job is to read through the code and add a comment
after each hashtag saying what the next block or line of code does.
'''

# Creates a title above simulation
scene.title = "This is the title caption of a clock simulation.\nThis is a new line in the title caption.\n"
scene.append_to_title("This is yet a third line of text.")

# Global Boolean for movement
wound = False

runButton = button(bind=winding, text="click to start")
def winding():
    global wound
    wound = !wound

    if wound:
        runButton.text="click to stop"
    else:
        runButton.text="click to start"


# Clock tick lengths
big_rad = 3.1
little_rad = 2.6
micro_rad = 2.8
# Making clock ticks
for i in range(12):
    outer_x = big_rad*cos(pi*i/6)
    outer_y = big_rad*sin(pi*i/6)
    if i%3 == 0:
        inner_x = little_rad*cos(pi*i/6)
        inner_y = little_rad*sin(pi*i/6)
    else:
        inner_x = micro_rad*cos(pi*i/6)
        inner_y = micro_rad*sin(pi*i/6)
    curve(pos=[vec(outer_x, outer_y, 0), vec(inner_x, inner_y, 0)], radius = 0.05, color=color.yellow)

# Creates hands of clock
minute_hand = arrow(pos=vec(0, 0, 0.1), axis=vec(0, little_rad-0.2, 0.1), color=color.blue)
hour_hand = arrow(pos=vec(0, 0, -0.1), axis=vec(0, little_rad-0.5, -0.1), color=color.green)

# Time passing
t = 0
# Amt of time passing (movement)
dt = 0.05

#
while True:
    rate(10)
    # Starts moving if wound == True
    if wound:
        # Rotates the hand
        minute_hand.rotate(axis=vec(0, 0, -1), angle=dt, origin=vec(0, 0, 0))
        hour_hand.rotate(axis=vec(0, 0, -1), angle=dt/12, origin=vec(0, 0, 0))
        # Adds more time
        t += dt



       
