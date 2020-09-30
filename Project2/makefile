all:compile execute2b execute2d execute2e
alltest:compiletest executetest

compile:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project2.exe project2main.cpp Jacobi.cpp -larmadillo -llapack -lblas

compiletest:
	c++ -std=c++11 -stdlib=libc++ -O3 -Wall -o project2test.exe Jacobi.cpp test-jacobi.cpp testmain.cpp -larmadillo -llapack -lblas

executetest:
	./project2test.exe

execute2b:
	./project2.exe 201 20 100000 1 0 0 buckbeam.txt

execute2d:
	./project2.exe 226 20 100000 4.5 1 0 oneelec.txt

execute2e:
	./project2.exe 251 20 150000 18 2 0.05 twoelec.txt
