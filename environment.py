class Environment:
    def __init__(self):
        self.size = 10
        self.obstacles = {(4, 5), (6, 8), (3, 1), (2, 7)}

    def grid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def nope(self, x, y):
        return (x, y) in self.obstacles

    def valid(self, x, y):
        return self.grid(x, y) and not self.nope(x, y)

    def print_grid(self, robot_x, robot_y):
        for y in reversed(range(self.size)):
            for x in range(self.size):
                if (x, y) == (robot_x, robot_y):
                    print("R", end=" ")
                elif (x, y) in self.obstacles:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()
