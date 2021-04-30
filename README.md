# Maze Solver
## Pre requirements
	python 3.x and gcc compiler installed 
## Instalation
	1- install the python environment requirements:
		pip install -r requirements.txt

	2- compile the cpp program:
		g++ mazeGenerator.cpp

## About The Program 
	This is a terminal based maze solver program.
	The program works with two options of algorithms to solve the maze,
	the first option is the Depth-first search algorithm
	and the second option is the breadth-first search algorithm.
## How to run
	1- To create a new maze, run the compiled cpp file:
		LINUX or MACOS : ./a.out
		WINDOWS : ./a.exe

	2- To run the solver:
		python3 main.py ./mazes/maze.txt
## Depth-first search
	Depth-first search (DFS) is an algorithm for traversing or
	searching tree or graph data structures. The algorithm starts 
	at the root node (selecting some arbitrary node as the root 	
	node in the case of a graph) and explores as far as possible 
	along each branch before backtracking.

## Breadth-first search
	Breadth-first search (BFS) is an algorithm for traversing or 
	searching tree or graph data structures. It starts at the 
	tree root (or some arbitrary node of a graph, sometimes 
	referred to as a 'search key'), and explores all of the 
	neighbor nodes at the present depth prior to moving on to the 
	nodes at the next depth level.


	It uses the opposite strategy of depth-first search, which 
	instead explores the node branch as far as possible before 
	being forced to backtrack and expand other nodes.
