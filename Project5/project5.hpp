#ifndef project5_HPP
#define project5_HPP

#include <armadillo>

using namespace arma;
using namespace std;

class solver {
private:
  double m_L,m_T, m_dt, m_dx, m_alpha;
  int m_nt,m_nx;
  mat m_v;
  void trigsolve(vec gtilde, vec dtilde, double e, int t);

public:
  void init(double L,double T, int nt, int nx);
  void forward();
  void backward();
  void CN();
  void outputfinal(string filename);
  void output(string filename);

};

#endif
