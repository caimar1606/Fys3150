#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>
#include <math.h>

//double L,double T, int nt, int nx

using namespace std;
using namespace arma;

mat func(vec x,double L){
  mat matrix = mat(x.n_elem,x.n_elem,fill::zeros);
  for(int i = 0;i <x.n_elem;i++){
    for(int j = 0;j <x.n_elem;j++){
      matrix(i,j) = sin(M_PI/L*x(i))*sin(M_PI/L*x(j));
    }
  }
  return matrix;
}


int main(int argc,char *argv[]){
  double L = atof(argv[1]);
  double T = atof(argv[2]);
  int nt = atoi(argv[3]);
  int nx = atoi(argv[4]);
  string name = argv[5];;

  solver system;

  system.init2d(L,T,nt,nx,func);
  system.solve2d();
  system.output2d(name);
  system.outputfinal2d(name);

  return 0;
}
