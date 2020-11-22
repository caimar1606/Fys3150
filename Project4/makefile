all:compile execute

all2:compile2 execute2

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project4.exe project4.cpp -larmadillo -llapack -lblas

compile2:
	mpic++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project4par.exe Project4par.cpp -larmadillo -llapack -lblas

execute:
	./project4.exe 2 1 100000 L20T1100000c L20T1Vec

execute2:
	mpirun -n 4 ./project4par.exe 40 2.27 2.33 0.005 1400000 L40closer
