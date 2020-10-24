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

public:
  void initialize(int total);
  void initialize(int total, double beta);
  void add_planet(double mass, vec rstart, vec vstart);
  void solve_euler(double Tmax, double h);
  void solve_verlet(double Tmax, double h);
  mat accel(int planet, int step);
  void printr(string output);
  void printv(string output);
  void print(string outputr, string outputv);
};

#endif
