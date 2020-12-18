all: compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project5.exe main.cpp class_solver.cpp -larmadillo -llapack -lblas
execute:
	./project5.exe 1 1 201 11 forward0_1dx backward0_1dx CN0_1dx

all2d: compile2d execute2d

compile2d:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project52d.exe main2d.cpp class_solver.cpp -larmadillo -llapack -lblas

execute2d:
	./project52d.exe 1 1 201 51 2d

allQ: compileQ executeQ

compileQ:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project5Q.exe mainQ.cpp class_solver.cpp -larmadillo -llapack -lblas

executeQ:
	./project5Q.exe 120.0 1.0 50001 101 noQ normalQ moreQ expQ
