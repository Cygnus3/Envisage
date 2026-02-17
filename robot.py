from environment import Environment


class Robot:

    def __init__(self):
        self.env = Environment()
        self.x = 0
        self.y = 0
        self.direction = "N"

    def forward(self):
        next_x = self.x
        next_y = self.y

        if self.direction == "N":
            next_y += 1
        elif self.direction == "S":
            next_y -= 1
        elif self.direction == "E":
            next_x += 1
        elif self.direction == "W":
            next_x -= 1

        if self.env.valid(next_x, next_y):
            self.x = next_x
            self.y = next_y
        else:
            print("Obstacle detected or out of bound")

    def backward(self):
        next_x = self.x
        next_y = self.y

        if self.direction == "N":
            next_y -= 1
        elif self.direction == "S":
            next_y += 1
        elif self.direction == "E":
            next_x -= 1
        elif self.direction == "W":
            next_x += 1

        if self.env.valid(next_x, next_y):
            self.x = next_x
            self.y = next_y
        else:
            print("Obstacle detected or out of bounds")

    def left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def auto_move(self, steps):

        for _ in range(steps):

            next_x = self.x
            next_y = self.y

            if self.direction == "N":
                next_y += 1
            elif self.direction == "S":
                next_y -= 1
            elif self.direction == "E":
                next_x += 1
            elif self.direction == "W":
                 next_x -= 1

            if self.env.valid(next_x, next_y):
                self.x = next_x
                self.y = next_y
            else:
                self.right()


            


