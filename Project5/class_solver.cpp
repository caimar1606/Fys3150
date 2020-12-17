#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>

using namespace std;
using namespace arma;

ofstream ofile;

void solver::init(double L,double T, int nt, int nx,vec (*func)(vec,double)){
  m_L = L;
  m_T = T;
  m_dt = T/(nt-1);
  m_dx = L/(nx-1);
  m_nt = nt;
  m_nx = nx;
  m_alpha = m_dt/m_dx/m_dx;
  m_v = zeros(nx,nt);
  m_v(span(1,nx-2),0) = func(linspace(m_dx,L-m_dx,nx-2),L);
}

void solver::init2d(double L,double T, int nt, int nx,mat (*func)(vec,double)){
  m_L = L;
  m_T = T;
  m_dt = T/(nt-1);
  m_dx = L/(nx-1);
  m_nt = nt;
  m_nx = nx;
  m_alpha = m_dt/m_dx/m_dx;
  m_vc = cube(nx,nx,nt,fill::zeros);
  m_vc(span(1,nx-2),span(1,nx-2),span(0,0)) = func(linspace(m_dx,L-m_dx,nx-2),L);
}


void solver::forward(){
  for(int j = 0; j < m_nt-1; j++){
    for(int i = 1; i < m_nx-1; i++){
      m_v(i, j+1) = m_v(i,j)*(1-2*m_alpha) + m_alpha*(m_v(i+1,j)+m_v(i-1,j));
    }
  }
}

void solver::backward(){
  vec gtilde;
  double e = -m_alpha;
  double diag = 1+2*m_alpha;
  double ee = e*e;
  vec dtilde = zeros(m_nx);
  dtilde +=ones(m_nx)*diag;
  for(int i =1;i<m_nx;i++){
    dtilde(i)-=ee/dtilde(i-1);
  }

  for(int j = 0; j < m_nt-1; j++){
    gtilde = m_v.col(j);
    trigsolve(gtilde,dtilde,e,j);
  }
}

void solver::CN(){
  vec gtilde;
  double e = -m_alpha;
  double diag = 2+2*m_alpha;
  double ee = e*e;
  double diagD = 2-2*m_alpha;
  double ed = m_alpha;

  vec dtilde = zeros(m_nx);
  dtilde +=ones(m_nx)*diag;

  for(int i =1;i<m_nx;i++){
    dtilde(i)-=ee/dtilde(i-1);
  }
  mat multmat = eye(m_nx,m_nx)*diagD;
  for(int i =0;i<m_nx;i++){
    for( int j = 0; j<m_nx;j++){
      if(abs(i-j)==1){
        multmat(i,j) = ed;
      }
    }
  }

  for(int j = 0; j < m_nt-1; j++){
    gtilde = multmat*m_v.col(j);
    trigsolve(gtilde,dtilde,e,j);
  }
}

void solver::CNwQ(vec (*func)(vec,double,double)){
  vec gtilde;
  double e = -m_alpha;
  double diag = 2+2*m_alpha;
  double ee = e*e;
  double diagD = 2-2*m_alpha;
  double ed = m_alpha;

  vec dtilde = zeros(m_nx);
  dtilde +=ones(m_nx)*diag;

  for(int i =1;i<m_nx;i++){
    dtilde(i)-=ee/dtilde(i-1);
  }
  mat multmat = eye(m_nx,m_nx)*diagD;
  for(int i =0;i<m_nx;i++){
    for( int j = 0; j<m_nx;j++){
      if(abs(i-j)==1){
        multmat(i,j) = ed;
      }
    }
  }
  vec addmat =zeros(m_nx);
  for(int j = 0; j < m_nt-1; j++){
    addmat(span(1,m_nx-2)) = func(linspace(m_dx,m_L-m_dx,m_nx-2),m_L,m_dt*j)*m_dt*2;
    gtilde = multmat*(m_v.col(j))+addmat;
    trigsolve(gtilde,dtilde,e,j);
  }
}



void solver::trigsolve(vec gtilde, vec dtilde, double e, int t){
  for(int i = 1; i < m_nx;i++){
    gtilde(i)-=e*gtilde(i-1)/dtilde(i-1);
  }
  for(int i = m_nx-2;i >0;i--){
    m_v(i,t+1) = (gtilde(i)-e*m_v(i+1,t+1))/dtilde(i);
  }
}

void solver::solve2d(double eps,int S){
  int matsize = (m_nx-2)*(m_nx-2);
  mat Dinv = eye(matsize,matsize)*1/(1+4*m_alpha);
  vec x,b,xnew,xdiff;
  int count;
  double val;
  count = 0;

  mat M = makemat();
  x = ones(matsize);

  for(int i = 1;i<m_nt;i++){
    b = vectorise(m_vc(span(1,m_nx-2),span(1,m_nx-2),span(i-1,i-1)));
    count = 0;
    val = 1;
    while(count < S && val > eps){
      xnew = Dinv*(b-M*x);
      xdiff = abs(xnew-x);
      val = xdiff.max();
      x = xnew;
      count++;
    }

    m_vc(span(1,m_nx-2),span(1,m_nx-2),span(i,i)) = reshape(x,m_nx-2,m_nx-2);
  }
}

void solver::outputfinal(string filename){
  ofile.open(filename+"final");
  ofile << setiosflags(ios::scientific | ios::uppercase);
  ofile << setw(18)<< setprecision(8)<<m_v.col(m_nt-1);
  ofile.close();
}

void solver::output(string filename){
  ofile.open(filename);
  ofile << setiosflags(ios::scientific | ios::uppercase);
  for(int i = 0; i <m_nt;i++){
    ofile << setw(18)<<setprecision(8)<<m_v.col(i)<<endl;
  }
  ofile.close();
}

void solver::outputfinal2d(string filename){
  ofile.open(filename+"final");
  ofile << setiosflags(ios::scientific | ios::uppercase);
  ofile << setw(18)<< setprecision(8)<<m_vc.slice(m_nt-1);
  ofile.close();
}

void solver::output2d(string filename){
  ofile.open(filename);
  ofile << setiosflags(ios::scientific | ios::uppercase);
  for(int i = 0; i <m_nt;i++){
    ofile << setw(18)<<setprecision(8)<<m_vc.slice(i)<<endl;
  }
  ofile.close();
}


mat solver::makemat(){
  mat M = zeros((m_nx-2)*(m_nx-2),(m_nx-2)*(m_nx-2));
  int jump = (m_nx-2);
  int n = 0;
  for(int j = 0;j<m_nx-2;j++){
    for(int i = 0; i < m_nx-2;i++){
      if(i==0 && j==0){
        M(n,n+1)=-m_alpha;
        M(n,n+jump)=-m_alpha;
      }
      else if(i==0 && j == m_nx-3){
        M(n,n+1)=-m_alpha;
        M(n,n-jump)=-m_alpha;
      }
      else if(i==0 && j!=0 && j!=m_nx-3){
        M(n,n+1)=-m_alpha;
        M(n,n-jump)=-m_alpha;
        M(n,n+jump)=-m_alpha;
      }

      else if(i==m_nx-3 && j==0){
        M(n,n-1)=-m_alpha;
        M(n,n+jump)=-m_alpha;
      }
      else if(i==m_nx-3 && j == m_nx-3){
        M(n,n-1)=-m_alpha;
        M(n,n-jump)=-m_alpha;
      }
      else if(i==m_nx-3&& j!=0 && j!=m_nx-3){
        M(n,n+jump)=-m_alpha;
        M(n,n-1)=-m_alpha;
        M(n,n-jump)=-m_alpha;
      }
      else if(j==0 && i!=0 && i!=m_nx-3){
        M(n,n+1)=-m_alpha;
        M(n,n+jump)=-m_alpha;
        M(n,n-1)=-m_alpha;
      }
      else if(j==m_nx-3&& i!=0 && i!=m_nx-3){
        M(n,n-1)=-m_alpha;
        M(n,n+1)=-m_alpha;
        M(n,n-jump)=-m_alpha;
      }
      else{
        M(n,n+1)=-m_alpha;
        M(n,n-1)=-m_alpha;
        M(n,n+jump) = -m_alpha;
        M(n,n-jump) = -m_alpha;
      }
      n++;
      }
    }
  return M;
}
