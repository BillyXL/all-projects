import turtle

def draw_somalian():
    """
    Function to draw a Somali flag using the Turtle graphics library.

    Draws a Somali flag which consists of a blue background with a large white star in the center.

    No parameters are needed to be passed to this function.

    Returns:
    - None
        This function does not return anything, it just draws the Somali flag using Turtle graphics.
    """

    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.title("Somali Flag")
    screen.bgcolor("blue")

    # Create a Turtle object
    flag_turtle = turtle.Turtle()
    flag_turtle.speed(0)  # Set the drawing speed to the maximum

    # Draw the white star in the center
    flag_turtle.color("white")
    flag_turtle.begin_fill()
    for _ in range(5):
        flag_turtle.forward(100)
        flag_turtle.right(144)
    flag_turtle.end_fill()

    # Hide the Turtle and display the flag
    flag_turtle.hideturtle()
    turtle.done()

# Call the function to draw the Somali flag
draw_somalian()