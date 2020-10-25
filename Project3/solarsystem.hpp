#ifndef solarsystem_HPP
#define solarsystem_HPP

#include <armadillo>
#include <cstdlib>


using namespace std;
using namespace arma;


class solarsystem{
private:
  mat m_r;      //posisjoner
  vec m_rstart;
  mat m_v;      //hastigheter
  vec m_vstart;
  vec m_M;
  int m_planets;
  vec m_GdM;
  double m_beta;
  double m_rel;

public:
  void initialize(int total, double beta = 2, double rel = 0);
  void add_planet(double mass, vec rstart, vec vstart);
  mat accel(int planet, int step);
  void solve_euler(double Tmax, double h);
  void solve_verlet(double Tmax, double h);
  void print(string outputr, string outputv, int skip = 1);
};

#endif
