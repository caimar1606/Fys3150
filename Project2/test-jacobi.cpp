#include "catch.hpp"
#include "project2.hpp"
#include <cstdlib>

using namespace std;

TEST_CASE("Testing maxval"){
  Jacobi test;
  int N = 4; double eps = pow(10,-8); int S = 5; double rhomax = 0;int mode =0;double angfreq=0; string filename = "testing";
  test.Initialize(N,eps,S,rhomax,mode,angfreq,filename);
  tuple<int,int> index = test.Findkl();
  int k = get<0>(index);
  int l = get<1>(index);

  REQUIRE(k==0);
  REQUIRE(l==1);
  REQUIRE(test.m_A(k,l)==Approx(-16));
}

TEST_CASE("Testing eigenval no potential"){
  Jacobi test;
  int N = 10; double eps = pow(10,-20);int S = 10000;double rhomax = 0;int mode = 0;double angfreq=0; string filename = "test_eigen_no_pot.txt";
  test.Initialize(N,eps,S,rhomax,mode,angfreq,filename);
  test.Solve();

  vec A = vec(N-1,fill::zeros);
  for(int i=0;i<N-1;i++){
    A(i)=test.m_A(i,i);
  }
  A = sort(A);

  Approx target1 = Approx(9.78869674).epsilon(0.005);
  Approx target2 = Approx(38.1966011).epsilon(0.005);
  Approx target3 = Approx(82.44294954).epsilon(0.005);

  REQUIRE(A(0)==target1);
  REQUIRE(A(1)==target2);
  REQUIRE(A(2)==target3);
}

TEST_CASE("Testing eigenval with potential"){
  Jacobi test;
  int N = 100; double eps = pow(10,-22);int S = 1000000;int rhomax = 10;int mode = 1; double angfreq=0; string filename = "test_eigen_with_pot.txt";
  test.Initialize(N,eps,S,rhomax,mode,angfreq,filename);
  test.Solve();

  vec A = vec(N-1,fill::zeros);
  for(int i=0;i<N-1;i++){
    A(i)=test.m_A(i,i);
  }
  A = sort(A);

  Approx target1 = Approx(3).epsilon(0.005);
  Approx target2 = Approx(7).epsilon(0.005);
  Approx target3 = Approx(11).epsilon(0.005);

  REQUIRE(A(0)==target1);
  REQUIRE(A(1)==target2);
  REQUIRE(A(2)==target3);
}
