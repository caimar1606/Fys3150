all: compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project5.exe main.cpp class_solver.cpp -larmadillo -llapack -lblas
execute:
	./project5.exe 1 1 20001 101 forward0_01dx backward0_01dx CN0_01dx
