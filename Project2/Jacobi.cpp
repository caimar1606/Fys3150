#include "project2.hpp"
#include <armadillo>
#include <stdlib>
#include <iostream>

using namespace arma;
using namespace std;


void Jacobi::Initialize(int N, double eps, int S){
  m_eps = eps;
  m_N = N;
  m_S = S;
  mat A = mat(N-1,N-1,fill::zeros);
  for(int i=0;i<N-1;i++){
    for(int j=0;j<N-1;j++){
      if(i==j)
        A(i,j) = 2;
      else if(i == j-1 || i == j+1)
        A(i,j) = -1;
    }
  }
  double h = 1/N;
  m_A = A/(h*h);
}

int Jacobi::Test(double a_max){
  if(a_max*a_max > m_eps)
    return 0;
  else
    return 1;
}

tuple Jacobi::Findkl(){
  double maxval = 0;
  int k,l;
  for(int i=0;i<N-1;i++){
    for(int j=0;j<N-1;j++){
      if(i!=j && abs(m_A(i,j)) > maxval){
        k = i;
        l = j;
        maxval = m_A(i,j);
      }
    }
  }
  return make_tuple(k,l)
}

void Jacobi::Computeb(int k, int l){
  tau = (m_A(l,l)-m_A(k,k))/(2*m_A(k,l));
  double t = 0, c=0, s=0;
  if(tau>0)
    t = 1/(tau+sqrt(1+tau*tau));
  else
    t = -1/(tau+sqrt(1+tau*tau));
  c = 1/sqrt(1+t*t);
  s = t*c;

  mat B = m_A;

  for(int i = 0;i<N-1;i++){
    for(int j = 0; j<N-1;j++){
      if(i!=k && i!=l)
        B(i,k)=m_A(i,k)*c-m_A(i,l)*s;
        B(i,l)=m_A(i,l)*c-m_A(i,l)*s;
    }
  }
  B(k,k)=m_A(k,k)*c*c-2*m_A(k,l)*c*s+m_A(l,l)*s*s;
  B(l,l)=m_A(l,l)*c*c-2*m_A(k,l)*c*s+m_A(k,k)*s*s;
  B(k,l)=0;
  B(l,k)=0;

  m_A = B
}

void Jacobi::solve(){
  tuple index;
  int max_val;
  int count = 0;
  while(count<=S){

    index = Findkl();
    max_val = test(m_A(index));

    if(max_val==1)
      break;

    Computeb(index(0),index(1));

    count +=1;

    }
}


void Jacobi::print(){
  
}
