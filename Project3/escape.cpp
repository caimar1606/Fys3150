#include <cstdlib>
#include "solarsystem.hpp"
#include <armadillo>
#include <math.h>

using namespace std;
using namespace arma;

int main(int argc, char const *argv[]){
  vec mass = {1,3.0024584*pow(10,-6)};
  vec rstartstar = {0,0};
  vec rstartearth = {1,0};

  vec vstartstar = {0,0};
  vec vstartearth = {0,atof(argv[3])};

  double Tmax = atof(argv[4]);
  string outputname = argv[2];
  double h = atof(argv[1]);


  clock_t start, finish;
  double time;
  double cps = CLOCKS_PER_SEC;

  solarsystem system2;
  system2.initialize(2);
  system2.add_planet(mass(0),rstartstar,vstartstar);
  system2.add_planet(mass(1),rstartearth,vstartearth);

  start = clock();
  system2.solve_verlet(Tmax,h);
  finish = clock();
  time = (finish - start)/cps;
  cout << "The time it takes for velocity verlet to compute " << floor(Tmax/h)+1 << " steps is " << time*1000 << "ms" << endl;
  system2.print("verlet_position_"+outputname+"_object_","verlet_velocity_"+outputname+"_object_",10);

}
