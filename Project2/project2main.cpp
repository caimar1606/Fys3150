#include <cstdlib>
#include "project2.hpp"

using namespace std;

int main(int argc, char const *argv[]){
  int N = atof(argv[1]);
  double eps = pow(10, -atof(argv[2]));
  int S = atof(argv[3]);
  double rhomax = atof(argv[4]);
  int mode = atof(argv[5]);
  double angfreq = atof(argv[6]);
  string filename = argv[7];

  Jacobi my_solver;
  my_solver.Initialize(N, eps, S, rhomax, mode,angfreq, filename);
  my_solver.Solve();
  my_solver.Print();

  return 0;

}
