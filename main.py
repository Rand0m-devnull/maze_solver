from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 6, 8, 25, 25, win, 10)
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

if __name__ == "__main__":
    main()