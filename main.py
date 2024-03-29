# Python
# lowercase turtle is a module and uppercase is a class
from turtle import Turtle, Screen, mainloop

class Etch:

    def __init__(self):
        # get a turtle object and a screen object
        self.__t = Turtle()
        self.__screen = Screen()

        # Set attributes on the turtle
        self.__t.color('blue')
        self.__t.pensize(2)
        self.__t.speed(0)
        self.__distance = 2
        self.__turn = 6

        # start all key presses
        self.__up_pressed = False
        self.__down_pressed = False
        self.__left_pressed = False
        self.__right_pressed = False

        # register callback
        # a callback is a function that is called from the
        # operating system
        # up
        self.__screen.onkeypress(self.__up_press, 'Up')  # don't type key it's just for type
        self.__screen.onkeyrelease(self.__up_release, 'Up')  # no ()
        # Down
        self.__screen.onkeypress(self.__down_press, 'Down')
        self.__screen.onkeyrelease(self.__down_release, 'Down')
        # left
        self.__screen.onkeypress(self.__left_press, 'Left')
        self.__screen.onkeyrelease(self.__left_release, 'Left')
        # right
        self.__screen.onkeypress(self.__right_press, 'Right')
        self.__screen.onkeyrelease(self.__right_release, 'Right')
        # toggle
        self.__screen.onkey(self.__toggle_pen, 't')
        # clear
        self.__screen.onkey(self.__clear, 'c')
        # color
        self.__screen.onkey(self.__color, 'a')
        # uit
        self.__screen.onkey(self.__quit, 'q')
        self.__screen.listen()



    def __up_press(self):
        self.__up_pressed = True

    def __up_release(self):
        self.__up_pressed = False

    def __down_press(self):
        self.__down_pressed = True

    def __down_release(self):
        self.__down_pressed = False

    def __left_press(self):
        self.__left_pressed = True

    def __left_release(self):
        self.__left_pressed = False

    def __right_press(self):
        self.__right_pressed = True

    def __right_release(self):
        self.__right_pressed = False

    def __move(self):
        if self.__up_pressed:
            self.__t.forward(self.__distance)
        elif self.__down_pressed:
            self.__t.backward(self.__distance)
        if self.__left_pressed:
            self.__t.left(self.__turn)
        elif self.__right_pressed:
            self.__t.right(self.__turn)

        self.__screen.ontimer(self.__move, 10)

    def __toggle_pen(self):
        if self.__t.isdown():
            self.__t.penup()
        else:
            self.__t.pendown()

    def __clear(self):
        self.__t.clear()

    def __color(self):
        if self.__t.color()[0] == 'red':
            self.__t.color('green')

        elif self.__t.color()[0] == 'green':
            self.__t.color('blue')

        else:
            self.__t.color('red')

    def __quit(self):
        self.__screen.bye()
    def run(self):
        self.__move()
        mainloop()  # creates game loop until loss or physically quit

if __name__ == '__main__':
    draw = Etch()
    draw.run()
