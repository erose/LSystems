from turtle import Turtle, mainloop, tracer, update, mode

dist, angle = 20, 25

class DrawingTurtle(Turtle):
    def take_state(self, state):
        """
        Assume the position & heading given.
        """
        x, y, heading = state

        # Speed 0 is instantaneous travel.
        orig_speed = self.speed()
        self.speed(0)

        self.goto(x, y)
        self.setheading(heading)

        self.speed(orig_speed)

    def get_state(self):
        """
        Returns the current position & heading as a tuple.
        """
        return self.xcor(), self.ycor(), self.heading()

def replace(s):
    return s.replace("F", "F[-F]F[+F][F]")

def draw(s):
    # A stack of x, y, heading tuples.
    stack = []

    for char in s:
        if char == "F": t.forward(dist)
        if char == "+": t.right(angle)
        if char == "-": t.left(angle)
        if char == "[": stack.append(t.get_state())
        if char == "]": t.take_state(stack.pop())


if __name__ == "__main__":
    mode("logo")
    t = DrawingTurtle()
    t.hideturtle()
    tracer(0)

    s = "F"
    print("How many iterations?")
    for _ in range(int(input())):
        s = replace(s)

    draw(s)
    update()

    mainloop()