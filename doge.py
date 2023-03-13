import turtle
# Create a turtle object and set its speed to maximum
dog = turtle.Turtle()
dog.speed(0)

# Define a function to draw the dog's body
def draw_body():
    dog.penup()
    dog.goto(-50, 0)
    dog.pendown()
    dog.circle(50)

# Define a function to draw the dog's legs
def draw_legs():
    leg_positions = [(-30, -30), (30, -30), (-30, -70), (30, -70)]
    for x, y in leg_positions:
        dog.penup()
        dog.goto(x, y)
        dog.pendown()
        dog.forward(40)
        dog.penup()
        dog.backward(40)

# Define a function to animate the dog running
def run():
    for i in range(10):
        dog.clear()
        draw_body()
        if i % 2 == 0:
            dog.setheading(30)
            draw_legs()
        else:
            dog.setheading(-30)
            draw_legs()
        turtle.update()

# Set up the window and start the animation
turtle.setup(500, 500)
turtle.tracer(0)
run()

turtle.done()