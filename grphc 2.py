import turtle
import colorsys

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest
t.hideturtle()

h = 0.0  # Initial hue value

# Loop to draw 16 "petals" of the flower
for i in range(16):
    # Loop to draw the concentric arcs for each petal
    for j in range(18):
        # Convert HSV color to RGB
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        
        # Increment the hue for the gradient effect
        h += 0.005
        
        # Draw one side of the petal
        t.right(90)
        t.circle(150 - j * 6, 90)
        
        # Draw the other side of the petal
        t.left(90)
        t.circle(150 - j * 6, 90)
        
        # Turn around for the next arc in the petal
        t.right(180)
        
    # Draw a small arc to position for the next petal
    t.circle(40, 24)

# Finish drawing
turtle.done()