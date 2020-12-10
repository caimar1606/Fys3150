#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>

//double L,double T, int nt, int nx

using namespace std;
using namespace arma;

vec func(vec x,double L){
  return -1/L*x;
}

int main(int argc,char *argv[]){
  double L = atof(argv[1]);
  double T = atof(argv[2]);
  int nt = atoi(argv[3]);
  int nx = atoi(argv[4]);
  string namef = argv[5];
  string nameb = argv[6];
  string nameCN = argv[7];

  solver feuler;
  solver beuler;
  solver CNs;

  feuler.init(L,T,nt,nx,*func);
  feuler.forward();
  feuler.output(namef);
  feuler.outputfinal(namef);

  beuler.init(L,T,nt,nx,*func);
  beuler.backward();
  beuler.output(nameb);
  beuler.outputfinal(nameb);

  CNs.init(L,T,nt,nx,*func);
  CNs.CN();
  CNs.output(nameCN);
  CNs.outputfinal(nameCN);

  return 0;
}
