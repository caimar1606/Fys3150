#include "solarsystem.hpp"
#include <armadillo>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <math.h>

using namespace arma;
using namespace std;

ofstream ofile;

void solarsystem::initialize(int total, double beta, double rel){
  m_M = vec(total,fill::zeros);
  m_rstart = vec(2*total, fill::zeros);
  m_vstart = vec(2*total, fill::zeros);
  m_GdM = vec(total,fill::zeros);
  m_planets = 0;
  m_beta = beta;
  m_rel = rel;
}

void solarsystem::add_planet(double mass, vec rstart, vec vstart){
  m_M(m_planets) = mass;
  m_rstart(span(m_planets*2,m_planets*2+1)) = rstart;
  m_vstart(span(m_planets*2,m_planets*2+1)) = vstart;
  m_GdM(m_planets) = 4*M_PI*M_PI*mass;
  m_planets += 1;
}

void solarsystem::solve_euler(double Tmax, double h){
  int N = floor(Tmax/h)+1;
  m_r = mat(N,m_planets*2,fill::zeros);
  m_v = mat(N,m_planets*2,fill::zeros);
  m_r.row(0) = m_rstart.t();
  m_v.row(0) = m_vstart.t();
  for(int i = 0; i<N-1;i++){
    for(int j = 0; j<m_planets;j++){
      m_v(i+1,span(j*2,j*2+1)) = m_v(i,span(j*2,j*2+1))+h*accel(j,i);
      m_r(i+1,span(j*2,j*2+1)) = m_r(i,span(j*2,j*2+1))+h*m_v(i,span(j*2,j*2+1));
    }
  }
}

void solarsystem::solve_verlet(double Tmax, double h){
  int N = floor(Tmax/h)+1;
  m_r = mat(N,m_planets*2,fill::zeros);
  m_v = mat(N,m_planets*2,fill::zeros);
  m_r.row(0) = m_rstart.t();
  m_v.row(0) = m_vstart.t();
  for(int i = 0; i<N-1;i++){
    for(int j = 0; j<m_planets;j++){
      m_r(i+1,span(j*2,j*2+1)) = m_r(i,span(j*2,j*2+1))+h*m_v(i,span(j*2,j*2+1))+accel(j,i)*h*h/2;
    }
    for(int k =0; k<m_planets;k++){
      m_v(i+1,span(k*2,k*2+1)) = m_v(i,span(k*2,k*2+1))+(accel(k,i+1)+accel(k,i))*h/2;
    }
  }
}

mat solarsystem::accel(int planet, int step){
  mat a = mat(1,2,fill::zeros);
  double len, clen;
  mat vectr, vectv;
  if (m_rel ==0){
    for(int i=0; i< m_planets;i++){
      if(i==planet) continue;
      len = norm(m_r(step,span(planet*2,planet*2+1))-m_r(step,span(i*2,i*2+1)),2);
      a += -m_GdM(i)/(pow(len,m_beta+1))*(m_r(step,span(planet*2,planet*2+1))-m_r(step,span(i*2,i*2+1)));
    }
    return a;
  }
  else{
    for(int i=0; i< m_planets;i++){
      if(i==planet) continue;
      vectr = (m_r(step,span(planet*2,planet*2+1))-m_r(step,span(i*2,i*2+1)));
      vectv = (m_v(step,span(planet*2,planet*2+1))-m_v(step,span(i*2,i*2+1)));
      len = norm(m_r(step,span(planet*2,planet*2+1))-m_r(step,span(i*2,i*2+1)),2);
      clen = vectr(0,0)*vectv(0,1)-vectr(0,1)*vectv(0,0);
      a -= m_GdM(i)/(pow(len,m_beta+1))*vectr*(1+3*clen*clen/(len*len*63240*63240));
    }
    return a;
  }
}

void solarsystem::print(string outputr, string outputv, int skip){
  for(int k=0; k < m_planets; k++){
    string filename = outputr + to_string(k)+".txt";
    ofile.open(filename);
    ofile << setiosflags(ios::scientific | ios::uppercase);
    ofile << setw(18) << setprecision(8) << "x";
    ofile << setw(18) << setprecision(8) << "y"<<"\n";
    for (int i = 0; i < m_r.n_rows; i+=skip){
      ofile << setw(18) << setprecision(8) << m_r(i,2*k);
      ofile << setw(18) << setprecision(8) << m_r(i,2*k+1)<<"\n";
    }
    ofile.close();
  }
  for(int k=0; k < m_planets; k++){
    string filename = outputv + to_string(k)+".txt";
    ofile.open(filename);
    ofile << setiosflags(ios::scientific | ios::uppercase);
    ofile << setw(18) << setprecision(8) << "x";
    ofile << setw(18) << setprecision(8) << "y"<<"\n";
    for (int i = 0; i < m_r.n_rows; i+=skip){
      ofile << setw(8) << setprecision(8) << m_v(i,2*k);
      ofile << setw(18) << setprecision(8) << m_v(i,2*k+1)<<"\n";
    }
    ofile.close();
  }
}
