#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>

//double L,double T, int nt, int nx

using namespace std;
using namespace arma;

vec func(vec x,double L){
  return -1292/L*x-8;
}

vec Qnormal(vec x,double L,double t){
  double rho = 3.5*10*10*10;
  double cp = 1000;
  double scale = 1/(rho*cp);
  vec values = vec(x.n_elem,fill::zeros);
  for(int i = 0;i <x.n_elem;i++){
    if(x(i)<=L/6){
      values(i)=1.4*pow(10,-6)*scale;
    }
    else if(x(i)<=L/3){
      values(i) = 0.35*pow(10,-6)*scale;
    }
    else{
      values(i) = 0.05*pow(10,-6)*scale;
    }
  }
  return values;
}

vec Qmore(vec x,double L,double t){
  vec values = vec(x.n_elem,fill::zeros);
  double rho = 3.5*10*10*10;
  double cp = 1000;
  double scale = 1/(rho*cp);
  for(int i = 0;i <x.n_elem;i++){
    if(x(i)<=L/6){
      values(i)=1.4*pow(10,-6)*scale;
    }
    else if(x(i)<=L/3){
      values(i) = 0.35*pow(10,-6)*scale;
    }
    else{
      values(i) = (0.5+0.05)*pow(10,-6)*scale;
    }
  }
  return values;
}

vec Qexp(vec x,double L, double t){
  vec values = vec(x.n_elem,fill::zeros);
  double rho = 3.5*10*10*10;
  double cp = 1000;
  double scale = 1/(rho*cp);
  double timescale = 3.16*pow(10.0,16.0);
  for(int i = 0;i <x.n_elem;i++){
    if(x(i)<=L/6){
      values(i)=1.4*pow(10,-6)*scale;
    }
    else if(x(i)<=L/3){
      values(i) = 0.35*pow(10,-6)*scale;
    }
    else{
      values(i) = (0.2*pow(2,-t/(4.47*timescale))+0.2*pow(2,-t/(14*timescale))+0.1*pow(2,-t/(1.25*timescale))+0.05)*pow(10,-6)*scale;
    }
  }
  return values;
}

int main(int argc,char *argv[]){
  double k = 2.5;
  double rho = 3.5*10*10*10;
  double cp = 1000;
  double gamma = sqrt(k/(rho*cp));
  double L = atof(argv[1])*1000/gamma;
  double T = atof(argv[2])*3.16*pow(10.0,16.0);
  int nt = atoi(argv[3]);
  int nx = atoi(argv[4]);
  string namenoQ = argv[5];
  string namenormalQ = argv[6];
  string namemoreQ = argv[7];
  string nameexpQ = argv[8];

  solver noQ;
  solver normalQ;
  solver moreQ;
  solver expQ;

  noQ.init(L,T,nt,nx,*func);
  noQ.CN();
  noQ.output(namenoQ);
  noQ.outputfinal(namenoQ);

  normalQ.init(L,T,nt,nx,*func);
  normalQ.CNwQ(Qnormal);
  normalQ.output(namenormalQ);
  normalQ.outputfinal(namenormalQ);

  moreQ.init(L,T,nt,nx,*func);
  moreQ.CNwQ(Qmore);
  moreQ.output(namemoreQ);
  moreQ.outputfinal(namemoreQ);

  expQ.init(L,T,nt,nx,*func);
  expQ.CNwQ(Qexp);
  expQ.output(nameexpQ);
  expQ.outputfinal(nameexpQ);
  return 0;
}
