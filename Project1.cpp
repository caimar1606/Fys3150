#include <iostream>
#include <cmath>
#include <armadillo>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include "time.h"

using namespace std;
using namespace arma;
using namespace std;

ofstream ofile;
vec f(vec);
double exact(double);

int main(int argc,char *argv[]) //argv[1] = name of the output file, argv[2] = power, which gives the smallest stepsize h = 10**(-power)
{

  string output = argv[1];
  int power = atof(argv[2]);


  for(int i = 1; i<=power; i+=1) //computes the fast version of the algorithm
    {

      string fileout = output;
      string argument = to_string(i);
      fileout.append(argument);
      double h = pow(10,-i);
      int n = 1/h;
      vec x = linspace(0,1,n);
      vec btilde = h*h*f(x);
      vec sol = vec(n,fill::zeros);
      vec g = vec(n,fill::zeros);
      vec dtilde = vec(n,fill::zeros);

      for(int j=1;j<=n-1;j+=1)
      {
        dtilde(j) = (j+1)/double(j);
      }
      for(int j=2;j<=n-2;j+=1)
      {
        g(j) = btilde(j)-g(j-1)/dtilde(j-1);
      }

      for(int j=n-2;j>=1;j-=1)
      {
        sol(j)=(g(j)-sol(j+1))/dtilde(j);
      }
      ofile.open(fileout);
      ofile << setiosflags(ios::showpoint | ios::uppercase);
      ofile << "       x:             approx:          exact:       relative error" << endl;
      for (int i = 1; i < n;i+=1)
      {
	       double RelativeError = fabs((exact(x(i))-sol(i))/exact(x(i)));
	       ofile << setw(15) << setprecision(8) << x(i);
	       ofile << setw(15) << setprecision(8) << sol(i);
	       ofile << setw(15) << setprecision(8) << exact(x(i));
         ofile << setw(15) << setprecision(8) << log10(RelativeError) << endl;
      }
      ofile.close();
    }

  return 0;
}

vec f(vec x)
{
  return 100*exp(-10*x);
}
double exact(double x)
{
  return 1-(1-exp(-10))*x-exp(-10*x);
}
/*
dmat d = mat(n,n,fill::zeros);

for(int j=0; j<=n-1;j+=1)
{
  for(int k=0; k<=n-1;k+=1)
  {
    if(j==k)
    {
      d(j,k)=2;
    }
    else if(j-1==k)
    {
      d(j,k)=-1;
    }
    else if(k-1==j)
    {
      d(j,k)=-1;
    }
  }
}
*/
