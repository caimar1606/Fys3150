#include <cstdlib>
#include "solarsystem.hpp"
#include <armadillo>
#include <math.h>

using namespace std;
using namespace arma;

int main(int argc, char const *argv[]){
  vec mass = {1,3.0024584*pow(10,-6),atof(argv[3])};
  vec rstartstar = {-0.00615,0.00639};
  vec rstartearth = {0.866,0.485};
  vec rstartjupiter = {2.61,-4.39};

  vec vstartstar = {-0.00000724,-0.00000514};
  double day2yr = 365.242199;
  vec vstartjupiter = {0.00639*day2yr,0.00422*day2yr};
  vec vstartearth = {-0.00857*day2yr,0.0150*day2yr};

  double Tmax = 100;
  string outputname = argv[2];
  double h = atof(argv[1]);


  clock_t start, finish;
  double time;

  double cps = CLOCKS_PER_SEC;

  solarsystem system2;
  system2.initialize(3);
  system2.add_planet(mass(0),rstartstar,vstartstar);
  system2.add_planet(mass(1),rstartearth,vstartearth);
  system2.add_planet(mass(2),rstartjupiter,vstartjupiter);

  start = clock();
  system2.solve_verlet(Tmax,h);
  finish = clock();
  time = (finish - start)/cps;
  cout << "The time it takes for velocity verlet to compute " << floor(Tmax/h)+1 << " steps is " << time*1000 << "ms" << endl;
  system2.print("verlet_position_"+outputname+"_object_","verlet_velocity_"+outputname+"_object_",10);

}
