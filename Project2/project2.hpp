#ifndef project2_HPP
#define project2_HPP

class Jacobi{
private:
  int m_N;            // Number of intervals in mesh grid
  double m_eps;      //Tolerance
  mat m_A;
  int m_S;
  int Test(double a_max);
  tuple Findkl();
  void ComputeB(int k, int l);


public:
  void Initialize(int N, double eps, int S);
  void Solve()
  void Print()

}

#endif
