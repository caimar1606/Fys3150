#include <cstdlib>
#include "solarsystem.hpp"
#include <armadillo>
#include <math.h>

using namespace std;
using namespace arma;

int main(int argc, char const *argv[]){
  vec mass = {1,1.651*pow(10,-7),0.000002447,3.0024584*pow(10,-6),3.22613242*pow(10,-7),0.0009543,0.0002857,0.00004365,0.00005149};
  vec rstartstar = {-0.00615,0.00639};
  vec rstartearth = {0.866,0.485};
  vec rstartmercury = {0.327,0.0781};
  vec rstartvenus = {-0.334,0.645};
  vec rstartmars = {1.28,0.622};
  vec rstartjupiter = {2.61,-4.39};
  vec rstartsaturn = {5.17,-8.55};
  vec rstarturanus = {15.5,12.3};
  vec rstartneptune = {29.4,-5.45};

  vec vstartstar = {-0.00000724,-0.00000514};
  double day2yr = 365.242199;
  vec vstartjupiter = {0.00639*day2yr,0.00422*day2yr};
  vec vstartearth = {-0.00857*day2yr,0.0150*day2yr};
  vec vstartmercury = {-0.0114*day2yr,0.0288*day2yr};
  vec vstartvenus = {-0.0181*day2yr,-0.00934*day2yr};
  vec vstartmars = {-0.00552*day2yr,0.0138*day2yr};
  vec vstartsaturn = {0.00446*day2yr,0.00287*day2yr};
  vec vstarturanus = {-0.00247*day2yr,0.00290*day2yr};
  vec vstartneptune = {0.000550*day2yr,0.00311*day2yr};

  double Tmax = atof(argv[3]);
  string outputname = argv[2];
  double h = atof(argv[1]);


  clock_t start, finish;
  double time;

  double cps = CLOCKS_PER_SEC;

  solarsystem system2;
  system2.initialize(3);
  system2.add_planet(mass(0),rstartstar,vstartstar);
  system2.add_planet(mass(1),rstartmercury,vstartmercury);
  system2.add_planet(mass(2),rstartvenus,vstartvenus);
  system2.add_planet(mass(3),rstartearth,vstartearth);
  system2.add_planet(mass(4),rstartmars,vstartmars);
  system2.add_planet(mass(5),rstartjupiter,vstartjupiter);
  system2.add_planet(mass(6),rstartsaturn,vstartsaturn);
  system2.add_planet(mass(7),rstarturanus,vstarturanus);
  system2.add_planet(mass(8),rstartneptune,vstartneptune);
  start = clock();
  system2.solve_verlet(Tmax,h);
  finish = clock();
  time = (finish - start)/cps;
  cout << "The time it takes for velocity verlet to compute " << floor(Tmax/h)+1 << " steps is " << time*1000 << "ms" << endl;
  system2.print("verlet_position_"+outputname+"_object_","verlet_velocity_"+outputname+"_object_",10);

}
