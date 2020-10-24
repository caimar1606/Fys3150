#include "project2.hpp"
#include <armadillo>
#include <cstdlib>
#include <iostream>
#include <tuple>
#include <iomanip>

using namespace arma;
using namespace std;

ofstream ofile;

void Jacobi::Initialize(int N, double eps, int S,double rhomax,int mode,double angfreq, string filename){
  double h;
  m_eps = eps;
  m_N = N;
  m_S = S;
  if(mode ==0){
    h = 1/double(N);
  }
  else{
    h = rhomax/double(N);
  }
  vec rho = linspace(0,rhomax,N+1);
  m_filename = filename;
  m_R = mat(N-1,N-1,fill::eye);
  m_A = mat(N-1,N-1,fill::zeros);
  if(mode == 0){
    for(int i=0;i<N-1;i++){
      for(int j=0;j<N-1;j++){
        if(i==j)
          m_A(i,j) = 2/(h*h);
        else if(i == j-1 || i == j+1)
          m_A(i,j) = -1/(h*h);
      }
    }
  }
  else if(mode==1){
    for(int i=0;i<N-1;i++){
      for(int j=0;j<N-1;j++){
        if(i==j)
          m_A(i,j) = 2/(h*h)+rho(i+1)*rho(i+1);
        else if(i == j-1 || i == j+1)
          m_A(i,j) = -1/(h*h);
      }
    }
  }
  else if(mode==2){
    for(int i=0;i<N-1;i++){
      for(int j=0;j<N-1;j++){
        if(i==j)
          m_A(i,j) = 2/(h*h)+angfreq*angfreq*rho(i+1)*rho(i+1)+1/rho(i+1);
        else if(i == j-1 || i == j+1)
          m_A(i,j) = -1/(h*h);
      }
    }
  }
}

int Jacobi::Test(double a_max){
  if(a_max*a_max > m_eps)
    return 0;
  else
    return 1;
}

tuple<int,int> Jacobi::Findkl(){
  double maxval = 0;
  int k,l;
  for(int i=0;i<m_N-1;i++){
    for(int j=0;j<m_N-1;j++){
      if(i!=j && abs(m_A(i,j)) > maxval){
        k = i;
        l = j;
        maxval = abs(m_A(i,j));
      }
    }
  }
  return make_tuple(k,l);
}

void Jacobi::ComputeB(int k, int l){
  double tau = (m_A(l,l)-m_A(k,k))/(2*m_A(k,l));
  double t = 0, c=0, s=0;
  if(tau>0)
    t = 1/(tau+sqrt(1+tau*tau));
  else
    t = -1/(-tau+sqrt(1+tau*tau));
  c = 1/sqrt(1+t*t);
  s = t*c;

  mat B = m_A;
  mat Rnew = m_R;

  for(int i = 0;i<m_N-1;i++){
    for(int j = 0; j<m_N-1;j++){
      if(i!=k && i!=l){
        B(i,k)=m_A(i,k)*c-m_A(i,l)*s;
        B(k,i)=B(i,k);
        B(i,l)=m_A(i,l)*c+m_A(i,k)*s;
        B(l,i)=B(i,l);
      }
    }
    Rnew(i,k)=c*m_R(i,k)-s*m_R(i,l);
    Rnew(i,l)=c*m_R(i,l)+s*m_R(i,k);
  }
  B(k,k)=m_A(k,k)*c*c-2*m_A(k,l)*c*s+m_A(l,l)*s*s;
  B(l,l)=m_A(l,l)*c*c+2*m_A(k,l)*c*s+m_A(k,k)*s*s;
  B(k,l)=0;
  B(l,k)=0;

  m_A = B;
  m_R = Rnew;
}

void Jacobi::Solve(){
  tuple<int,int> index;
  int max_val,k,l;
  double value;
  int count = 0;
  while(count<=m_S){

    index = Findkl();
    k = get<0>(index);
    l = get<1>(index);
    value = m_A(k,l);

    max_val = Test(value);

    if(max_val==1){
      cout <<"Number of iterations was:"<<count<<endl;
      break;
    }
    ComputeB(k,l);

    count +=1;

    }
}


void Jacobi::Print(){
  vec printvec = vec(m_N-1);
  for (int i = 0; i < m_N-1; i++){
    printvec(i)=m_A(i,i);
  }
  uvec indexes = sort_index(printvec);
  printvec = sort(printvec);
  ofile.open(m_filename);
  ofile << setiosflags(ios::scientific | ios::uppercase);
  ofile << setprecision(8) << "Eigenvalues:"<<endl;
  for (int i = 0; i < m_N-1; i++){
    ofile << setw(10) << setprecision(8)<<printvec(i)<<endl;
  }
  ofile.close();

  m_filename.insert(0,"vec");
  ofile.open(m_filename);
  ofile << setiosflags(ios::scientific | ios::uppercase);
  for(int i = 0;i <m_N-1;i++){
    ofile << setprecision(8) << "Eigenvector"<< i << ":" <<endl;
    ofile << setw(10) << setprecision(8)<<m_R.col(indexes(i))<<endl;
  }
}
