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



    def __up_press(self):
        pass

    def __up_release(self):
        pass

    def __down_press(self):
        pass

    def __down_release(self):
        pass

    def __left_press(self):
        pass

    def __left_release(self):
        pass

    def __right_press(self):
        pass

    def __right_release(self):
        pass

    def __move(self):
        pass

    def __toggle_pen(self):
        pass

    def __clear(self):
        pass

    def __color(self):
        pass

    def __quit(self):
        pass
    def run(self):
        pass

if __name__ == '__main__':
    draw = Etch()
    draw.run()
