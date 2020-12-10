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
  cube m_vc;
  void trigsolve(vec gtilde, vec dtilde, double e, int t);
  mat makemat();

public:
  void init(double L,double T, int nt, int nx,vec (*func)(vec,double));
  void init2d(double L,double T, int nt, int nx,mat (*func)(vec,double));
  void forward();
  void backward();
  void CN();
  void solve2d(double eps = pow(10,-6),int S = 10000);
  void outputfinal(string filename);
  void output(string filename);
  void outputfinal2d(string filename);
  void output2d(string filename);
};

#endif
