all: compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project5.exe main.cpp class_solver.cpp -larmadillo -llapack -lblas
execute:
	./project5.exe 1 1 20001 101 forward0_01dx backward0_01dx CN0_01dx

all2d: compile2d execute2d

compile2d:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project52d.exe main2d.cpp class_solver.cpp -larmadillo -llapack -lblas

execute2d:
	./project52d.exe 120 1 1201 61 noQ
