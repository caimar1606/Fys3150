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
vec thomas(int);

int main(int argc,char *argv[]) //argv[1] = name of the output file, argv[2] = power, which gives the smallest stepsize h = 10**(-power)
{
  string output = argv[1];
  int power = atof(argv[2]);

  string clockffast = "timefast";
  ofile.open(clockffast);
  ofile << setiosflags(ios::showpoint | ios::uppercase);
  ofile << "power of n:    time:" << endl;
  ofile.close();

  string clockfslow = "timeslow";
  ofile.open(clockfslow);
  ofile << setiosflags(ios::showpoint | ios::uppercase);
  ofile << "power of n:    time:" << endl;
  ofile.close();


  for(int i = 1; i<=power; i+=1)
    {
      //computes the fast version of the algorithm

      string fileout = output;
      string argument = to_string(i);
      fileout.append(argument);
      fileout.append("fast");

      double h = pow(10,-i);
      int n = 1/h;

      vec x = linspace(0,1,n);
      vec btilde = h*h*f(x);
      vec sol = vec(n,fill::zeros);
      vec g = vec(n,fill::zeros);
      vec dtilde = thomas(n);

      clock_t start, finish;
      start = clock();

      g(0)=btilde(0);

      for(int j=1;j<=n-1;j+=1)
      {
        g(j) = btilde(j)+g(j-1)/dtilde(j-1);
      }
      for(int j=n-2;j>=0;j-=1)
      {
        sol(j)=(g(j)+sol(j+1))/dtilde(j);
      }

      finish = clock();
      double cps = CLOCKS_PER_SEC;
      double time =(finish - start)/cps;
      ofile.open(clockffast,ios::app);
      ofile << setiosflags(ios::scientific | ios::uppercase | ios::left);
      ofile << setw(15) << i;
      ofile << setw(15) << setprecision(8) << time << endl;
      ofile.close();

      ofile.open(fileout);
      ofile << setiosflags(ios::showpoint | ios::uppercase);
      ofile << "       x:             approx:          exact:       relative error" << endl;
      for (int i = 1; i < n;i+=1)
      {
	       double RelativeError = fabs((exact(x(i))-sol(i))/exact(x(i)));
	       ofile << setw(18) << setprecision(8) << x(i);
	       ofile << setw(18) << setprecision(8) << sol(i);
	       ofile << setw(18) << setprecision(8) << exact(x(i));
         ofile << setw(18) << setprecision(8) << log10(RelativeError) << endl;
      }
      ofile.close();

      fileout = output;
      argument = to_string(i);
      fileout.append(argument);
      fileout.append("slow");

      vec as = vec(n-1,fill::zeros);
      vec bs = vec(n,fill::zeros);
      vec cs = vec(n-1,fill::zeros);
      vec btildes = h*h*f(x);
      vec sols = vec(n,fill::zeros);

      vec gs = vec(n,fill::zeros);
      vec ds = vec(n,fill::zeros);

      start = clock();

      ds(0) = 2;
      gs(0) = btildes(0);

      for(int j =0; j<n-1;j+=1)
      {
        as(j)=-1;
      }
      for(int j =0; j<n-1;j+=1)
      {
        cs(j)=-1;
      }
      for(int j =0; j<n;j+=1)
      {
        bs(j)=2;
      }

      for(int j = 1;j<=n-1;j+=1)
      {
        ds(j) = bs(j)-as(j-1)*cs(j-1)/ds(j-1);
        gs(j) = btilde(j)-as(j-1)*gs(j-1)/ds(j-1);
      }

      for(int j = n-2;j>=0;j-=1)
      {
        sols(j)=(gs(j)-cs(j)*sols(j+1))/ds(j);
      }

      finish = clock();
      time =(finish - start)/cps;

      ofile.open(clockfslow,ios::app);
      ofile << setiosflags(ios::scientific | ios::uppercase | ios::left);
      ofile << setw(15) << i;
      ofile << setw(15) << setprecision(8) << time << endl;
      ofile.close();

      ofile.open(fileout);
      ofile << setiosflags(ios::showpoint | ios::uppercase);
      ofile << "       x:             approx:          exact:       relative error" << endl;
      for (int i = 1; i < n;i+=1)
      {
         double RelativeError = fabs((exact(x(i))-sols(i))/exact(x(i)));
         ofile << setw(18) << setprecision(8) << x(i);
         ofile << setw(18) << setprecision(8) << sols(i);
         ofile << setw(18) << setprecision(8) << exact(x(i));
         ofile << setw(18) << setprecision(8) << log10(RelativeError) << endl;
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

vec thomas(int n)
{
  vec values = linspace(1,n,n);
  return (values+1)/values;
}
