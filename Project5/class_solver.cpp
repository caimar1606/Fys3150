#include "project5.hpp"
#include <iostream>
#include <armadillo>
#include <cstdlib>
#include <iomanip>

using namespace std;
using namespace arma;

ofstream ofile;

void solver::init(double L,double T, int nt, int nx){
  m_L = L;
  m_T = T;
  m_dt = T/(nt-1);
  m_dx = L/(nx-1);
  m_nt = nt;
  m_nx = nx;
  m_alpha = m_dt/m_dx/m_dx;
  m_v = mat(nx,nt,fill::zeros);
  m_v(span(1,nx-2),0) = -1/L*linspace(m_dx,L-m_dx,nx-2);
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
  vec dtilde = vec(m_nx,fill::zeros);
  dtilde +=vec(m_nx,fill::ones)*diag;
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

  vec dtilde = vec(m_nx,fill::zeros);
  dtilde +=vec(m_nx,fill::ones)*diag;

  for(int i =1;i<m_nx;i++){
    dtilde(i)-=ee/dtilde(i-1);
  }
  mat multmat = mat(m_nx,m_nx,fill::eye)*diagD;
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


void solver::trigsolve(vec gtilde, vec dtilde, double e, int t){
  for(int i = 1; i < m_nx;i++){
    gtilde(i)-=e*gtilde(i-1)/dtilde(i-1);
  }
  for(int i = m_nx-2;i >0;i--){
    m_v(i,t+1) = (gtilde(i)-e*m_v(i+1,t+1))/dtilde(i);
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
