exec = maze
sources = $(wildcard *.cpp)
objects = $(sources:.cpp=.o)



$(exec): $(objects)
	g++ $(objects) -o $(exec)

%.o: %.cpp 
	g++ -c $(flags) $< -o $@

install:
	make
	cp ./maze /usr/local/bin/maze

clean:
	-rm *.o maze
