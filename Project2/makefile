all:compile execute

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project2.exe project2main.cpp Jacobi.cpp -larmadillo -llapack -lblas

compiletest:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project2test.exe Jacobi.cpp test-jacobi.cpp testmain.cpp -larmadillo -llapack -lblas

execute2b:
	./project2.exe 100 20 100000 1 0 0 2b.txt

executetest:
	./project2test.exe

execute2d:
	./project2.exe 100 20 100000 4 1 0 2d.txt

execute2e:
	./project2.exe 200 25 100000 20 2 0.25 2efequal1.txt
