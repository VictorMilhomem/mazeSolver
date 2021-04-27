from mazeSolver import *

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            sys.exit("Usage: python maze.py maze.txt")

        maze = Maze(sys.argv[1])
        print("Maze:")
        maze.print()
        print("Solving...")
        maze.solve()
        print("States Explored:", maze.num_explored)
        print("Solution:")
        maze.print()
        maze.output_image("maze.png", show_explored=True)
    except:
        print("Unexpected ERROR")
        sys.exit()