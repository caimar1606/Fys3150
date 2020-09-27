#ifndef project2_HPP
#define project2_HPP

#include <armadillo>
#include <cstdlib>
#include <tuple>

using namespace std;
using namespace arma;

class Jacobi{
private:
  int m_N;            // Number of intervals in mesh grid
  double m_eps;      //Tolerance
  int m_S;
  string m_filename;
  int Test(double a_max);
  void ComputeB(int k, int l);

public:
  dmat m_A;
  dmat m_R;
  tuple<int,int> Findkl();
  void Initialize(int N, double eps, int S,double rhomax,int mode,double angfreq, string filename);
  void Solve();
  void Print();

};

#endif
