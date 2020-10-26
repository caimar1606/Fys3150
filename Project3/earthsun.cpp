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

  double vel = 2*M_PI;
  vec vstartstar = {0,0};
  vec vstartearth = {0,vel};

  double Tmax = 10;
  string outputname = argv[2];
  double h = atof(argv[1]);

  solarsystem system;
  system.initialize(2);
  system.add_planet(mass(0),rstartstar,vstartstar);
  system.add_planet(mass(1),rstartearth,vstartearth);

  clock_t start, finish;
  double time;
  start = clock();
  system.solve_euler(Tmax, h);
  finish = clock();
  double cps = CLOCKS_PER_SEC;
  time =(finish - start)/cps;
  cout << "The time it takes for euler to compute " << floor(Tmax/h)+1 << " steps is " << time*1000 << "ms" << endl;
  system.print("Euler_position_"+outputname+"_object_","Euler_velocity_"+outputname+"_object_");

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
