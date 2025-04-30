from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.shapesize(0.5)
my_screen = Screen()

def move_fd():
    tim.fd(10)

def move_bck():
    tim.backward(10)

def count_cl():
    tim.left(10)

def clock_ws():
    tim.right(10)

def clean():
    tim.clear()
    tim.pu()
    tim.home()

my_screen.listen()
my_screen.onkey(key= "W",fun= move_fd)
my_screen.onkey(key= "S",fun= move_bck)
my_screen.onkey(key= "A",fun= count_cl)
my_screen.onkey(key= "D",fun= clock_ws)
my_screen.onkey(key= "C",fun= clean)

my_screen.exitonclick()