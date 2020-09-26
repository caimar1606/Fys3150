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
  dmat m_A;
  dmat m_R;
  int m_S;
  string m_filename;
  int Test(double a_max);
  tuple<int,int> Findkl();
  void ComputeB(int k, int l);

public:
  void Initialize(int N, double eps, int S,double rhomax, string filename);
  void Solve();
  void Print();

};

#endif
