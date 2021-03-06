from mazeSolver import *
import time
import os

def intro():
    print("######################################### MAZE SOLVER ##############################")
    print("  --------------------------- CHOOSE THE ALGORITHM TO SOLVE THE MAZE-------------- ")
    print(" |  1 - Depth-first Search Algorithm                                              |")
    print(" |  2 - Breadth-first Search Algorithm                                            |")
    print("  -------------------------------------------------------------------------------- ")
    print("####################################################################################")
    while True:
        algorithm = input("Algorithm selection (1 | 2): ")
        if algorithm.isdigit():
            algorithm = int(algorithm)
        else:
            raise ValueError("Choose a valid option (1 | 2)")
            continue
        break
    return algorithm
        
def run(algorithm):
    #os.system('a.exe' if os.name == 'nt' else './a.out')
    try:
        if len(sys.argv) != 2:
            sys.exit("Usage: python main.py ./mazes/maze.txt")

        maze = Maze(sys.argv[1])
        print("Maze:")
        maze.print()

        # solving the maze
        print("Solving...")
        start = time.time()
        maze.solve(algorithm)
        end = time.time()
        finalTime = end - start

        print("States Explored:", maze.num_explored)
        print("Time: {} s".format(finalTime))

        print("Solution:")
        maze.print()
        maze.output_image("maze.png", show_explored=True)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Unexpected ERROR\n")
        sys.exit()


if __name__ == "__main__":
    algorithm = intro()
    run(algorithm)
    