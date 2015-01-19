from turtle import Turtle, mainloop, tracer, update, mode
import branches
import time

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

def replace(s, rules):
    """
    Runs the update rules on string s.
    """
    return "".join([rules.get(c, c) for c in s])

def draw(s, turt, distance, left_angle, right_angle):
    """
    Draws string s with the given turtle.
    """
    start_time = time.time()

    # A stack of x, y, heading tuples.
    stack = []

    for char in s:
        if char == "F": turt.forward(distance)
        if char == "-": turt.left(left_angle)
        if char == "+": turt.right(right_angle)
        if char == "[": stack.append(turt.get_state())
        if char == "]": turt.take_state(stack.pop())

    print("Finished drawing", time.time() - start_time)


if __name__ == "__main__":
    mode("logo")
    t = DrawingTurtle()
    t.hideturtle()
    tracer(0)

    s = branches.start
    print("How many iterations?")
    for _ in range(int(input())):
        s = replace(s, branches.rules)

    print("Finished iterating.")
    draw(s, t, branches.distance, branches.left_angle, branches.right_angle)
    update()

    mainloop()