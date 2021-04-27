from mazeSolver import *

def intro():
    print("############### MAZE SOLVER ###############")
    print("          CHOOSE THE ALGORITHM TO SOLVE THE MAZE")
    print("   1 - Stack Algorithm")
    print("   2 - Queue Algorithm")
    while True:
        algorithm = input("Algorithm selection: ")
        if algorithm.isdigit():
            algorithm = int(algorithm)
            break
        else:
            raise ValueError("Choose a valid option (1 or 2)")
            continue
    return algorithm
        


if __name__ == "__main__":
    algorithm = intro()
    try:
        if len(sys.argv) != 2:
            sys.exit("Usage: python main.py ./mazes/maze.txt")

        maze = Maze(sys.argv[1])
        print("Maze:")
        maze.print()
        print("Solving...")
        maze.solve(algorithm)
        print("States Explored:", maze.num_explored)
        print("Solution:")
        maze.print()
        maze.output_image("maze.png", show_explored=True)
    except:
        print("Unexpected ERROR")
        sys.exit()