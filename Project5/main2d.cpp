#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>

//double L,double T, int nt, int nx

using namespace std;
using namespace arma;

mat func(vec x,double L){
  mat matrix = mat(x.n_elem,x.n_elem,fill::zeros);
  for(int i = 0;i <x.n_elem;i++){
    for(int j = 0;j <x.n_elem;j++){
      matrix(i,j) = +1292/L*(L-x(i))-1300;
    }
  }
  return matrix;
}

int main(int argc,char *argv[]){
  double k = 2.5;
  double rho = 3.5*10*10*10;
  double cp = 1000;
  double L = atof(argv[1])*1000/sqrt(k);
  double T = atof(argv[2])*3.16*pow(10,16)/(rho*cp);
  int nt = atoi(argv[3]);
  int nx = atoi(argv[4]);
  string name = argv[5];;

  solver system;

  system.init2d(L,T,nt,nx,*func);
  system.solve2d();
  system.output2d(name);
  system.outputfinal2d(name);

  return 0;
}
