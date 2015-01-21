from PIL import Image, ImageDraw
import sys, time, math, json

class UndrawnTurtle():
    def __init__(self, start_x=0.0, start_y=0.0, start_angle=0.0):
        self.x, self.y, self.angle = start_x, start_y, start_angle
        self.points_visited = []
        self._visit()

    def forward(self, distance):
        angle_radians = math.radians(self.angle)

        self.x += math.cos(angle_radians) * distance
        self.y += math.sin(angle_radians) * distance

        self._visit()

    def right(self, angle):
        self.angle -= angle

    def left(self, angle):
        self.angle += angle

    def goto(self, x, y):
        self.x, self.y = x, y
        self._visit()

    def _visit(self):
        """
        Add point to the list of points gone to by the turtle.
        """
        self.points_visited.append((self.x, self.y))

class DrawingTurtle(UndrawnTurtle):
    def take_state(self, state):
        """
        Assume the position & heading given.
        """
        x, y, angle = state

        self.goto(x, y)
        self.angle = angle

    def get_state(self):
        """
        Returns the current position & heading as a tuple.
        """
        return self.x, self.y, self.angle

def replace(s, rules):
    """
    Runs the update rules on string s.
    """
    return "".join([rules.get(c, c) for c in s])

def draw(s, turt, distance, left_angle, right_angle):
    """
    Draws string s with the given turtle.
    """

    # A stack of x, y, angle tuples.
    stack = []

    for char in s:
        if char == "F": turt.forward(distance)
        if char == "-": turt.left(left_angle)
        if char == "+": turt.right(right_angle)
        if char == "[": stack.append(turt.get_state())
        if char == "]": turt.take_state(stack.pop())


if __name__ == "__main__":
    width, height = 600, 600
    t = DrawingTurtle(width/2, height, -90)

    L_system = json.loads(open(sys.argv[1]).read())

    s = L_system["start_str"]
    for _ in range(int(input("How many iterations? "))):
        s = replace(s, L_system["rules"])

    distance = L_system["distance"]
    left_angle = L_system["left_angle"]
    right_angle = L_system["right_angle"]
    draw(s, t, distance, left_angle, right_angle)

    canvas = Image.new('RGB', (width, height), color='white')
    canvas_draw = ImageDraw.Draw(canvas)

    canvas_draw.line(t.points_visited, (0, 0, 0))
    canvas.show()
    # canvas.save(sys.argv[2], format="gif")