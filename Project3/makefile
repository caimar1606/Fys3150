all:compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project3.exe project3main.cpp solarsystem.cpp -larmadillo -llapack -lblas

execute:
	./project3.exe 0.0001 0_00001_exact
