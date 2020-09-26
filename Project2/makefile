all:compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project2.exe project2main.cpp Jacobi.cpp -larmadillo -llapack -lblas

execute:
	./project2.exe
