from robot import Robot 

robot = Robot()
robot.env.print_grid(robot.x, robot.y)


while True:
    key = input("Enter command (F/B/L/R/A/Q): ")

    if key == "F":
        robot.forward()
    elif key == "B":
        robot.backward()
    elif key == "L":
        robot.left()
    elif key == "R":
        robot.right()
    elif key == "A":
        steps = int(input("Enter steps: "))
        robot.auto_move(steps)
    elif key == "Q":
        break

    robot.env.print_grid(robot.x, robot.y)

